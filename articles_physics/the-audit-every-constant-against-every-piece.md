# __The Audit: Every Constant Against Every Piece__

## Introduction

**The claim.** Every one of the forty-nine rows has a coefficient, and every coefficient is one of the nineteen parameters or a canonical normalisation. The table below writes each row against the numbers that fix it.

**The answer.**

$$
\boxed{\;49\ \text{rows},\ 19\ \text{numbers},\ \text{and no row unfixed}\;}
$$

**Why the audit is not a tautology.** A list of forty-nine rows can be assembled from any set of terms, and the question the audit answers is whether the assembly is a theory: if a row's coefficient were a free number not in the list, the count of parameters would be wrong; if a row had no coefficient at all, the row would not be a term. The audit checks both directions on every row.

**The standing.** [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html) sorts the nineteen by constant; this article sorts the forty-nine by row. The two views are transposes of one another, and the transposition is the statement that the coefficient map is a well-defined function from rows to numbers.

## The Audit in One Table

| # | piece | coefficient | fixed by |
|---|---|---|---|
| 1 | gluon kinetic | $-\tfrac14$, canonical | none |
| 2 | photon kinetic | $-\tfrac14$, canonical | none |
| 3 | $Z$ kinetic | $-\tfrac14$, canonical | none |
| 4 | $W$ kinetic | $-\tfrac12$, canonical | none |
| 5 | $W$ mass | $-M_W^2$ | $g$, $v$ |
| 6 | $Z$ mass | $-\tfrac12M_Z^2$ | $g$, $\theta_W$, $v$ |
| 7 | $h$ kinetic | $\tfrac12$, canonical | none |
| 8 | $h$ mass | $-\tfrac12m_h^2$ | $m_h$ |
| 9 | $hWW$ | $-g^2v/2$ | $g$, $v$ |
| 10 | $hZZ$ | $-(g^2+g_{\mathrm Y}^2)v/4$ | $g$, $\theta_W$, $v$ |
| 11 | $hhWW$ | $-g^2/4$ | $g$ |
| 12 | $hhZZ$ | $-(g^2+g_{\mathrm Y}^2)/8$ | $g$, $\theta_W$ |
| 13 | $h^3$ | $-m_h^2/(2v)$ | $m_h$, $v$ |
| 14 | $h^4$ | $-m_h^2/(8v^2)$ | $m_h$, $v$ |
| 15 | $i\bar u\slashed\partial u$ | $1$, canonical | none |
| 16 | $i\bar c\slashed\partial c$ | $1$, canonical | none |
| 17 | $i\bar t\slashed\partial t$ | $1$, canonical | none |
| 18 | $i\bar d\slashed\partial d$ | $1$, canonical | none |
| 19 | $i\bar s\slashed\partial s$ | $1$, canonical | none |
| 20 | $i\bar b\slashed\partial b$ | $1$, canonical | none |
| 21 | $i\bar e\slashed\partial e$ | $1$, canonical | none |
| 22 | $i\bar \mu\slashed\partial \mu$ | $1$, canonical | none |
| 23 | $i\bar \tau\slashed\partial \tau$ | $1$, canonical | none |
| 24 | $i\bar \nu_e\slashed\partial \nu_e$ | $1$, canonical | none |
| 25 | $i\bar \nu_\mu\slashed\partial \nu_\mu$ | $1$, canonical | none |
| 26 | $i\bar \nu_\tau\slashed\partial \nu_\tau$ | $1$, canonical | none |
| 27 | mass of $u$ | $-m_{u}$ | $m_{u}$ |
| 28 | mass of $c$ | $-m_{c}$ | $m_{c}$ |
| 29 | mass of $t$ | $-m_{t}$ | $m_{t}$ |
| 30 | mass of $d$ | $-m_{d}$ | $m_{d}$ |
| 31 | mass of $s$ | $-m_{s}$ | $m_{s}$ |
| 32 | mass of $b$ | $-m_{b}$ | $m_{b}$ |
| 33 | mass of $e$ | $-m_{e}$ | $m_{e}$ |
| 34 | mass of $\mu$ | $-m_{\mu}$ | $m_{\mu}$ |
| 35 | mass of $\tau$ | $-m_{\tau}$ | $m_{\tau}$ |
| 36 | $h\bar uu$ | $-m_{u}/v$ | $m_{u}$, $v$ |
| 37 | $h\bar cc$ | $-m_{c}/v$ | $m_{c}$, $v$ |
| 38 | $h\bar tt$ | $-m_{t}/v$ | $m_{t}$, $v$ |
| 39 | $h\bar dd$ | $-m_{d}/v$ | $m_{d}$, $v$ |
| 40 | $h\bar ss$ | $-m_{s}/v$ | $m_{s}$, $v$ |
| 41 | $h\bar bb$ | $-m_{b}/v$ | $m_{b}$, $v$ |
| 42 | $h\bar ee$ | $-m_{e}/v$ | $m_{e}$, $v$ |
| 43 | $h\bar \mu\mu$ | $-m_{\mu}/v$ | $m_{\mu}$, $v$ |
| 44 | $h\bar \tau\tau$ | $-m_{\tau}/v$ | $m_{\tau}$, $v$ |
| 45 | QCD | $g_s$ | $g_s$ |
| 46 | QED | $eQ$ | $e$ |
| 47 | charged current, quarks | $g/\sqrt2$ times $V_{\mathrm{CKM}}$ | $g$, four mixing |
| 48 | charged current, leptons | $g/\sqrt2$ | $g$ |
| 49 | neutral current | $g/\cos\theta_W$ | $g$, $\theta_W$ |

## What the Table Shows

**The numbering is the audit's own.** The table groups rows by the kind of number that fixes them, so the masses sit together and the interactions sit last; the display numbers the same forty-nine rows by ancestor. Both orderings contain the same rows, and a reader comparing the two should compare the pieces and not the numbers.

**Seventeen rows carry no parameter.** The four gauge kinetics, the $h$ kinetic and the twelve fermion kinetics are canonical: their coefficients are fixed by the requirement that the fields be the ones whose commutators are the canonical ones. None of the seventeen consumes a number from the nineteen.

**The rest fall into five groups, and each group is one kind of number.** The nine mass rows are fixed by the nine masses. The nine Higgs–fermion rows are fixed by those masses and by $v$. The six vector rows ($W$ mass, $Z$ mass, $hWW$, $hZZ$, $hhWW$, $hhZZ$) are fixed by $g$, $\theta_W$ and $v$. The two self-pieces and the $h$ mass are fixed by $m_h$ and $v$. The five interaction rows are fixed by $g_s$, $e$ and $\theta_W$.

**The groups sum to forty-nine.** $17+9+9+6+3+5=49$, and the three is the $h$ mass with the two self-pieces.

**No row is unfixed and no coefficient is unused except one.** The exception is $\theta_{\mathrm{QCD}}$, whose piece is absent, and it is in the list of parameters precisely because it is the one exception.

## The Rows That Share a Number

**A mass appears in two rows.** Each of the nine masses fixes a mass row and a Higgs–fermion row, which is why the nine cost eighteen rows and nine numbers.

**A coupling appears in many.** $g$ fixes the $W$ mass, the $hWW$ row, the $hhWW$ row and the two charged currents; $\theta_W$ fixes the $Z$ mass, the $hZZ$ row, the $hhZZ$ row and the neutral current. The map from numbers to rows is many-to-many, and the audit table is the only place where the whole of it is visible.

**The canonical rows and the parameter rows are disjoint.** No canonical row consumes a parameter, and no parameter row is canonical. The partition is exact, which is what makes the count of the forty-nine compatible with the count of the nineteen.

## Checks

1. The row count. $4+2+2+2+2+2+12+9+9+5=49$.
2. The canonical rows. $4+1+12=17$ rows with no parameter.
3. The parameter rows. $49-17=32$, and each consumes at least one of the nineteen.
4. The nine masses. Nine mass rows and nine $h\bar ff$ rows, from nine numbers.
5. The two vector masses. Fixed by $g$, $\theta_W$ and $v$, and by nothing else.
6. The scalar. $m_h$ fixes three rows (the mass and the two self-pieces), together with $v$ in the two self-pieces.
7. The interactions. Five rows from three numbers, $g_s$, $e$ and $\theta_W$, with $g$ supplying the charged currents and the neutral current's denominator.
8. The sharing. The nine masses fix eighteen rows, the mass and the Higgs coupling of each species.
9. The exception. $\theta_{\mathrm{QCD}}$ fixes no row.
10. The transposition. The same content as [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html), read by rows instead of by columns.

## Summary

The audit writes each of the forty-nine rows against the numbers that fix it. Seventeen rows are canonical and consume no parameter; thirty-two consume at least one, and the shares are many-to-many.

The nine masses each fix two rows, a mass and a Higgs–fermion coupling, which is why the Yukawa sector is eighteen rows and nine numbers. The two couplings $g$ and $\theta_W$ and the scale $v$ fix the vector sector; $m_h$ and $v$ fix the scalar sector; $g_s$, $e$ and $\theta_W$ fix the interactions.

No row is unfixed, and one number fixes no row. The single exception is the vacuum angle, and its presence in the parameter list is the statement that the audit is not a bijection.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| canonical | a coefficient fixed by the commutators and not by a measurement |
| fixed by | the numbers of the nineteen that determine a row's coefficient |
| many-to-many | the map from numbers to rows, which is not a partition |

## Further Reading

- [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html). The transposed table.
- [The Complete Lagrangian](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html). The counts in one place.
- [Nineteen and Nineteen](nineteen-and-nineteen-the-parameter-count-before-and-after-the-rotation.html). The audit against the unbroken phase.
- [What the List Omits](what-the-list-omits-ghosts-the-theta-term-neutrino-mass-and-gravity.html). The exception: the vacuum angle and the measure.
- [The Completeness of the List](the-completeness-of-the-list-why-no-other-dimension-four-piece-exists.html). Why there is no fiftieth row.
