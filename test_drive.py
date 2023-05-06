# import student

import pytest
import logging
import numpy as np
import imageio
from typing import NamedTuple

import invertedai as iai
# from invertedai.api.drive import DriveResponse
from invertedai.common import AgentState, RecurrentState, AgentAttributes, Point, TrafficLightState
# from invertedai.api import TrafficLightState


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

    except Exception as e:
        logger.error(f"Exception : {e}")
        return Drive_Crash

    logger.info(f'drive return response')
    assert isinstance(response, iai.api.DriveResponse)
    assert len(response.agent_states) == len(agent_states)
    assert len(response.recurrent_states) == len(recurrent_states)
    
    return Drive_OK
    

@pytest.mark.TEST00001
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

@pytest.mark.TEST00002
@pytest.mark.parametrize(
    "dstring, location, agent_states, agent_attributes, recurrent_states, expected_result",    
    [
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
def test_invalid_location(
    suite_setupteardown,
    dstring,
    location,
    agent_states,
    agent_attributes,
    recurrent_states,
    expected_result,
):
    test_invalid_location.__doc__ = dstring
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


@pytest.mark.TEST00101
@pytest.mark.parametrize(
    "dstring, location, agent_states, agent_attributes, recurrent_states, expected_result",    
    [
        (
            "TEST00101 : Verify crash: agent invalid format",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [{'x': 0, 'y': 0, 'orientation': 0, 'speed': 5}],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_Crash,
        ),
    ],
)
def test_AgentState_invalid(
    suite_setupteardown,
    dstring,
    location,
    agent_states,
    agent_attributes,
    recurrent_states,
    expected_result,
):
    test_AgentState_invalid.__doc__ = dstring
    actual_result = verify_drive(location, agent_states, agent_attributes, recurrent_states)
    assert actual_result == expected_result

@pytest.mark.TEST00111
@pytest.mark.TEST00112
@pytest.mark.TEST00113
@pytest.mark.parametrize(
    "dstring, location, agent_states, agent_attributes, recurrent_states, expected_result",    
    [
        (
            "TEST00111 : Verify crash: AgentAttributes invalid format: rear_axis_offset",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [{'length': 4, 'width': 2, 'rear_axis_offset': 'ab'}],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_Crash,
        ),
        (
            "TEST00112 : Verify crash: AgentAttributes invalid format: width",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [{'length': 4, 'width': 'ab', 'rear_axis_offset': 10}],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_Crash,
        ),
        (
            "TEST00113 : Verify crash: AgentAttributes invalid format: length",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [{'length': 'ab', 'width': 10, 'rear_axis_offset': 10}],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_Crash,
        ),
    ],
)
def test_AgentAttributes_invalid(
    suite_setupteardown,
    dstring,
    location,
    agent_states,
    agent_attributes,
    recurrent_states,
    expected_result,
):
    test_AgentAttributes_invalid.__doc__ = dstring
    actual_result = verify_drive(location, agent_states, agent_attributes, recurrent_states)
    assert actual_result == expected_result


@pytest.mark.TEST00201
@pytest.mark.TEST00202
@pytest.mark.TEST00203
@pytest.mark.TEST00204
@pytest.mark.TEST00205
@pytest.mark.parametrize(
    "dstring, location, agent_states, agent_attributes, recurrent_states, expected_result",    
    [
        (
            "TEST00201 : Verify valid speed",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=10)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00202 : Verify large speed",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=99999999999999999999999)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00203 : Verify speed 0",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00204 : Verify speed negative",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=-0.02)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00205 : Verify speed negative large",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=-999999999999999)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
    ],
)
def test_speed(
    suite_setupteardown,
    dstring,
    location,
    agent_states,
    agent_attributes,
    recurrent_states,
    expected_result,
):
    test_speed.__doc__ = dstring
    actual_result = verify_drive(location, agent_states, agent_attributes, recurrent_states)
    assert actual_result == expected_result

@pytest.mark.TEST00211
@pytest.mark.TEST00212
@pytest.mark.TEST00213
@pytest.mark.parametrize(
    "dstring, location, agent_states, agent_attributes, recurrent_states, expected_result",    
    [
        (
            "TEST00211 : Verify orientation 0",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0, speed=0.02)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00212 : Verify orientation negative",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=-9999, speed=0.02)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00213 : Verify orientation large",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=999999999999999, speed=0.02)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
    ],
)
def test_orientation(
    suite_setupteardown,
    dstring,
    location,
    agent_states,
    agent_attributes,
    recurrent_states,
    expected_result,
):
    test_orientation.__doc__ = dstring
    actual_result = verify_drive(location, agent_states, agent_attributes, recurrent_states)
    assert actual_result == expected_result


@pytest.mark.TEST00221
@pytest.mark.TEST00222
@pytest.mark.TEST00223
@pytest.mark.parametrize(
    "dstring, location, agent_states, agent_attributes, recurrent_states, expected_result",    
    [
        (
            "TEST00221 : Verify point x 0",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=0, y=-15.48), orientation=0.39, speed=0.02)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00222 : Verify point x 0, y 0",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=0, y=0), orientation=0.39, speed=0.02)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00223 : Verify point x negative large, y large",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-9999999999, y=9999999999999999), orientation=0.39, speed=0.02)],
            [AgentAttributes(length=4.93, width=2.0, rear_axis_offset=1.58)],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
    ],
)
def test_point(
    suite_setupteardown,
    dstring,
    location,
    agent_states,
    agent_attributes,
    recurrent_states,
    expected_result,
):
    test_point.__doc__ = dstring
    actual_result = verify_drive(location, agent_states, agent_attributes, recurrent_states)
    assert actual_result == expected_result


@pytest.mark.TEST00301
@pytest.mark.TEST00302
@pytest.mark.TEST00303
@pytest.mark.parametrize(
    "dstring, location, agent_states, agent_attributes, recurrent_states, expected_result",    
    [
        (
            "TEST00301 : Verify agent_attributes length 0",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [{'length': 0, 'width': 10, 'rear_axis_offset': 10}],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00302 : Verify agent_attributes length negative",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [{'length': -90.8, 'width': 10, 'rear_axis_offset': 10}],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00303 : Verify agent_attributes length large",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [{'length': 9999999999999999, 'width': 10, 'rear_axis_offset': 10}],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
    ],
)
def test_length(
    suite_setupteardown,
    dstring,
    location,
    agent_states,
    agent_attributes,
    recurrent_states,
    expected_result,
):
    test_length.__doc__ = dstring
    actual_result = verify_drive(location, agent_states, agent_attributes, recurrent_states)
    assert actual_result == expected_result

@pytest.mark.TEST00311
@pytest.mark.TEST00312
@pytest.mark.TEST00313
@pytest.mark.parametrize(
    "dstring, location, agent_states, agent_attributes, recurrent_states, expected_result",    
    [
        (
            "TEST00311 : Verify agent_attributes width 0",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [{'length': 0, 'width': 0, 'rear_axis_offset': 10}],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00312 : Verify agent_attributes width negative",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [{'length': -90.8, 'width': -10.01, 'rear_axis_offset': 10}],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00313 : Verify agent_attributes width large",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [{'length': 9999999999999999, 'width': -999999999999, 'rear_axis_offset': 10}],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
    ],
)
def test_width(
    suite_setupteardown,
    dstring,
    location,
    agent_states,
    agent_attributes,
    recurrent_states,
    expected_result,
):
    test_width.__doc__ = dstring
    actual_result = verify_drive(location, agent_states, agent_attributes, recurrent_states)
    assert actual_result == expected_result

@pytest.mark.TEST00321
@pytest.mark.TEST00322
@pytest.mark.TEST00323
@pytest.mark.parametrize(
    "dstring, location, agent_states, agent_attributes, recurrent_states, expected_result",    
    [
        (
            "TEST00321 : Verify agent_attributes rear_axis_offset 0",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [{'length': 10, 'width': 0, 'rear_axis_offset': 0}],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00322 : Verify agent_attributes rear_axis_offset negative",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [{'length': -90.8, 'width': -10.01, 'rear_axis_offset': -10}],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
        (
            "TEST00323 : Verify agent_attributes rear_axis_offset large",
            "canada:vancouver:drake_street_and_pacific_blvd",
            [AgentState(center=Point(x=-11.25, y=-15.48), orientation=0.39, speed=0.02)],
            [{'length': 0.1, 'width': -0.1, 'rear_axis_offset': 999999}],
            [RecurrentState(packed=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -11.248814582824707, -15.482272148132324, 0.3917691707611084, 0.01937323808670044])],
            Drive_OK,
        ),
    ],
)
def test_rear_axis_offset(
    suite_setupteardown,
    dstring,
    location,
    agent_states,
    agent_attributes,
    recurrent_states,
    expected_result,
):
    test_rear_axis_offset.__doc__ = dstring
    actual_result = verify_drive(location, agent_states, agent_attributes, recurrent_states)
    assert actual_result == expected_result


def verify_drive_optional(
    agent_count, 
    traffic_lights_states,get_birdview,
    rendering_center, rendering_fov, get_infractions, random_seed, 
):
    location = "canada:vancouver:drake_street_and_pacific_blvd"  # select one of available locations

    location_info_response = iai.location_info(location=location)

    # get traffic light states
    light_response = iai.light(location=location)

    # initialize the simulation by spawning NPCs
    response = iai.initialize(
        location=location,  # select one of available locations
        agent_count=agent_count,    # number of NPCs to spawn
        get_birdview=True,  # provides simple visualization - don't use in production
        traffic_light_state_history=[light_response.traffic_lights_states],  # provide traffic light states
    )
    agent_attributes = response.agent_attributes  # get dimension and other attributes of NPCs
    agent_states = response.agent_states
    recurrent_states = response.recurrent_states
    # images = [response.birdview.decode()]  # images storing visualizations of subsequent states
    # for _ in range(1):  # how many simulation steps to execute (10 steps is 1 second)

        # get next traffic light state
    # light_response = iai.light(location=location, recurrent_states=light_response.recurrent_states)

        # query the API for subsequent NPC predictions
    logger.info(f'drive location : {location}')
    logger.info(f'drive agent_attributes : {agent_attributes}')
    logger.info(f'drive agent_states : {agent_states}')
    logger.info(f'drive recurrent_states : {recurrent_states}')

    logger.info(f'drive get_birdview : {get_birdview}')
    logger.info(f'drive traffic_lights_states : {traffic_lights_states}')
    logger.info(f'drive rendering_center : {rendering_center}')
    logger.info(f'drive rendering_fov : {rendering_fov}')
    logger.info(f'drive get_infractions : {get_infractions}')
    logger.info(f'drive random_seed : {random_seed}')
            
    try:
        response = iai.drive(
            location=location,
            agent_attributes=agent_attributes,
            agent_states=response.agent_states,
            recurrent_states=response.recurrent_states,
            traffic_lights_states=traffic_lights_states,
            get_birdview=get_birdview,
            rendering_center=rendering_center,
            rendering_fov=rendering_fov,
            get_infractions=get_infractions,
            random_seed=random_seed,
        )
    except Exception as e:
        logger.error(f"Exception : {e}")
        return Drive_Crash    

    logger.info(f'drive return response')
    assert isinstance(response, iai.api.DriveResponse)
    assert len(response.agent_states) == len(agent_states)
    assert len(response.recurrent_states) == len(recurrent_states)
    
    return Drive_OK



@pytest.mark.TEST01001
@pytest.mark.TEST01002
@pytest.mark.TEST01003
@pytest.mark.TEST01004
@pytest.mark.TEST01005
@pytest.mark.TEST01006
@pytest.mark.TEST01007
@pytest.mark.TEST01008
@pytest.mark.parametrize(
    "dstring, agent_count, traffic_lights_states, get_birdview, rendering_center, rendering_fov, get_infractions, random_seed, expected_result",    
    # "dstring, agent_count, get_birdview, expected_result",    
    [
        (
            "TEST01001 : Verify 2 NPCs with traffic none",
            2,
            {103760: TrafficLightState.none, 103761: TrafficLightState.none, 103762: TrafficLightState.none},
            True,
            None,
            None,
            False,
            None,
            Drive_OK,
        ),
        (
            "TEST01002 : Verify 2 NPCs with traffic green",
            2,
            {103760: TrafficLightState.green, 103761: TrafficLightState.green, 103762: TrafficLightState.green},
            True,
            None,
            None,
            False,
            None,
            Drive_OK,
        ),
        (
            "TEST01003 : Verify 2 NPCs with traffic yellow",
            2,
            {103760: TrafficLightState.yellow, 103761: TrafficLightState.yellow, 103762: TrafficLightState.yellow},
            True,
            None,
            None,
            False,
            None,
            Drive_OK,
        ),
        (
            "TEST01004 : Verify 2 NPCs with traffic red",
            2,
            {103760: TrafficLightState.red, 103761: TrafficLightState.red, 103762: TrafficLightState.red},
            True,
            None,
            None,
            False,
            None,
            Drive_OK,
        ),
        (
            "TEST01005 : Verify 2 NPCs with traffic empty",
            2,
            {},
            True,
            None,
            None,
            False,
            None,
            Drive_OK,
        ),
        (
            "TEST01006 : Verify 2 NPCs with traffic yellow switch to red",
            2,
            {103760: TrafficLightState.yellow, 103761: TrafficLightState.red, 103762: TrafficLightState.red},
            True,
            None,
            None,
            False,
            None,
            Drive_OK,
        ),
        (
            "TEST01007 : Verify crash: 2 NPCs with traffic invalid id",
            2,
            {1: TrafficLightState.red, 103761: TrafficLightState.red, 103762: TrafficLightState.red},
            True,
            None,
            None,
            False,
            None,
            Drive_Crash,
        ),
        (
            "TEST01008 : Verify crash: 2 NPCs with traffic invalid format",
            2,
            {103760: 'y'},
            True,
            None,
            None,
            False,
            None,
            Drive_Crash,
        ),
    ],
)
def test_traffic_light(
    suite_setupteardown,
    dstring,
    agent_count, 
    traffic_lights_states,get_birdview,
    rendering_center, rendering_fov, get_infractions, random_seed, 
    expected_result,
):
    test_traffic_light.__doc__ = dstring
    actual_result = verify_drive_optional(
    agent_count, 
    traffic_lights_states,get_birdview,
    rendering_center, rendering_fov, get_infractions, random_seed)
    assert actual_result == expected_result


@pytest.mark.TEST01101
@pytest.mark.TEST01102
@pytest.mark.parametrize(
    "dstring, agent_count, traffic_lights_states, get_birdview, rendering_center, rendering_fov, get_infractions, random_seed, expected_result",    
    # "dstring, agent_count, get_birdview, expected_result",    
    [
        (
            "TEST01101 : Verify 2 NPCs with get_birdview False",
            2,
            {103760: TrafficLightState.none, 103761: TrafficLightState.none, 103762: TrafficLightState.none},
            True,
            None,
            None,
            False,
            None,
            Drive_OK,
        ),
        (
            "TEST01102 : Verify 2 NPCs with get_birdview True",
            2,
            {103760: TrafficLightState.none, 103761: TrafficLightState.none, 103762: TrafficLightState.none},
            True,
            None,
            None,
            False,
            None,
            Drive_OK,
        ),
    ],
)
def test_get_birdview(
    suite_setupteardown,
    dstring,
    agent_count, 
    traffic_lights_states,get_birdview,
    rendering_center, rendering_fov, get_infractions, random_seed, 
    expected_result,
):
    test_get_birdview.__doc__ = dstring
    actual_result = verify_drive_optional(
    agent_count, 
    traffic_lights_states,get_birdview,
    rendering_center, rendering_fov, get_infractions, random_seed)
    assert actual_result == expected_result

@pytest.mark.TEST01201
@pytest.mark.TEST01202
@pytest.mark.parametrize(
    "dstring, agent_count, traffic_lights_states, get_birdview, rendering_center, rendering_fov, get_infractions, random_seed, expected_result",    
    # "dstring, agent_count, get_birdview, expected_result",    
    [
        (
            "TEST01201 : Verify 2 NPCs with get_infractions False",
            2,
            {103760: TrafficLightState.none, 103761: TrafficLightState.none, 103762: TrafficLightState.none},
            True,
            None,
            None,
            False,
            None,
            Drive_OK,
        ),
        (
            "TEST01202 : Verify 2 NPCs with get_infractions True",
            2,
            {103760: TrafficLightState.none, 103761: TrafficLightState.none, 103762: TrafficLightState.none},
            True,
            None,
            None,
            True,
            None,
            Drive_OK,
        ),
    ],
)
def test_get_infractions(
    suite_setupteardown,
    dstring,
    agent_count, 
    traffic_lights_states,get_birdview,
    rendering_center, rendering_fov, get_infractions, random_seed, 
    expected_result,
):
    test_get_infractions.__doc__ = dstring
    actual_result = verify_drive_optional(
    agent_count, 
    traffic_lights_states,get_birdview,
    rendering_center, rendering_fov, get_infractions, random_seed)
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

