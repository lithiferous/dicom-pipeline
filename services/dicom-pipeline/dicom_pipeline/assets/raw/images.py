"""
This module specifies the Attributes that identify and describe an image within a particular Series.
"""
columns = [
'AcquisitionDate',
'AcquisitionDuration',
'AcquisitionMatrix',
'AcquisitionNumber',
'AcquisitionTime',
'AngioFlag',
'BeatRejectionFlag',
'BitsAllocated',
'BitsStored',
'BurnedInAnnotation',  
'Columns',
'ContentDate',
'ContentQualification',
'ContentTime',
'ContrastBolusVolume',
'dBdt',
'EchoNumbers',
'EchoTime',
'EchoTrainLength',
'FlipAngle',    
'GeometryOfKSpaceTraversal',
'HeartRate',
'HighBit',
'HighRRValue',
'ImageComments',
'ImagedNucleus',
'ImageOrientationPatient',
'ImagePositionPatient',
'ImagesInAcquisition',
'ImageType',
'ImagingFrequency',
'InPlanePhaseEncodingDirection',
'InStackPositionNumber',
'InstanceCreationDate',
'InstanceCreationTime',
'InstanceCreatorUID',
'InstanceNumber',
'IntervalsAcquired',
'IntervalsRejected',
'InversionTime',
'LargestImagePixelValue',
'Laterality',
'LossyImageCompression',
'LowRRValue',
'MagneticFieldStrength',
'MRAcquisitionType',
'NominalInterval',
'NumberOfAverages',
'NumberOfFrames',
'NumberOfKSpaceTrajectories',
'NumberOfPhaseEncodingSteps',
'ParallelAcquisition',
'ParallelAcquisitionTechnique',
'PatientPosition', 
'PercentPhaseFieldOfView',
'PercentSampling',
'PhotometricInterpretation',
'PixelAspectRatio',
'PixelBandwidth',
'PixelRepresentation',
'PixelSpacing',
'ReceiveCoilName',
'ReconstructionDiameter',
'RectilinearPhaseEncodeReordering',
'ReferencedImageSequence',
'RepetitionTime',
'Rows',
'SamplesPerPixel', 
'SAR',
'SaturationRecovery',
'ScanningSequence',
'ScanOptions',
'SequenceName',
'SequenceVariant',
'SeriesInstanceUID',
'SharedFunctionalGroupsSequence',
'SkipBeats',
'SliceLocation',  
'SliceThickness',
'SmallestImagePixelValue',
'SOPClassUID',
'SOPInstanceUID',
'SpacingBetweenSlices',
'SpecificCharacterSet',
'StackID',
'TemporalPositionIndex',
'TransmitCoilName',
'TriggerTime',
'TriggerWindow',
'VariableFlipAngleFlag',
'WindowCenter',
'WindowCenterWidthExplanation',
'WindowWidth',
]

from .lib import *

@asset(
	metadata={"partition_expr": COLUMN_PARTITION_MAP["images"]},
	auto_materialize_policy=AutoMaterializePolicy.eager(),
	partitions_def=PARTITION_MONTHLY,
	compute_kind="pandas",
)
def images(
	context: AssetExecutionContext,
	config: RawConfig,
)-> pd.DataFrame:
    """
    An image within a particular Series.
    """
    return read_dicom_file_to_df(context, config)