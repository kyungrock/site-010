#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""신규 20편 추가 (카테고리 중복 없음)"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_PATH = ROOT / "data" / "blog-posts.json"

# 공통 푸터 링크 패턴
GUNMA = '<a href="https://gunmacity.com/" target="_blank" rel="noopener noreferrer">마사지</a>'

NEW_POSTS = [
    {
        "id": "pilates-yoga-pre-massage-shower",
        "title": "필라테스·요가 수업 후 마사지, 전 샤워로 근섬유 이완 준비하기",
        "summary": "유연성 운동 직후 땀과 매트 먼지가 남은 채 마사지를 받으면 효과가 떨어집니다. 필라테스·요가 후 전 샤워 포인트를 정리했습니다.",
        "category": "필라테스·요가",
        "date": "2026-07-22",
        "tags": ["필라테스", "요가", "마사지전샤워", "웰니스"],
        "content": f"""<p>매트 위에서 50분을 보낸 뒤 마사지 예약이 이어지는 날, 몸은 부드러워진 것 같지만 피부에는 땀·먼지·매트 잔여물이 남아 있습니다. <strong>마사지 전 샤워</strong>는 유연성 운동 후 회복 루틴의 첫 관문입니다.</p>
<h2>요가·필라테스 후 왜 씻어야 하나</h2>
<p>매트 접촉 부위(등·팔·종아리)에 땀과 각질이 남으면 오일 마사지 흡수가 떨어지고, 관리대 위생에도 영향을 줍니다. 가벼운 스트레칭으로 풀린 근육은 미지근한 물로 이완을 유지하는 편이 좋아요.</p>
<h2>추천 루틴 (약 7분)</h2>
<ul><li>37℃ 전후 미지근한 물 2분</li><li>등·팔·종아리 순한 세정</li><li>수건 눌러 말리기 — 문지르지 않기</li><li>관리 10분 전 물 반 잔</li></ul>
<div class="tip-box"><strong>팁</strong><p>핫요가 직후에는 5분 안정 후 샤워하세요. 심박이 높을 때 바로 뜨거운 물은 어지러움을 부를 수 있습니다.</p></div>
<p>운동 후 기본은 <a href="../posts/exercise-shower-massage-routine.html">운동 후 전 샤워 루틴</a>, 전국 정보는 {GUNMA}·웰니스 허브에서 확인하세요.</p>
<h2>마무리</h2>
<p>필라테스·요가 날의 <strong>마사지 전 샤워</strong>는 매트에서 관리실로 넘어가는 <strong>청결 다리</strong>입니다.</p>""",
    },
    {
        "id": "hiking-trekking-pre-massage-shower",
        "title": "등산·트레킹 후 마사지 전 샤워, 먼지·땀 제거 가이드",
        "summary": "산에서 내려온 뒤 등·종아리·발에 남은 먼지와 땀을 씻지 않으면 마사지 효과와 위생 모두 손해입니다.",
        "category": "등산·트레킹",
        "date": "2026-07-21",
        "tags": ["등산", "트레킹", "마사지전샤워", "회복"],
        "content": f"""<p>주말 등산 후 저녁 마사지 예약은 흔한 패턴입니다. 그런데 등·다리·발에 흙먼지와 땀이 남은 채 관리실에 누우면 <strong>마사지 전 샤워</strong>를 건너뛴 셈이 됩니다.</p>
<h2>등산 후 피부·근육 상태</h2>
<p>장시간 하행으로 종아리·허벅지·발이 뭉치고, 땀과 미세먼지가 옷 안에 남습니다. 오일과 섞이면 모공이 막히기 쉽습니다.</p>
<h2>세정 순서</h2>
<ol><li>발·종아리 먼저 — 등산화·양말 자국</li><li>등·어깨 — 배낭 땀</li><li>팔·손 — 스틱·장갑 접촉면</li><li>미지근한 물로 마무리</li></ol>
<p>러닝·야외 운동 글 <a href="../blog/running-post-workout-pre-massage-shower.html">러닝 후 전 샤워</a>와 함께 보시면 종목별 차이가 보입니다.</p>
<h2>마무리</h2>
<p>등산 날 <strong>마사지 전 샤워</strong>는 산에서 도시로 몸을 <strong>리셋</strong>하는 과정입니다.</p>""",
    },
    {
        "id": "cycling-pre-massage-shower-guide",
        "title": "자전거·사이클 라이딩 후, 마사지 전 샤워 체크리스트",
        "summary": "라이딩 후 허벅지·엉덩이·손의 땀과 로션 잔여물을 씻어야 마사지 압이 잘 들어갑니다.",
        "category": "자전거·사이클",
        "date": "2026-07-20",
        "tags": ["사이클", "자전거", "마사지전샤워", "스포츠"],
        "content": f"""<p>40km 라이딩 후 마사지를 예약했다면, 허벅지·엉덩이·손바닥에 땀과 선크림·바람막이 잔여물이 남아 있을 수 있습니다. <strong>마사지 전 샤워</strong>는 사이클 회복의 필수 단계입니다.</p>
<h2>라이딩 후 집중 부위</h2>
<ul><li><strong>허벅지·엉덩이</strong> — 안장 마찰</li><li><strong>종아리·발</strong> — 페달 반복</li><li><strong>손·팔</strong> — 그립·햇볕</li><li><strong>등</strong> — 저지 땀</li></ul>
<h2>온도·시간</h2>
<p>36~38℃, 7~10분. 찬물만으로 급히 식히면 근육이 다시 굳을 수 있어요.</p>
<div class="tip-box"><strong>팁</strong><p>샤워 후 5분 스트레칭과 수분 섭취를 함께 하면 관리 효과가 커집니다.</p></div>
<p>{GUNMA}·웰니스 정보도 함께 참고해 보세요.</p>
<h2>마무리</h2>
<p>사이클 날 <strong>마사지 전 샤워</strong>는 페달을 멈춘 뒤 <strong>몸을 풀기 전</strong> 꼭 필요합니다.</p>""",
    },
    {
        "id": "after-drinking-pre-massage-shower",
        "title": "회식·음주 다음 날 마사지, 전 샤워로 몸 깨우기 vs 쉬기",
        "summary": "술 마신 다음 날 마사지를 받을 계획이라면 전 샤워와 수분·온도를 어떻게 잡을지 먼저 정해야 합니다.",
        "category": "회식·음주 후",
        "date": "2026-07-19",
        "tags": ["회식", "숙취", "마사지전샤워", "힐링"],
        "content": f"""<p>회식 다음 날 오후에 마사지를 잡아 두었다면, 몸은 무겁고 피부에는 전날 땀·향수·음식 냄새가 남아 있을 수 있습니다. <strong>마사지 전 샤워</strong>는 숙취 날에도 청결과 각성 조절에 도움이 됩니다.</p>
<div class="warn-box"><strong>주의</strong><p>심한 구토·어지러움·탈수가 있으면 마사지를 미루고 의료 상담을 우선하세요. 전 샤워는 컨디션이 회복된 경우에만.</p></div>
<h2>가능할 때의 전 샤워</h2>
<ul><li>미지근한 물 5~7분 — 뜨거운 물은 피하기</li><li>순한 바디워시로 땀·냄새 제거</li><li>샤워 전후 물·전해질</li><li>강한 향수·데오드란트는 생략</li></ul>
<p>수분 관련은 <a href="../blog/hydration-before-massage-and-shower.html">수분과 전 샤워 글</a>을 참고하세요.</p>
<h2>마무리</h2>
<p>음주 다음 날 <strong>마사지 전 샤워</strong>는 무리한 각성이 아니라 <strong>몸을 정돈</strong>하는 정도로만.</p>""",
    },
    {
        "id": "long-flight-pre-massage-shower",
        "title": "장거리 비행 후 마사지, 공항·호텔에서 하는 전 샤워 팁",
        "summary": "비행 후 붓기·뻣뻣함으로 마사지를 받는다면 전 샤워로 순환과 청결을 먼저 챙기세요.",
        "category": "장거리·항공여행",
        "date": "2026-07-18",
        "tags": ["비행", "여행", "마사지전샤워", "회복"],
        "content": f"""<p>10시간 비행 후 도착지에서 마사지를 예약하는 경우가 많습니다. 다리가 붓고 피부는 건조한데, <strong>마사지 전 샤워</strong> 없이 관리실에 가면 위생·효과 모두 아쉬울 수 있어요.</p>
<h2>비행 후 몸의 변화</h2>
<p>저압·장시간 착석으로 다리 부종, 건조한 피부, 머리카락·옷에 남은 공항·기내 먼지. 미지근한 샤워는 표면을 정돈하고 근육 긴장을 낮춥니다.</p>
<h2>호텔·공항 샤워 팁</h2>
<ol><li>미지근한 물 5~8분</li><li>다리·발 집중 — 붓기 완화에 도움</li><li>보습은 가볍게</li><li>샤워 후 10분 앉아 안정</li></ol>
<p>출장 루틴은 <a href="../blog/business-trip-hotel-shower-massage.html">출장지 호텔 샤워 글</a>과 연결됩니다.</p>
<h2>마무리</h2>
<p>장거리 비행 후 <strong>마사지 전 샤워</strong>는 <strong>착륙 후 첫 리셋</strong>입니다.</p>""",
    },
    {
        "id": "jjimjilbang-sauna-before-massage",
        "title": "찜질방·사우나 후 마사지, 전 샤워 순서 이렇게 잡으세요",
        "summary": "찜질방에서 마사지까지 이어질 때 땀·염분·때를 씻는 타이밍을 잘못 잡으면 피로만 쌓입니다.",
        "category": "찜질방·사우나",
        "date": "2026-07-17",
        "tags": ["찜질방", "사우나", "마사지전샤워", "힐링"],
        "content": f"""<p>찜질방에 가면 사우나 → 식사 → 마사지 순서가 흔합니다. 그런데 땀을 충분히 씻지 않고 관리실로 가면 <strong>마사지 전 샤워</strong>가 형식적으로 끝난 셈이 됩니다.</p>
<h2>추천 순서</h2>
<ol><li>사우나 15~20분 이내</li><li>미지근한 <strong>전 샤워</strong>로 땀·염분 헹구기</li><li>5~10분 휴식·수분</li><li>마사지 시작</li></ol>
<h2>피할 것</h2>
<p>고온 사우나 직후 바로 딥티슈, 찬물 확 샤워 후 즉시 눕기 — 어지러움 위험이 있습니다.</p>
<p>스파 순서는 <a href="../blog/resort-spa-shower-order.html">리조트 스파 글</a>도 참고하세요.</p>
<h2>마무리</h2>
<p>찜질방에서 <strong>마사지 전 샤워</strong>는 땀을 <strong>남기지 않는</strong> 짧은 정돈입니다.</p>""",
    },
    {
        "id": "wedding-event-pre-massage-shower",
        "title": "웨딩·행사 전날 마사지, 전 샤워와 스타일링 타이밍",
        "summary": "중요한 날 전날 마사지를 받을 때 전 샤워·헤어·메이크업 순서를 어떻게 잡을지 정리했습니다.",
        "category": "웨딩·특별일",
        "date": "2026-07-16",
        "tags": ["웨딩", "행사", "마사지전샤워", "셀프케어"],
        "content": f"""<p>결혼식·돌잔·중요 발표 전날 마사지는 긴장을 풀어 주지만, <strong>마사지 전 샤워</strong>와 스타일링 순서를 잘못 잡으면 다음 날 메이크업·헤어가 꼬일 수 있습니다.</p>
<h2>전날 마사지 전 샤워</h2>
<ul><li>미지근한 물 7~10분 — 등·어깨·발</li><li>두피는 가볍게, 스타일링 제품 최소화</li><li>오일 마사지 후 샤워는 다음 날 아침(오일 흡수 시간 고려)</li></ul>
<div class="tip-box"><strong>팁</strong><p>오일 향이 강하면 다음 날 향수와 겹칩니다. 무향·약향 오일을 요청하세요.</p></div>
<p>메이크업 관련은 <a href="../blog/makeup-cleansing-before-massage.html">메이크업 클렌징 글</a>을 함께 보세요.</p>
<h2>마무리</h2>
<p>특별한 날 전 <strong>마사지 전 샤워</strong>는 <strong>내일을 위한 준비</strong>입니다.</p>""",
    },
    {
        "id": "exam-student-pre-massage-shower",
        "title": "수험생·시험 기간, 마사지 전 샤워로 집중력 회복하기",
        "summary": "장시간 책상에 앉은 수험생도 전 샤워로 긴장을 풀면 마사지 효과가 달라집니다. 학생·부모를 위한 가이드입니다.",
        "category": "수험생·집중피로",
        "date": "2026-07-15",
        "tags": ["수험생", "시험", "마사지전샤워", "힐링"],
        "content": f"""<p>수능·자격증 시험 전, 목·어깨·허리가 뻣뻣한 학생에게 마사지를 선물하는 가정이 많습니다. <strong>마사지 전 샤워</strong>는 학생도 거의 필수입니다.</p>
<h2>학생에게 필요한 이유</h2>
<p>장시간 앉아 공부하면 땀·피지·머리카락·책상 먼지가 피부에 남습니다. 청결·예절·관리 효과 모두를 위해 짧게라도 씻는 편이 좋아요.</p>
<h2>안전한 루틴</h2>
<ul><li>37℃ 전후 5~7분</li><li>목·어깨·등 가볍게</li><li>샤워 후 10분 휴식 후 이동</li><li>카페인·에너지드rink 과다는 피하기</li></ul>
<p>사무실·VDT 관련은 <a href="../blog/after-work-massage-shower-timeline.html">퇴근 후 타임라인</a>과도 연결됩니다.</p>
<h2>마무리</h2>
<p>시험 시즌 <strong>마사지 전 샤워</strong>는 공부를 잠깐 멈추고 <strong>몸을 돌보는 신호</strong>입니다.</p>""",
    },
    {
        "id": "desk-vdt-neck-pre-shower",
        "title": "하루 종일 모니터 앞, 마사지 전 샤워로 목·어깨 풀기",
        "summary": "VDT 증후군으로 목·어깨 마사지를 받는다면 전 샤워로 근육과 피부를 함께 준비하세요.",
        "category": "사무실·VDT",
        "date": "2026-07-14",
        "tags": ["VDT", "목어깨", "마사지전샤워", "직장인"],
        "content": f"""<p>8시간 모니터 앞에 앉은 뒤 저녁 마사지 — 목·어깨만 풀면 될 것 같지만, 등과 두피에도 땀과 피로가 쌓여 있습니다. <strong>마사지 전 샤워</strong>는 VDT 직장인에게 특히 등·목 라인 세정이 중요합니다.</p>
<h2>집중 부위</h2>
<ul><li>목덜미·어깨</li><li>등 상부 — 셔츠 땀</li><li>두피 — 유분·스타일링</li><li>손·손목 — 키보드·마우스</li></ul>
<h2>온도</h2>
<p>미지근한 물로 5~8분. 너무 뜨거우면 어지러울 수 있습니다.</p>
<p>스트레스 날은 <a href="../blog/stress-relief-pre-shower-routine.html">스트레스 전 샤워 글</a>도 참고하세요. {GUNMA} 정보도 활용해 보세요.</p>
<h2>마무리</h2>
<p>모니터 앞 하루를 마무리하는 <strong>마사지 전 샤워</strong>는 <strong>목·등 5분</strong>만으로도 충분합니다.</p>""",
    },
    {
        "id": "climbing-bouldering-pre-shower",
        "title": "클라이밍·볼더링 후 마사지, 전 샤워로 손·전완 케어",
        "summary": "암벽·볼더링 후 초크·땀·굳은살이 남은 손과 팔을 씻고 마사지를 받아야 효과가 납니다.",
        "category": "클라이밍·암벽",
        "date": "2026-07-13",
        "tags": ["클라이밍", "볼더링", "마사지전샤워", "스포츠"],
        "content": f"""<p>클라이밍 직후 손바닥·전완·어깨가 뭉친 상태에서 마사지를 예약했다면, 초크 가루와 땀이 그대로 남아 있을 수 있습니다. <strong>마사지 전 샤워</strong>에서 손·팔 세정을 빼먹지 마세요.</p>
<h2>세정 포인트</h2>
<ol><li>손·손가락 — 초크·굳은살 주변 부드럽게</li><li>전완·어깨 — 그립 긴장</li><li>등 — 하네스·땀</li></ol>
<div class="tip-box"><strong>팁</strong><p>굳은살을 샤워에서 거칠게 깎지 마세요. 출혈·통증 시 관리사에게 알리세요.</p></div>
<p>등산·야외 글 <a href="../blog/hiking-trekking-pre-massage-shower.html">등산 후 전 샤워</a>와 비교해 보세요.</p>
<h2>마무리</h2>
<p>클라이밍 날 <strong>마사지 전 샤워</strong>는 <strong>손부터</strong> 시작합니다.</p>""",
    },
    {
        "id": "ski-winter-sports-pre-shower",
        "title": "스키·보드 후 마사지, 전 샤워로 근육 냉각·이완 준비",
        "summary": "겨울 스포츠 후 땀과 장비 냄새를 씻지 않으면 마사지실에서 불편할 수 있습니다. 스키·보드 후 전 샤워 가이드입니다.",
        "category": "스키·겨울스포츠",
        "date": "2026-07-12",
        "tags": ["스키", "보드", "마사지전샤워", "겨울"],
        "content": f"""<p>스키장에서 하루를 보낸 뒤 리조트 마사지를 받는 경우, 장갑·부츠 안 땀과 장비 냄새가 남기 쉽습니다. <strong>마사지 전 샤워</strong>는 겨울 스포츠 후 필수입니다.</p>
<h2>겨울에도 땀이 납니다</h2>
<p>추워 보여도 활동량이 크면 등·다리·발에 땀이 많습니다. 미지근한 물로 8~10분 세정하세요.</p>
<h2>보습 주의</h2>
<p>겨울 건조 피부는 <a href="../blog/winter-dry-skin-pre-shower-prep.html">겨울 보습 전 샤워</a> 글과 함께 보세요. 오일 마사지 전 두꺼운 로션은 피합니다.</p>
<h2>마무리</h2>
<p>스키·보드 날 <strong>마사지 전 샤워</strong>는 <strong>장비를 벗은 뒤</strong> 바로.</p>""",
    },
    {
        "id": "foot-bath-half-bath-pre-massage",
        "title": "반신욕·족욕만 하고 마사지 받아도 될까? 전 샤워와 차이",
        "summary": "족욕·반신욕이 전 샤워를 대체할 수 있는지, 마사지 전에 어떻게 조합하면 좋은지 정리했습니다.",
        "category": "반신욕·족욕",
        "date": "2026-07-11",
        "tags": ["족욕", "반신욕", "마사지전샤워", "힐링"],
        "content": f"""<p>집에서 족욕만 하고 마사지샵에 가는 분들이 있습니다. 족욕은 이완에 좋지만 <strong>마사지 전 샤워</strong>의 청결 기능을 완전히 대체하진 못합니다.</p>
<h2>족욕 vs 전 샤워</h2>
<ul><li><strong>족욕</strong> — 발 이완·혈행, 냄새 일부 완화</li><li><strong>전 샤워</strong> — 전신 땀·먼지·피지 제거</li></ul>
<p>발 마사지만 받는 날에도 발가락 사이·발등 세정은 필요합니다. <a href="../blog/foot-reflexology-pre-shower-clean.html">발 마사지 전 씻기</a> 글을 참고하세요.</p>
<h2>조합 추천</h2>
<p>족욕 10분 → 미지근한 샤워로 발·종아리 헹구기 → 마사지. 뜨거운 족욕 직후 찬물은 피하세요.</p>
<h2>마무리</h2>
<p>족욕은 <strong>보조</strong>, <strong>마사지 전 샤워</strong>는 <strong>기본</strong>으로 기억하세요.</p>""",
    },
    {
        "id": "hand-wrist-typing-pre-shower",
        "title": "손·손목 마사지 전, 타이핑·스마트폰 사용 후 씻는 이유",
        "summary": "손·손목 관리를 받는다면 키보드·폰 사용 후 세정과 보습을 어떻게 할지 정리했습니다.",
        "category": "손·손목·타이핑",
        "date": "2026-07-10",
        "tags": ["손목", "타이핑", "마사지전샤워", "VDT"],
        "content": f"""<p>손·손목 마사지를 예약했다면, 하루 종일 타이핑·스크롤한 손에 땀·손소독제·보습제가 겹쳐 있을 수 있습니다. <strong>마사지 전 샤워</strong>에서 손·손목을 꼭 씻으세요.</p>
<h2>세정 방법</h2>
<ul><li>미지근한 물로 1~2분</li><li>손등·손바닥·손가락 사이</li><li>손목 라인 — 시계·밴드 자국</li><li>알코올 손소독제 잔여물 헹구기</li></ul>
<p>손목 통증과 함께라면 <a href="../blog/back-pain-pre-massage-warmup.html">통증 날 전 샤워</a>도 참고하세요.</p>
<h2>마무리</h2>
<p>손 관리 날 <strong>마사지 전 샤워</strong>는 <strong>손부터</strong>입니다.</p>""",
    },
    {
        "id": "body-odor-underarm-pre-shower",
        "title": "겨드랑이·체취 걱정, 마사지 전 샤워로 자신감 챙기기",
        "summary": "전신·어깨 마사지를 받을 때 겨드랑이·체취 관리는 예절이자 효과를 위한 준비입니다.",
        "category": "겨드랑이·체취",
        "date": "2026-07-09",
        "tags": ["체취", "겨드랑이", "마사지전샤워", "에티켓"],
        "content": f"""<p>어깨·등·팔 마사지를 받을 때 겨드랑이 근처를 관리사가 지나갑니다. <strong>마사지 전 샤워</strong>에서 겨드랑이 세정을 빼먹으면 본인도 관리사도 불편할 수 있어요.</p>
<h2>실전 팁</h2>
<ul><li>미지근한 물로 겨드랑이 30초 이상</li><li>데오드란트는 향 약하게 — 오일과 겹치지 않게</li><li>면 티셔츠 등 땀 흡수 좋은 옷 착용</li></ul>
<p>샵 에티켓은 <a href="../blog/massage-shop-first-visit-shower.html">첫 방문 글</a>도 참고하세요.</p>
<h2>마무리</h2>
<p>체취 걱정은 <strong>마사지 전 샤워 5분</strong>으로 많이 줄일 수 있습니다.</p>""",
    },
    {
        "id": "tattoo-area-pre-massage-shower",
        "title": "타투·문신 부위 근처 마사지, 전 샤워와 피부 보호",
        "summary": "문신 주변 마사지를 받을 때 전 샤워와 오일·압 주의점을 정리했습니다.",
        "category": "타투·문신",
        "date": "2026-07-08",
        "tags": ["타투", "문신", "마사지전샤워", "피부"],
        "content": f"""<p>팔·등·다리 문신 근처를 마사지받을 계획이라면, <strong>마사지 전 샤워</strong>는 감염 예방과 관리사 안내에 모두 필요합니다.</p>
<div class="warn-box"><strong>주의</strong><p>문신 후 2~4주(상처 회복 기간)에는 해당 부위 마사지·강한 샤워 자극을 피하고 의사·타투이스트 지침을 따르세요.</p></div>
<h2>회복 후 전 샤워</h2>
<ul><li>순한 세정제, 문신 위 직접 강한 문지름 금지</li><li>주변 근육은 가볍게 세정</li><li>관리사에게 문신 위치·민감도 알리기</li></ul>
<p>민감 피부는 <a href="../blog/sensitive-skin-pre-massage-shower.html">민감성 피부 글</a>도 함께 보세요.</p>
<h2>마무리</h2>
<p>문신 있는 분의 <strong>마사지 전 샤워</strong>는 <strong>말하기 + 순하게</strong>가 핵심입니다.</p>""",
    },
    {
        "id": "laser-skin-treatment-pre-shower",
        "title": "피부 시술·레이저 후 마사지, 전 샤워 가능 시점",
        "summary": "레이저·필링 등 시술 후 언제부터 마사지와 전 샤워를 해도 되는지 일반적인 주의점을 정리했습니다.",
        "category": "피부시술·레이저",
        "date": "2026-07-07",
        "tags": ["레이저", "피부시술", "마사지전샤워", "피부"],
        "content": f"""<p>피부과 시술 후 몸 전체 마사지를 예약해 두었다면, 시술 부위의 <strong>마사지 전 샤워</strong>와 관리 가능 여부를 담당 의사에게 먼저 확인하세요.</p>
<div class="warn-box"><strong>안내</strong><p>시술 직후·발적·각질 제거 기간에는 해당 부위 마사지·뜨거운 샤워를 피해야 합니다. 이 글은 일반 정보입니다.</p></div>
<h2>의사 OK 후</h2>
<ul><li>미지근한 물, 자극 최소</li><li>시술 부위는 가볍게만</li><li>향·알cohol 성분 세정제 피하기</li></ul>
<p>제품 선택은 <a href="../blog/bodywash-ingredients-avoid.html">바디워시 성분 글</a>을 참고하세요.</p>
<h2>마무리</h2>
<p>시술 후 <strong>마사지 전 샤워</strong>는 <strong>의료 지침 다음</strong>에만.</p>""",
    },
    {
        "id": "camping-outdoor-pre-massage-shower",
        "title": "캠핑·야영 후 마사지, 전 샤워로 먼지·연기·냄새 제거",
        "summary": "캠핑에서 돌아온 뒤 마사지를 받는다면 텐트·모닥불 냄새와 먼지를 씻는 것부터 시작하세요.",
        "category": "캠핑·야영",
        "date": "2026-07-06",
        "tags": ["캠핑", "야영", "마사지전샤워", "아웃도어"],
        "content": f"""<p>주말 캠핑 후 월요일 저녁 마사지 — 옷과 머리에는 불냄새·먼지·땀이 남아 있습니다. <strong>마사지 전 샤워</strong>는 야외 활동 후 필수입니다.</p>
<h2>캠핑 후 세정</h2>
<ul><li>머리·두피 — 연기·먼지</li><li>등·팔 — 텐트·의자 접촉</li><li>발 — 흙·잔디</li></ul>
<p>등산·트레킹 글 <a href="../blog/hiking-trekking-pre-massage-shower.html">등산 후 전 샤워</a>와 유사한 포인트가 많습니다.</p>
<h2>마무리</h2>
<p>캠핑 날 <strong>마사지 전 샤워</strong>는 <strong>자연에서 돌아온 몸</strong>을 정리하는 일입니다.</p>""",
    },
    {
        "id": "volleyball-team-sports-pre-shower",
        "title": "배구·구기종목 경기 후, 마사지 전 샤워 루틴",
        "summary": "팀 스포츠 후 전신 땀과 코트 먼지를 씻고 마사지를 받아야 회복 마사지 효과가 살아납니다.",
        "category": "배구·구기종목",
        "date": "2026-07-05",
        "tags": ["배구", "구기종목", "마사지전샤워", "스포츠"],
        "content": f"""<p>배구·풋살·농구 같은 구기종목 후 마사지 예약이 있다면, 코트·체육관 먼지와 땀이 전신에 남습니다. <strong>마사지 전 샤워</strong>는 팀 스포츠 회복의 기본입니다.</p>
<h2>집중 부위</h2>
<ul><li>종아리·허벅지 — 점프·달리기</li><li>어깨·팔 — 스파이크·패스</li><li>등 — 유니폼 땀</li><li>발 — 실내화·양말</li></ul>
<p>러닝·사이클 글과 함께 보면 종목별 차이를 비교하기 좋습니다.</p>
<h2>마무리</h2>
<p>경기 후 <strong>마사지 전 샤워</strong>는 <strong>샤워실 10분</strong>이면 충분합니다.</p>""",
    },
    {
        "id": "diet-fasting-pre-massage-shower",
        "title": "다이어트·단식 중 마사지, 전 샤워와 어지러움 예방",
        "summary": "식사를 줄이는 기간에 마사지를 받을 때 전 샤워 온도와 수분 섭취를 어떻게 할지 정리했습니다.",
        "category": "다이어트·식이",
        "date": "2026-07-04",
        "tags": ["다이어트", "단식", "마사지전샤워", "웰니스"],
        "content": f"""<p>다이어트·간헐적 단식 중 마사지를 받으면 혈당·수분이 낮아 어지러울 수 있습니다. <strong>마사지 전 샤워</strong>도 뜨겁고 길게 하면 부담이 커질 수 있어요.</p>
<h2>주의</h2>
<ul><li>미지근한 물 5~7분</li><li>샤워 전후 물·전해질</li><li>공복 극단 + 딥티슈는 피하기</li><li>어지러우면 즉시 중단</li></ul>
<p>수분은 <a href="../blog/hydration-before-massage-and-shower.html">수분·전 샤워 글</a>을 참고하세요.</p>
<h2>마무리</h2>
<p>다이어트 중 <strong>마사지 전 샤워</strong>는 <strong>짧고 미지근하게</strong>, 수분과 함께.</p>""",
    },
    {
        "id": "meditation-breath-pre-shower-relax",
        "title": "명상·호흡 전 마사지, 전 샤워로 몸과 마음 연결하기",
        "summary": "마사지를 명상처럼 받고 싶다면 전 샤워를 호흡·이완 루틴과 연결해 보세요.",
        "category": "명상·호흡·이완",
        "date": "2026-07-03",
        "tags": ["명상", "호흡", "마사지전샤워", "힐링"],
        "content": f"""<p>마사지를 &quot;몸 명상&quot;처럼 받고 싶다면, <strong>마사지 전 샤워</strong>부터 호흡을 맞춰 보세요. 미지근한 물과 천천히 내쉬는 숨이 관리 준비가 됩니다.</p>
<h2>3분 호흡 샤워</h2>
<ol><li>미지근한 물 1분</li><li>들숨 4초·날숨 6초 × 5회</li><li>목·어깨에 물 머금기 30초</li><li>수건으로 가볍게 말리기</li></ol>
<p>스트레스 루틴은 <a href="../blog/stress-relief-pre-shower-routine.html">스트레스 전 샤워</a>, 불면은 <a href="../blog/insomnia-pre-massage-shower-sleep.html">수면 글</a>과 연결됩니다.</p>
<p>{GUNMA}·아로마 정보로 분위기를 맞출 수도 있습니다.</p>
<h2>마무리</h2>
<p><strong>마사지 전 샤워</strong>는 몸을 씻는 시간이자 <strong>마음을 비우는</strong> 5분이 될 수 있습니다.</p>""",
    },
]


def main() -> None:
    existing = []
    if POSTS_PATH.is_file():
        existing = json.loads(POSTS_PATH.read_text(encoding="utf-8")).get("posts", [])
    by_id = {p["id"]: p for p in existing}
    cats = {p.get("category") for p in existing}
    added = 0
    for p in NEW_POSTS:
        if "{GUNMA}" in p.get("content", ""):
            p["content"] = p["content"].replace("{GUNMA}", GUNMA)
        if p.get("category") in cats and p["id"] not in by_id:
            print(f"WARN duplicate category: {p['category']}")
        p.setdefault("author", "전 샤워")
        p.setdefault("published", True)
        if p["id"] not in by_id:
            added += 1
        by_id[p["id"]] = p
        cats.add(p.get("category"))
    merged = sorted(by_id.values(), key=lambda x: x.get("date", ""), reverse=True)
    POSTS_PATH.write_text(
        json.dumps({"posts": merged}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"blog-posts.json: existing {len(existing)} + new {added} → total {len(merged)}")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "publish_blog.py")], check=True)


if __name__ == "__main__":
    main()
