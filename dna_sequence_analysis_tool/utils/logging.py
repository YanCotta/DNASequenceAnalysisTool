import logging

# Configure the root logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

# Create a logger for the utils package
logger = logging.getLogger('dna_sequence_analysis_tool.utils')
