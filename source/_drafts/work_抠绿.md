1. 抠绿
	for (int row = 0; row < img.rows; row++){
		for (int col = 0; col < img.cols; col++){
			if (img.at<Vec3b>(row, col)[1]>150 && img.at<Vec3b>(row, col)[1]<210) //绿
			{
				if (img.at<Vec3b>(row, col)[0]<140 && img.at<Vec3b>(row, col)[0]>80) //蓝
					if (img.at<Vec3b>(row, col)[2]>70 && img.at<Vec3b>(row, col)[2]<130) //红
					{
						img.at<Vec3b>(row, col)[0] = 255;
						img.at<Vec3b>(row, col)[1] = 255;
						img.at<Vec3b>(row, col)[2] = 255;
					}
			}
		}
	}