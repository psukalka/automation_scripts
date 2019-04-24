# Run these commands from iPython or directly create some py file and paste it there.
from kurma.utils.fsutils import get_system_config
from kurma.utils.metautils import get_instance_id
from kurma.utils.metautils import get_from_mars_with_retry
from marsclient.client import MARSClient
import logging
import grpc
from time import sleep
l = logging.getLogger('test.log')
sys_config = get_system_config('sys_globals')
mc = MARSClient(config = sys_config["model_repo"], instance_id=get_instance_id(sys_config), logger = l)
num_tries = 3

def get_analyser(num_tries=3):
        while num_tries >= 0:
                try:
                        conf = mc.getanalyserconfig(analyser_version="FUNDUS-0.0.17")
                        print(conf)
                        return conf
                except grpc.RpcError as e:
                        err_msg = "Error occurred while fetching analyser config. Status_code: {}, details: {}".format(e.code(), e.details())
                        print(err_msg)
                        if e.code() == grpc.StatusCode.UNAVAILABLE:
                                num_tries -= 1
                                print("MARS Client is unavailable. Retrying ...")
                                sleep(2)
                        else:
                                break
                except Exception as e:
                        raise e
        raise Exception("msg")
# conf = get_analyser()
get_from_mars_with_retry(l, mc.getanalyserconfig, analyser_version="FUNDUS-0.0.7")
