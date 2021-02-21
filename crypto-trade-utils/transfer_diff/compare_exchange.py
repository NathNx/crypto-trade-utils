

class ExchangeStretegy:

    def __init__(self,
                 src_exc: str,
                 dst_exc: str,
                 from_cur: str,
                 to_cur: str):

        self.from_cur = from_cur
        self.to_cur = to_cur
        self.src_exc = src_exc
        self.dst_exc = dst_exc

    @staticmethod
    def __calculate_diff(fiat_amount: float=1,
                         from_cur_src_exc: float=0,
                         to_cur_dst_exc: float=0,
                         to_cur_src_exc: float=0,
                         from_cur_fee: float=0,
                         to_cur_fee: float=0,
                         ref_cur_dst_exc: float=None,
                         to_cur_spot_ref_cur: float=None) -> dict:
        """
        Calculate conversion cost between specify currencies and exchanges
        :param fiat_amount:
        :param from_cur_src_exc:
        :param to_cur_dst_exc:
        :param to_cur_src_exc:
        :param from_cur_fee:
        :param to_cur_fee:
        :param ref_cur_dst_exc:
        :param to_cur_spot_ref_cur:
        :return:
        """

        from_cur_dst_exc_amount = fiat_amount / from_cur_src_exc
        from_cur_dst_exc_trans_amount = from_cur_dst_exc_amount - from_cur_fee

        if ref_cur_dst_exc is None:
            print("No reference spot has been assigned.")
            to_dst_cost = from_cur_dst_exc_trans_amount / to_cur_dst_exc
        else:
            print("Reference spot has been assigned.")
            to_dst_cost = (from_cur_dst_exc_trans_amount / ref_cur_dst_exc) / to_cur_spot_ref_cur

        stay_src_cost = (fiat_amount / to_cur_src_exc) - to_cur_fee

        if to_dst_cost > stay_src_cost:
            print("a")
        elif stay_src_cost < to_dst_cost:
            print("b")
        elif stay_src_cost == to_dst_cost:
            print("c")
        else:
            raise ValueError("Comparison cannot be done.")

        return {"fiat_amount": fiat_amount,
                "reference_spot": -1 if to_cur_spot_ref_cur is None else to_cur_spot_ref_cur,
                "transfer_cost": to_dst_cost,
                "no_transfer_cost": stay_src_cost}

    def compare(self,
                fiat_amount: float) -> dict:

        #...  # to be implement price fetching process.

        output = self.__calculate_diff(fiat_amount)  # get strategy

        return output