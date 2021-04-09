#!/bin/bash

subjects='AVL-003 AVL-005 AVL-007 AVL-010 AVL-101 AVL-103 AVL-004 AVL-006 AVL-009 AVL-011 AVL-102 AVL-105'

for s in ${subjects[@]}; do

	mri_cvs_register --mov $s
done

