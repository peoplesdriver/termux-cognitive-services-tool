from settings import create_cv_client

# Describe a local image by:
#   1. Opening the binary file for reading.
#   2. Defining what to extract from the image by initializing an array of VisualFeatureTypes.
#   3. Calling the Computer Vision service's analyze_image_in_stream with the:
#      - image
#      - features to extract
#   4. Displaying the image captions and their confidence values.

def local_img_analyzer(local_image_path):
    computervision_client = create_cv_client()

    local_image = open(local_image_path, "rb")
    local_image_description = computervision_client.describe_image_in_stream(local_image)

    print("\nCaptions from local image: ")
    if (len(local_image_description.captions) == 0):
        print("No captions detected.")
    else:
        for caption in local_image_description.captions:
            print("'{}' >>> {:.2f}%".format(caption.text, caption.confidence * 100))
    #  END - Describe a local image


# Describe a remote image by:
#   1. Defining what to extract from the image by initializing an array of VisualFeatureTypes.
#   2. Calling the Computer Vision service's analyze_image with the:
#      - image URL
#      - features to extract
#   3. Displaying the image captions and their confidence values.

def remote_img_analyzer(remote_image_url):
    computervision_client = create_cv_client()
    remote_image_description = computervision_client.describe_image(remote_image_url)

    print("\nCaptions from remote image: ")
    if (len(remote_image_description.captions) == 0):
        print("No captions detected.")
    else:
        for caption in remote_image_description.captions:
            print("'{}' >>> {:.2f}%".format(caption.text, caption.confidence * 100))


# Categorize a remote image by:
#   1. Calling the Computer Vision service's analyze_image with the:
#      - image URL
#      - features to extract
#   2. Displaying the image categories and their confidence values.


def remote_img_categoryzer(remote_image_url):
    computervision_client = create_cv_client()

    remote_image_features = ["categories"]
    remote_image_analysis = computervision_client.analyze_image(remote_image_url, remote_image_features)

    print("\nCategories from remote image: ")
    if (len(remote_image_analysis.categories) == 0):
        print("No categories detected.")
    else:
        for category in remote_image_analysis.categories:
            print("'{}' with confidence {:.2f}%".format(category.name, category.score * 100))



# Tag a remote image by:
#   1. Calling the Computer Vision service's analyze_image with the:
#      - image URL
#      - features to extract
#   2. Displaying the image captions and their confidence values.

def remote_img_tags(remote_image_url):
    computervision_client = create_cv_client()

    remote_image_tags = computervision_client.tag_image(remote_image_url)

    print("\nTags in the remote image: ")
    if (len(remote_image_tags.tags) == 0):
        print("No tags detected.")
    else:
        for tag in remote_image_tags.tags:
            print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))




#   Detect objects in a remote image by:
#   1. Opening the binary file for reading.
#   2. Calling the Computer Vision service's detect_objects with the:
#      - image
#      - features to extract
#   3. Displaying the location of the objects.

def remote_img_detect(remote_image_url):
    computervision_client = create_cv_client()

    remote_image_objects = computervision_client.detect_objects(remote_image_url)

    print("\nDetecting objects in remote image:")
    if len(remote_image_objects.objects) == 0:
        print("No objects detected.")
    else:
        for object in remote_image_objects.objects:
            print("object at location {}, {}, {}, {}".format( \
            object.rectangle.x, object.rectangle.x + object.rectangle.w, \
            object.rectangle.y, object.rectangle.y + object.rectangle.h))


#   Detect objects in a remote image by:
#   1. Opening the binary file for reading.
#   2. Calling the Computer Vision service's detect_objects with the:
#      - image
#      - features to extract
#   3. Displaying the location of the objects.

def remote_img_brands(remote_image_url):
    computervision_client = create_cv_client()

    remote_image_objects = computervision_client.detect_objects(remote_image_url)

    print("\nDetecting objects in remote image:")
    if len(remote_image_objects.objects) == 0:
        print("No objects detected.")
    else:
        for object in remote_image_objects.objects:
            print("object at location {}, {}, {}, {}".format( \
            object.rectangle.x, object.rectangle.x + object.rectangle.w, \
            object.rectangle.y, object.rectangle.y + object.rectangle.h))


# Detect faces in a remote image by:
#   1. Calling the Computer Vision service's analyze_image with the:
#      - image URL
#      - features to extract
#   2. Displaying the image captions and their confidence values.

def remote_img_face_detect(remote_image_url):
    computervision_client = create_cv_client()

    remote_image_features = ["faces"]
    remote_image_analysis = computervision_client.analyze_image(remote_image_url, remote_image_features)

    print("\nFaces in the remote image: ")
    if (len(remote_image_analysis.faces) == 0):
        print("No faces detected.")
    else:
        for face in remote_image_analysis.faces:
            print("'{}' of age {} at location {}, {}, {}, {}".format(face.gender, face.age, \
            face.face_rectangle.left, face.face_rectangle.top, \
            face.face_rectangle.left + face.face_rectangle.width, \
            face.face_rectangle.top + face.face_rectangle.height))


# Detect adult or racy content in a remote image by:
#   1. Calling the Computer Vision service's analyze_image with the:
#      - image URL
#      - features to extract
#   2. Displaying the image captions and their confidence values.

def remote_img_adult_detect(remote_image_url):
    computervision_client = create_cv_client()

    remote_image_features = ["adult"]
    remote_image_analysis = computervision_client.analyze_image(remote_image_url, remote_image_features)

    print("\nAnalyzing remote image for adult or racy content ... ")
    print("Is adult content: {} with confidence {:.2f}%".format(remote_image_analysis.adult.is_adult_content, local_image_analysis.adult.adult_score * 100))
    print("Has racy content: {} with confidence {:.2f}%".format(remote_image_analysis.adult.is_racy_content, local_image_analysis.adult.racy_score * 100))


# Detect the color scheme of a remote image by:
#   1. Calling the Computer Vision service's analyze_image with the:
#      - image
#      - features to extract
#   2. Displaying color scheme of the local image.

def remote_get_color(remote_image_url):
    computervision_client = create_cv_client()

    remote_image_features = ["color"]
    remote_image_analysis = computervision_client.analyze_image(remote_image_url, remote_image_features)

    print("\nColor scheme of the remote image: ");
    print("Is black and white: ".format(remote_image_analysis.color.is_bw_img))
    print("Accent color: 0x{}".format(remote_image_analysis.color.accent_color))
    print("Dominant background color: {}".format(remote_image_analysis.color.dominant_color_background))
    print("Dominant foreground color: {}".format(remote_image_analysis.color.dominant_color_foreground))
    print("Dominant colors: {}".format(remote_image_analysis.color.dominant_colors))



#   Detect domain-specific content (celebrities/landmarks) in a remote image by:
#   1. Calling the Computer Vision service's analyze_image_by_domain with the:
#      - domain-specific content to search for
#      - image
#   2. Displaying any domain-specific content (celebrities/landmarks).

def remote_get_coustom(remote_image_url):
    computervision_client = create_cv_client()

    remote_image_celebs = computervision_client.analyze_image_by_domain("celebrities", remote_image_url)

    print("\nCelebrities in the remote image:")
    if len(remote_image_celebs.result["celebrities"]) == 0:
        print("No celebrities detected.")
    else:
        for celeb in remote_image_celebs.result["celebrities"]:
            print(celeb["name"])



#   Detect image types (clip art/line drawing) of a remote image by:
#   1. Calling the Computer Vision service's analyze_image with the:
#      - image
#      - features to extract
#   2. Displaying the image type.

def remote_img_type(remote_image_url):
    computervision_client = create_cv_client()

    remote_image_features = VisualFeatureTypes.image_type
    remote_image_analysis = computervision_client.analyze_image(remote_image_url, remote_image_features)


    print("\nImage type of remote image:")
    if remote_image_analysis.image_type.clip_art_type == 0:
        print("Image is not clip art.")
    elif remote_image_analysis.image_type.line_drawing_type == 1:
        print("Image is ambiguously clip art.")
    elif remote_image_analysis.image_type.line_drawing_type == 2:
        print("Image is normal clip art.")
    else:
        print("Image is good clip art.")

    if remote_image_analysis.image_type.line_drawing_type == 0:
        print("Image is not a line drawing.")
    else:
        print("Image is a line drawing")



