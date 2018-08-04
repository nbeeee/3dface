#!/usr/bin/python

import dlib
import numpy as np
import cv2
import os
import scipy.io as sio
from skimage.io import imread, imsave
from skimage.transform import rescale, resize
import api as PRN
from utils.cv_plot import plot_kpt, plot_vertices, plot_pose_box
from utils.estimate_pose import estimate_pose
from utils.rotate_vertices import frontalize
from utils.render_app import get_visibility, get_uv_mask, get_depth_image
from utils.write import write_obj, write_obj_with_texture

detector = dlib.get_frontal_face_detector()
facepath = 'face/face.jpg'
save_folder = 'model/'
def faceDetector(frame):
    if os.path.exists(facepath):
        os.remove(facepath)
    dets = detector(frame, 1)
    print("Number of faces detected: {}".format(len(dets)))
    if(len(dets) == 0): return

    face = dets[0]

    # 计算矩形框大小
    height = face.bottom()
    width = face.right()
    box = np.zeros((height, width, 3), np.uint8)
    for i in range(height):
        for j in range(width):
            box[i][j] = frame[i][int(face.left() /2) + j]

    cv2.imwrite('face/face.jpg',box)


def gener3DFace():
    print('create 3d face ...........')
    name = "screen"
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
    prn = PRN.PRN(is_dlib=True,prefix='PRNet/')
    # read image
    image = cv2.imread(facepath)
    [h, w, _] = image.shape
    max_size = max(image.shape[0], image.shape[1])
    if max_size > 1000:
        image = cv2.rescale(image, 1000. / max_size)
        image = (image * 255).astype(np.uint8)
    pos = prn.process(image)  # use dlib to detect face
    image = image / 255.
    # 3D vertices
    vertices = prn.get_vertices(pos)
    save_vertices = vertices.copy()
    save_vertices[:, 1] = h - 1 - save_vertices[:, 1]
    colors = prn.get_colors(image, vertices)
    texture = cv2.remap(image, pos[:, :, :2].astype(np.float32), None, interpolation=cv2.INTER_NEAREST,
                        borderMode=cv2.BORDER_CONSTANT, borderValue=(0))
    vertices_vis = get_visibility(vertices, prn.triangles, h, w)
    uv_mask = get_uv_mask(vertices_vis, prn.triangles, prn.uv_coords, h, w, prn.resolution_op)
    texture = texture * uv_mask[:, :, np.newaxis]
    write_obj_with_texture(os.path.join(save_folder, name + '.obj'), save_vertices, colors, prn.triangles, texture,
                           prn.uv_coords / prn.resolution_op)  # save 3d face with texture(can open with meshlab)
    sio.savemat(os.path.join(save_folder, name + '_mesh.mat'),
                {'vertices': vertices, 'colors': colors, 'triangles': prn.triangles})
    kpt = prn.get_landmarks(pos)
    np.savetxt(os.path.join(save_folder, name + '_kpt.txt'), kpt)
    '''

    '''
    camera_matrix, pose = estimate_pose(vertices)
    np.savetxt(os.path.join(save_folder, name + '_pose.txt'), pose)
    np.savetxt(os.path.join(save_folder, name + '_camera_matrix.txt'), camera_matrix)

    np.savetxt(os.path.join(save_folder, name + '_pose.txt'), pose)

    #image_pose = plot_pose_box(image, camera_matrix, kpt)
    #cv2.imshow('sparse alignment', plot_kpt(image, kpt))
    #cv2.imshow('dense alignment', plot_vertices(image, vertices))
    image = plot_vertices(image, vertices)
    return image
    #cv2.imshow('pose', plot_pose_box(image, camera_matrix, kpt))
    #cv2.waitKey(0)


