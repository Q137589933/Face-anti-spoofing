from torch.autograd import Variable
import torchvision
import torch
import cv2
from torchvision import transforms
import numpy as np
from PIL import Image
import torch.nn.functional as F

from dynamic.hopenet import Hopenet


def face_direction_detect(img, model, right_head=0, device='cpu'):
    # 0为左转头 1为右转头
    transformations = transforms.Compose([transforms.Resize(224),
                                          transforms.CenterCrop(224), transforms.ToTensor(),
                                          transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])])
    # cv2.rectangle(img,(200,120),(440,360),(0,255,0),2)
    # img[:480,:200,:] = np.full((480,200,3),0)
    # img[:480,440:,:] = np.full((480,200,3),0)
    # img[:120,200:440,:] = np.full((120,240,3),0)
    # img[360:,200:440,:] = np.full((120,240,3),0)

    # roi_img = img[120:360,200:440]
    yaw, _ = pred_yaw(model, img, transformations, device)
    if not right_head:
        if yaw.data.cpu().numpy().tolist() <= -30:
            return True
    else:
        if yaw.data.cpu().numpy().tolist() >= 30:
            return True
    return False


def read_img(path):
    img = cv2.imdecode(np.fromfile(path, np.uint8),
                       cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img


def load_model(path, device='cpu'):
    model = Hopenet(torchvision.models.resnet.Bottleneck, [3, 4, 6, 3], 66)
    model.load_state_dict(torch.load(path))
    model.to(device)
    model.eval()
    return model


def pred_yaw(model, img, transformations=None, device='cpu'):
    if transformations is not None:
        img = transformations(Image.fromarray(img))
    idx_tensor = [idx for idx in range(66)]
    idx_tensor = torch.FloatTensor(idx_tensor).to(device)
    img_shape = img.size()
    img = img.view(1, img_shape[0], img_shape[1], img_shape[2])
    img = Variable(img).to(device)

    yaw, pitch, roll = model(img)
    yaw_pred = F.softmax(yaw, dim=1)
    yaw_pred = torch.sum(yaw_pred.data[0] * idx_tensor) * 3 - 99
    pitch_pred = F.softmax(pitch, dim=1)
    pitch_pred = torch.sum(pitch_pred.data[0] * idx_tensor) * 3 - 99
    return yaw_pred, pitch_pred
