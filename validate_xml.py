from lxml import etree

# Load XSLT stylesheet
xslt = etree.parse("transform.xsl")
transform = etree.XSLT(xslt)

# Transform XML to HTML
xml = etree.parse("products.xml")
html_output = transform(xml)

# Save transformed HTML
with open("output.html", "wb") as output_file:
    output_file.write(etree.tostring(html_output, pretty_print=True))

# Load XSD schema
xsd = etree.parse("product_schema.xsd")
schema = etree.XMLSchema(xsd)

# Validate transformed HTML against XSD schema
html = etree.parse("output.html")
validation_result = schema.validate(html)

if validation_result:
    print("Validation successful.")
else:
    print("Validation failed. Errors:")
    for error in schema.error_log:
        print(error)
