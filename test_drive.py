# import student

import pytest
import logging
import numpy as np
import imageio
from typing import NamedTuple

import invertedai as iai

# from libs.login_page import *

logger = logging.getLogger("drive test")


class StatusCode(NamedTuple):
    code: int
    description: str
    
LOGIN_SUCCESS = StatusCode(1, 'login successfully')


def verify_login(suite_setupteardown, eachtest_setupteardown, usernm, passwd, err_msg):
    location = "canada:vancouver:drake_street_and_pacific_blvd"  # select one of available locations

    #API key:
    # iai.add_apikey("mZHY4zRJkJ557Aut85Q8T2pSFELU05Tn7LMrqxgu")

    # get static information about a given location including map in osm
    # format and list traffic lights with their IDs and locations.
    location_info_response = iai.location_info(location=location)

    # get traffic light states
    light_response = iai.light(location=location)

    # initialize the simulation by spawning NPCs
    response = iai.initialize(
        location=location,  # select one of available locations
        agent_count=10,    # number of NPCs to spawn
        get_birdview=True,  # provides simple visualization - don't use in production
        traffic_light_state_history=[light_response.traffic_lights_states],  # provide traffic light states
    )
    agent_attributes = response.agent_attributes  # get dimension and other attributes of NPCs

    # images = [response.birdview.decode()]  # images storing visualizations of subsequent states
    for _ in range(1):  # how many simulation steps to execute (10 steps is 1 second)

        # get next traffic light state
        light_response = iai.light(location=location, recurrent_states=light_response.recurrent_states)

        # query the API for subsequent NPC predictions
        response = iai.drive(
            location=location,
            agent_attributes=agent_attributes,
            agent_states=response.agent_states,
            recurrent_states=response.recurrent_states,
            get_birdview=True,
            traffic_lights_states=light_response.traffic_lights_states,
        )

        logger.info(f'response : {response}')

        # save the visualization - requires np and cv2
        # images.append(response.birdview.decode())

    # save the visualization to disk
    # imageio.mimsave("iai-example.gif", np.array(images), format="GIF-PIL")

    return LOGIN_SUCCESS


@pytest.mark.TEST00001
@pytest.mark.parametrize(
    "dstring, usernm, passwd, err_msg, expected_result",
    [
        (
            "TEST00001 : Verify login success : a valid username and password",
            "standard_user",
            "secret_sauce",
            "",
            LOGIN_SUCCESS,
        ),
    ],
)
def test_login_page_success(
    suite_setupteardown,
    eachtest_setupteardown,
    dstring,
    usernm,
    passwd,
    err_msg,
    expected_result,
):
    test_login_page_success.__doc__ = dstring
    actual_result = verify_login(
        suite_setupteardown, eachtest_setupteardown, usernm, passwd, err_msg
    )
    assert actual_result == expected_result


