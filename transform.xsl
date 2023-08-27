<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output method="html" indent="yes"/>

  <xsl:template match="/">
    <html>
      <head>
        <title>Product Catalog</title>
      </head>
      <body>
        <h1>Product Catalog</h1>
        <xsl:apply-templates select="products/product"/>
      </body>
    </html>
  </xsl:template>

  <xsl:template match="product">
    <div class="product">
      <h2><xsl:value-of select="name"/></h2>
      <p>Price: <xsl:value-of select="price"/></p>
      <p><xsl:value-of select="description"/></p>
    </div>
  </xsl:template>
</xsl:stylesheet>