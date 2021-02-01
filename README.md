# ACM Research Coding Challenge (Spring 2021)

## No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## Submission Procedure

Please follow the below instructions on how to submit your answers.

1. Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge-S21`. To fork this repo, click the button on the top right and click the "Fork" button.
2. Clone the fork of the repo to your computer using `git clone [the URL of your clone]`. You may need to install Git for this (Google it).
3. Complete the Challenge based on the instructions below.
4. Submit your solution by filling out this [form](https://acmutd.typeform.com/to/uqAJNXUe).

## Question One

Genome analysis is the identification of genomic features such as gene expression or DNA sequences in an individual's genetic makeup. A genbank file (.gb) format contains information about an individual's DNA sequence. The following dataset in `Genome.gb` contains a complete genome sequence of Tomato Curly Stunt Virus. 

**With this file, create a circular genome map and output it as a JPG/PNG/JPEG format.** We're not looking for any complex maps, just be sure to highlight the features and their labels.

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!


Python Libaraies used:
  https://www.reportlab.com/dev/opensource/rl-toolkit/
  https://www.tutorialspoint.com/biopython/index.htm
  Changing opacity with reportlab: https://www.reportlab.com/snippets/9/
  Biopython reference: http://biopython.org/DIST/docs/tutorial/Tutorial.html
  
Process:
  Initially when approaching the prompt, I decided to make an attempt in C++ (even though it was recommended to use python) due to the fact that my most recent programming experience was done through C++. After doing enough research to understand what the .gb file was actually saying, and what I had to do with the data, I began at what I thought would be the most difficult part of the program: creating an image. I found a simple drawing library for C++ called CImg (which was very easy to import as the entire library was contained to a single header file), and came up with the idea to make the image by overlaying parts of circles on a white background to create the effect of a ring shape, representing different protein sequences. I thought this idea would work if I made the length of the ring proportional to the number of bases in the protein per the total number of bases, and have the ring start at a proportional point to where the protein started in the gene sequence. Eventually, though, I ran into trouble when attempting to draw only fractions of a circle, instead of a whole, to represent the individual proteins. After spending a significant time trying to implement my idea, I decided to start from scratch in Python, since the prompt said that would make implementation the easiest.
  After switching languages, I decided to do some further googling on how to go about implementing the project, which is when I stumbled upon the BioPython library. I looked into the library, and upon skimming through the library's tutorial page, I spotted a circular genome map (almost exactly what I wanted to produce). Luckily for me, who has had close to no exposure to Python, above the image came a full tutorial on how to produce a circular genome map using a .gb file. After implementing and testing this code, I noticed my image seemed to have overlapping protein, which prompted me to figure out how to change the opacity of the colors I used. After solving this issue, I decided that the image I was producing was pretty clear to read, and contained the proper features and protein lables.
