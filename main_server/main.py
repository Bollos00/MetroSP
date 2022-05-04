from cypher.cypher_helper import CypherHelper
from credentials import credentials
from driver.metrodatabasedriver import MetroDatabaseDriver


def init_driver():
    uri = credentials.NEO4J_URI
    user = credentials.NEO4J_USER
    password = credentials.NEO4J_PASSWORD

    return MetroDatabaseDriver(uri, user, password)


if __name__ == "__main__":

    driver = init_driver()

    helper = CypherHelper(60)
    
    # driver.reset(helper)

    print(driver.update_tr_time(helper, l=2, v=1, n=1, time=39))
    print(driver.update_ft_transf_time(helper, "Ana Rosa", fl=1, fv=1, tl=2, tv=2, time=40))
    print(driver.update_ft_plat_bd_time(helper, "Ana Rosa", tl=2, tv=2, time=40))
    print(driver.update_ft_bd_plat_time(helper, "Ana Rosa", fl=1, fv=1, time=40))

    driver.close()