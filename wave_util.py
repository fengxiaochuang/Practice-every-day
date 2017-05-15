# encoding: utf-8
import wave
import os.path


def get_wave_info(path):
    """
    获取wave文件信息
    :param path:
    :return:
    """
    if os.path.exists(path):
        fh = wave.open(path, "r")
        info = fh.getparams()
        """
        info[0] channels 单声道 or 双声道
        info[3] frames
        info[3] * info[1] * info[0] bye 字节 可以计算文件大小
        info[2] Hz sample size  采样率
        info[1] Bytes/sample 采样大小 * 8 bit = 比特率
        info[5] compression 压缩率
        """
        # 计算播放时间
        wave_time = "%d" % ((info[3] * info[1] * 1000) / info[2] / 2,)
        return info[0], info[1] * 8, info[2], wave_time, info[3] * info[1] * info[0]
    else:
        return False
