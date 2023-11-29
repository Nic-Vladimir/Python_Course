contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced.",
            "The slices were evaluated as sliced correctly."]

filenames = ["doc.txt", "reports.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"Files/{filename}", 'w')
    file.write(content)
