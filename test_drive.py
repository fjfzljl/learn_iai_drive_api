# import student

import pytest
import logging
import numpy as np
import imageio
from typing import NamedTuple

import invertedai as iai
from invertedai.api.drive import DriveResponse, drive
from invertedai.common import AgentState, RecurrentState, AgentAttributes, Point

# from libs.login_page import *

logger = logging.getLogger("drive test")


class ResultCode(NamedTuple):
    code: int
    description: str

Drive_OK = ResultCode(1, 'return class DriveResponse')
Drive_Crash = ResultCode(2, 'api iai.drive crash')




def verify_drive(location, agent_states, agent_attributes, recurrent_states):
    logger.info(f'drive location : {location}')
    logger.info(f'drive agent_attributes : {agent_attributes}')
    logger.info(f'drive agent_states : {agent_states}')
    logger.info(f'drive recurrent_states : {recurrent_states}')
    try:
        response = iai.drive(
            location=location,
            agent_attributes=agent_attributes,
            agent_states=agent_states,
            recurrent_states=recurrent_states,
        )

        assert isinstance(response, iai.api.DriveResponse)

    except Exception as e:
        logger.error(f"Exception : {e}")
        return Drive_Crash

    return Drive_OK
    

@pytest.mark.TEST00001
@pytest.mark.TEST00002
@pytest.mark.parametrize(
    "dstring, location, agent_states, agent_attributes, recurrent_states, expected_result",    
    [
        (
            "TEST00001 : Verify valid location",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00002 : Verify crash: invalid location",
            "canada:vancouver:drake_street_and_pacific_bl",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_Crash,
        ),
    ],
)
def test_location(
    suite_setupteardown,
    dstring,
    location,
    agent_states,
    agent_attributes,
    recurrent_states,
    expected_result,
):
    test_location.__doc__ = dstring
    actual_result = verify_drive(location, agent_states, agent_attributes, recurrent_states)
    assert actual_result == expected_result

@pytest.mark.TEST00003
@pytest.mark.TEST00004
@pytest.mark.TEST00005
@pytest.mark.parametrize(
    "dstring, location, agent_states, agent_attributes, recurrent_states, expected_result",    
    [
        (
            "TEST00003 : Verify multiple AgentState: 2",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-38.0, y=-24.35), orientation=0.42, speed=10.09), AgentState(center=Point(x=17.64, y=11.37), orientation=-2.72, speed=0.74)],
            [AgentAttributes(length=4.94, width=2.02, rear_axis_offset=1.58), AgentAttributes(length=4.98, width=2.0, rear_axis_offset=1.6)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -37.99811935424805, -24.3450870513916, 0.4192616939544678, 10.090646743774414]), RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 17.641992568969727, 11.373613357543945, -2.7238662242889404, 0.7427858710289001])],
            Drive_OK,
        ),
        (
            "TEST00004 : Verify crash: empty AgentState, AgentAttributes not empty",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_Crash,
        ),
        (
            "TEST00005 : Verify crash: empty AgentState and empty AgentAttributes",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [],
            [],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_Crash,
        ),
    ],
)
def test_agentstate(
    suite_setupteardown,
    dstring,
    location,
    agent_states,
    agent_attributes,
    recurrent_states,
    expected_result,
):
    test_agentstate.__doc__ = dstring
    actual_result = verify_drive(location, agent_states, agent_attributes, recurrent_states)
    assert actual_result == expected_result



@pytest.mark.TEST00006
@pytest.mark.TEST00007
@pytest.mark.parametrize(
    "dstring, location, agent_states, agent_attributes, recurrent_states, expected_result",    
    [
        (
            "TEST00006 : Verify crash: RecurrentState: empty",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [],
            Drive_Crash,
        ),
        (
            "TEST00007 : Verify crash: AgentState: empty, AgentAttributes: empty, RecurrentState: empty",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [],
            [],
            [],
            Drive_Crash,
        ),
    ],
)
def test_RecurrentState(
    suite_setupteardown,
    dstring,
    location,
    agent_states,
    agent_attributes,
    recurrent_states,
    expected_result,
):
    test_RecurrentState.__doc__ = dstring
    actual_result = verify_drive(location, agent_states, agent_attributes, recurrent_states)
    assert actual_result == expected_result


@pytest.mark.TEST99999
@pytest.mark.parametrize(
    "dstring",
    [
        (
            "TEST99999 : Verify sample data work",
        ),
    ],
)
def test_login_sample(
    suite_setupteardown,
    dstring,
):
    test_login_sample.__doc__ = dstring
    location = "canada:vancouver:drake_street_and_pacific_blvd"  # select one of available locations

    location_info_response = iai.location_info(location=location)

    # get traffic light states
    light_response = iai.light(location=location)

    # initialize the simulation by spawning NPCs
    response = iai.initialize(
        location=location,  # select one of available locations
        agent_count=2,    # number of NPCs to spawn
        get_birdview=True,  # provides simple visualization - don't use in production
        traffic_light_state_history=[light_response.traffic_lights_states],  # provide traffic light states
    )
    agent_attributes = response.agent_attributes  # get dimension and other attributes of NPCs

    # images = [response.birdview.decode()]  # images storing visualizations of subsequent states
    # for _ in range(1):  # how many simulation steps to execute (10 steps is 1 second)

        # get next traffic light state
    light_response = iai.light(location=location, recurrent_states=light_response.recurrent_states)

        # query the API for subsequent NPC predictions
    logger.info(f'drive location : {location}')
    logger.info(f'drive agent_attributes : {agent_attributes}')
    logger.info(f'drive agent_states : {response.agent_states}')
    logger.info(f'drive recurrent_states : {response.recurrent_states}')
    logger.info(f'drive get_birdview : True')
    logger.info(f'drive traffic_lights_states : {light_response.traffic_lights_states}')
        
    response = iai.drive(
        location=location,
        agent_attributes=agent_attributes,
        agent_states=response.agent_states,
        recurrent_states=response.recurrent_states,
        get_birdview=True,
        traffic_lights_states=light_response.traffic_lights_states,
    )

    assert isinstance(response, iai.api.DriveResponse)

