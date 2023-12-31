Original Repository: https://github.com/robyoung/dicom-test-files/

The files in this directory including this file have been
copied from https://github.com/pydicom/pydicom.

See: pydicom/pydicom#1112

## Test Files used for testing pydicom

I obtained images to test the pydicom code, and revised them as follow:

- images were often downsized to keep the total file size quite small (typically <50K-ish). I wanted unittests for the code where I could run a number of tests quickly, and with files I could include in the source (and binary) distributions without bloating them too much
- In some cases, the original files have been binary edited to replace anything that looks like a real patient name

I believe there is no restriction on using any of these files in this manner.
MR_small.dcm : Expl VR Little Endian

MR_small.dcm

- MR image, Explicit VR, LittleEndian
- Downsized to 64x64 from 'MR1_UNC', ftp://medical.nema.org/MEDICAL/Dicom/DataSets/WG04/
- Explicit VR big endian version created using DCMTK's dcmconv for PR #714

MR2\_\*.dcm

- JPEG2000, JPEG2000Lossless and uncompressed versions
- unsigned 16-bit/12-bit with rescale and windowing
- From ftp://medical.nema.org/MEDICAL/Dicom/DataSets/WG04

== DICOMDIR tests ==

dicomdirtests files were from http://www.pcir.org, freely available image sets.
They were downsized to 16x16 images to keep them very small so they
could be added to the source distribution without bloating it. For the
same reason, many were removed, leaving only samples of the studies,
series, and images.

For the subdirectories ending in "N" (e.g. CT2N, CT5N), the name indicates
the number of images inside the folder, i.e. CT2N has two images,
CT5N has five. This was a memory-aid for use in unit tests.

Below is the hierarchy of Patient, Study, Series, Images that comes from a
straight read of the dicomdirtests DICOMDIR file. The DICOMDIR file itself
was created using the dcmtk program dcmgpdir. It complained about different
Specific Character Set in some of the files, so some with 2022 IR6 were set
to ISO_IR 100.

Patient: 77654033: Doe^Archibald
Study 2: 20010101: XR C Spine Comp Min 4 Views
Series 1: CR: (1 image)
['./77654033/CR1/6154']
Series 2: CR: (1 image)
['./77654033/CR2/6247']
Series 3: CR: (1 image)
['./77654033/CR3/6278']
Study 2: 19950903: CT, HEAD/BRAIN WO CONTRAST
Series 2: CT: (4 images)
['./77654033/CT2/17106',
'./77654033/CT2/17136',
'./77654033/CT2/17166',
'./77654033/CT2/17196']

Patient: 98890234: Doe^Peter
Study 2: 20010101:
Series 4: CT: (2 images)
['./98892001/CT2N/6293',
'./98892001/CT2N/6924']
Series 5: CT: (5 images)
['./98892001/CT5N/2062',
'./98892001/CT5N/2392',
'./98892001/CT5N/2693',
'./98892001/CT5N/3023',
'./98892001/CT5N/3353']
Study 428: 20030505: Carotids
Series 1: MR: (1 image)
['./98892003/MR1/15820']
Series 2: MR: (1 image)
['./98892003/MR2/15970']
Study 134: 20030505: Brain
Series 1: MR: (1 image)
['./98892003/MR1/4919']
Series 2: MR: (3 images)
['./98892003/MR2/4950',
'./98892003/MR2/5011',
'./98892003/MR2/4981']
Study 2: 20030505: Brain-MRA
Series 1: MR: (1 image)
['./98892003/MR1/5641']
Series 2: MR: (3 images)
['./98892003/MR2/6935',
'./98892003/MR2/6605',
'./98892003/MR2/6273']
Series 700: MR: (7 images)
['./98892003/MR700/4558',
'./98892003/MR700/4528',
'./98892003/MR700/4588',
'./98892003/MR700/4467',
'./98892003/MR700/4618',
'./98892003/MR700/4678',
'./98892003/MR700/4648']

== Overlay Data ==

MR-SIEMENS-DICOM-WithOverlays.dcm (from GDCM)
_ Little Endian Explicit VR
_ Single frame, single channel Pixel Data
_ Single frame Overlay Data in group 0x6000
_ Icon Image Sequence \* 8-bit Palette Color LUT

== Licenses ==

The datasets from GDCM (github.com/malaterre/GDCM) are used under the following
license:

Program: GDCM (Grassroots DICOM). A DICOM library

Copyright (c) 2006-2016 Mathieu Malaterre
Copyright (c) 1993-2005 CREATIS
(CREATIS = Centre de Recherche et d'Applications en Traitement de l'Image)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.

- Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

- Neither name of Mathieu Malaterre, or CREATIS, nor the names of any
  contributors (CNRS, INSERM, UCB, Universite Lyon I), may be used to
  endorse or promote products derived from this software without specific
  prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS ``AS IS''
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE AUTHORS OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
