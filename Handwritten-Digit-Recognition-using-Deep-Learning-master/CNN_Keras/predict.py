count = 0
# Show the images using OpenCV and making random selections.
for num in np.random.choice(np.arange(0, len(test_labels)), size=(5,)):
	if count > 20:
		break
	# Predict the label of digit using CNN.
	probs = clf.predict(test_img[np.newaxis, num])
	prediction = probs.argmax(axis=1)

	# Resize the Image to 100x100 from 28x28 for better view.
	image = (test_img[num][0] * 255).astype("uint8")
	image = cv2.merge([image] * 3)
	image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_LINEAR)
	cv2.putText(image, str(prediction[0]), (5, 20),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

	# Show and print the Actual Image and Predicted Label Value
	print('Predicted Label: {}, Actual Value: {}'.format(prediction[0],np.argmax(test_labels[num])))
	name = "Digits" + str(count)
	cv2.save(name, image)
	count += 1