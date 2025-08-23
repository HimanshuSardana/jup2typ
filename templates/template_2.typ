#show raw: set text(font: "Iosevka NF")

#let title(content) = [
  #box(width: 100%, fill: blue.lighten(80%), inset: 10pt)[
    #align(center + horizon)[
      #text(font: "Montserrat", weight: "bold", size: 12pt, fill: blue)[#content]
    ]
  ]
]

#let question(number, body) = context [
  #block(inset: 12pt, radius: 5pt, width: 100%, fill: blue.lighten(82%))[
    #text(font: "Montserrat", weight: "bold", size: 9pt, fill: blue)[Question #number] \
    #text(font: "Montserrat", size: 10pt)[#body]
  ]
]

#let solution(content) = [
  #block(inset: 12pt, radius: 5pt, width: 100%, stroke: (thickness: 1.3pt, dash: "dashed", paint: blue))[
    #text(font: "Montserrat", weight: "bold", size: 9pt, fill: blue)[Solution] \
    #v(-2mm)
    #text(font: "Montserrat", size: 10pt)[#content]
  ]
]

#let output(content) = [
  #block(inset: 5pt, radius: 5pt, width: 100%)[
    #text(font: "Montserrat", weight: "bold", size: 9pt, fill: blue)[Output] \
    #v(-2mm)
    #text(font: "Montserrat", size: 10pt)[#content]
  ]
]

