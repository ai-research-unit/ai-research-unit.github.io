# __Nineteen and Nineteen: The Parameter Count Before and After the Rotation__

## Introduction

**The claim.** The Standard Model has nineteen parameters. Written in the symmetric phase it displays sixty numbers and nineteen survive; written in the broken phase it displays nineteen and none is redundant. The two counts agree, and this article shows the agreement sector by sector rather than asserting it.

**The answer.**

$$
\boxed{\;60\;\xrightarrow[\;41\text{ removed}\;]{}\;19\;\equiv\;19\;}
$$

**Why the equality is not obvious.** The two descriptions do not look alike. One carries three gauge couplings and two scalar parameters; the other carries one charge, one mixing angle, one vacuum value and one mass. One carries three complex Yukawa matrices; the other carries nine masses and four mixing parameters. A reader who counts the letters will get different answers unless the map between the two sets of letters is written out.

**The standing.** The symmetric-phase count is the corpus's, from [The Complete Lagrangian](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html); the broken-phase count is the parameter table's, from [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html). What this article adds is the comparison, which neither of those makes.

## The Symmetric Count, in One Table

**Sixty written, forty-one removed, nineteen physical.**

| Sector | Written | Group acting | Stabiliser | Physical |
|---|---|---|---|---|
| gauge | $3$ | — | — | $3$ |
| scalar | $2$ | — | — | $2$ |
| vacuum angle | $1$ | — | — | $1$ |
| quark flavour | $36$ | $U(3)_Q\times U(3)_u\times U(3)_d$, $27$ | $U(1)_B$, $1$ | $10$ |
| lepton flavour | $18$ | $U(3)_L\times U(3)_e$, $18$ | $U(1)^3$, $3$ | $3$ |
| **total** | $\mathbf{60}$ | $\mathbf{45}$ | $\mathbf{4}$ | $\mathbf{19}$ |

**The rule of the count.** The physical number is the written number less the dimension of the group that acts, plus the dimension of the subgroup that leaves the couplings in their diagonal form. The last term is not a fudge: after diagonalisation a residual abelian group remains and it acts on nothing.

**The removal, graded by sector.** The quark sector loses $36-27+1=26$; the lepton sector loses $18-18+3=15$. The two add to forty-one.

**Why the removal is not a small correction.** The forty-one numbers are the freedom of choice of flavour basis. They are not small, they are not approximately zero, and no measurement could ever see them. A count that kept them would be a count of the Lagrangian's letters and not of the theory.

## The Broken Count, in the Same Form

**Nineteen written, none removed.**

| Sector | Written | Removed | Physical |
|---|---|---|---|
| strong | $1$ | $0$ | $1$ |
| electroweak | $2$ | $0$ | $2$ |
| scalar | $2$ | $0$ | $2$ |
| vacuum angle | $1$ | $0$ | $1$ |
| quark flavour | $10$ | $0$ | $10$ |
| lepton flavour | $3$ | $0$ | $3$ |
| **total** | $\mathbf{19}$ | $\mathbf{0}$ | $\mathbf{19}$ |

**Why nothing is removed.** The mass basis is a choice already made. Once the nine masses are numbers, the bi-unitary transformations that produced them have been spent, and the only freedom left is a residual abelian group acting on each species by a phase, which changes nothing. The count of written numbers is therefore the count of physical ones.

**The quark flavour block is ten: six masses and four mixing parameters.** The four are three angles and one phase, and their counting is the counting of a unitary matrix modulo rephasing. A general $3\times3$ unitary has nine parameters; rephasing the six quark fields removes $2N-1=5$; four remain.

**The lepton flavour block is three: three masses and no mixing.** In the minimal model there is no right-handed neutrino, so there is no leptonic mixing matrix to count. The matrix exists in principle, but it multiplies a neutrino mass term that the model does not have, and a matrix that multiplies nothing is not a parameter.

## The Typology of the Nineteen

The two tables above count by sector. A second cut counts by *kind of mathematical object*, and it is the one that says what would have to be built.

| Kind | What it is | Which entries | Count |
|---|---|---|---|
| Group coordinate | A point in a parameter space the algebra supplies | mixing parameters | $4$ |
| Connection normalisation | The size of a coupling in a covariant derivative | $g_s$, $g$, $g_{\mathrm Y}$ | $3$ |
| Central phase | The phase of a topological term | $\theta_{\mathrm{QCD}}$ | $1$ |
| Eigenvalue | A mass, that is a spectrum of an operator | nine fermion masses, $M_H$ | $10$ |
| Scale | The one dimensionful normalisation | $v$ | $1$ |

The counts add to nineteen, and the classification is exhaustive: a number in a Lagrangian is a coupling, a phase, an eigenvalue or a scale, and the mixing angles are coordinates with no other home.

**The kinds matter more than the sectors.** The sector split is about physics; the kind split is about what would have to be built. A group coordinate needs a group and a selection principle; a connection normalisation needs a connection and a normalisation principle; a central phase needs a topology and a value; an eigenvalue needs an operator and a spectral principle; a scale needs a mechanism that breaks dilatation invariance. Those are five different machines, and the framework has some of them and not others.

## Eight With an Arena, Nine With an Eigenvalue, Two With Nothing

The same nineteen, cut by what the framework can *represent* rather than by what the number is.

| Group | Entries | Count | What the framework has |
|---|---|---|---|
| Arena | mixing, couplings, vacuum angle | $8$ | The group, the connection, the phase: represented, value free |
| Eigenvalue only | the nine fermion masses | $9$ | A mass term, but no spectral principle |
| Nothing | $v$, $M_H$ | $2$ | No scale mechanism, no scalar mass principle |

The shares are $42.1\%$, $47.4\%$ and $10.5\%$. One entry is in two groups, and the reason is exact: $M_H$ is an eigenvalue by kind and belongs to "nothing" by arena, because the operator it is a spectrum of sits in a scalar sector the framework does not host. For the nine fermion masses the framework does host the operator — the Dirac mass term and the Yukawa matrices — and lacks only the principle that picks the eigenvalues. The kind and the arena are two different questions, and $M_H$ is the one entry where the answers differ.

**The framework's own list, counted the same way.** Three continuous parameters: $ϙ$, the central charge of the minimal coupling; $m$, the mass of the massive field equation; and $k_m$, the constant of that equation. None is fixed by the algebra, and none overlaps the nineteen. The total is therefore

$$
19+3=22 ,\qquad
\text{imported share}=\frac{19}{22}=86.4\% ,
$$

so the reformulation is not more parsimonious than the model it reformulates; it has a different list, and it adds a short one to a long one. Its defence is that its objects are geometric, not that its count is small. And the score on the same measure is stark: twenty-two parameters and **zero predictions not shared with the model**.

## The Map Between the Two Tables

**Row by row.**

| Symmetric row | Broken row | The map |
|---|---|---|
| $g_s$ | $g_s$ | identity |
| $g$, $g_{\mathrm Y}$ | $e$, $\theta_W$ | $e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$, $\tan\theta_W=g_{\mathrm Y}/g$ |
| $\mu^2$, $\varpi_{\mathrm{cpl}}$ | $v$, $m_h$ | $v^2=\mu^2/\varpi_{\mathrm{cpl}}$, $m_h^2=2\varpi_{\mathrm{cpl}}v^2$ |
| $y_u$, $y_d$, $y_e$ | nine masses, four mixing parameters | singular values and the mismatch of the two diagonalisations |
| $\theta_{\mathrm{QCD}}$ | $\theta_{\mathrm{QCD}}$ | identity |

**The flavour row is the only one where the map is not a coordinate change on a fixed number of letters.** Three complex $3\times3$ matrices carry fifty-four real numbers, which is thirty-six plus eighteen. The broken side carries thirteen. The difference is the forty-one, and the map is many-to-one: the same thirteen physical numbers arise from a forty-one-dimensional family of matrices. That is what a redundancy is, and it is why the symmetric count needs the group action to be stated.

**The gauge and scalar rows are coordinate changes on two-dimensional spaces.** Two letters become two letters in both cases, and the maps are invertible. Nothing is removed and nothing is created; the names change because the basis changes.

## Why the Count Cannot Drift

**Three ways a count can fail, and none of them happens here.**

- A piece with no coefficient. Every quadratic piece carries one and every interaction carries one; [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html) maps them.
- A coefficient shared by two pieces in one description and not in the other. The $W^+W^-ZZ$ vertex is fixed by $e$ and $\theta_W$ in the broken phase and by $g$ and $g_{\mathrm Y}$ in the symmetric one; the sharing is the same sharing under the map.
- A parameter multiplying nothing in one description and something in the other. $\theta_{\mathrm{QCD}}$ multiplies nothing in both, because the operator is a total derivative before and after the breaking.

**The structural reason the counts agree.** The rotation is an invertible change of basis in the space of fields, and a change of basis cannot change the number of independent coefficients of a function of those fields. The count is a property of the function, and the two descriptions are two writings of one function.

## Checks

1. The symmetric sum. $3+2+1+36+18=60$.
2. The removal. $27-1=26$ in the quark sector and $18-3=15$ in the lepton sector, and $26+15=41$.
3. The symmetric physical count. $60-41=19$.
4. The quark block. $36-27+1=10$, and $6$ masses $+3$ angles $+1$ phase $=10$.
5. The lepton block. $18-18+3=3$, three masses.
6. The broken sum. $1+2+2+1+10+3=19$.
7. The identity. $19=19$, and the equality is the statement that the two maps of §*The Map Between the Two Tables* are bijections on the parameter sets.
8. The mixing count. A $3\times3$ unitary has $9$ parameters, rephasing removes $2\times3-1=5$, and $9-5=4$.
9. The cross-check with the piece count. Forty-nine pieces, twenty-nine of them quadratic. Fourteen of the twenty-nine carry unit normalisation by the canonical form; the other fifteen carry three couplings, two vector masses, one scalar mass and nine fermion masses, and $3+2+1+9=15$.

## Summary

The Standard Model has nineteen parameters in both phases. In the symmetric phase sixty numbers are written, forty-one are removed by field redefinitions — twenty-six in the quark sector and fifteen in the lepton sector — and nineteen survive. In the broken phase nineteen numbers are written and none is removed, because the mass basis has already spent the freedom.

The two descriptions are related row by row: the strong coupling to itself, the two gauge couplings to the charge and the mixing angle, the two scalar parameters to the vacuum value and the Higgs mass, the three Yukawa matrices to nine masses and four mixing parameters, and the vacuum angle to itself. The gauge and scalar maps are invertible changes of coordinates on two-dimensional spaces; the flavour map is many-to-one, and its fibres are the forty-one removed numbers.

The count cannot drift, for a structural reason and not by inspection: a change of basis in field space cannot change the number of independent coefficients of the function of the fields. The two lists are two writings of one function, and the count is a property of the function.

The four mixing parameters are what survives the mismatch of the up-type and down-type diagonalisations, and their number is the number of parameters of a unitary matrix modulo rephasing: nine less five is four.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $60$ | Real numbers written in the symmetric phase |
| $41$ | Removed by field redefinitions, $26$ quark and $15$ lepton |
| $19$ | Physical parameters, in either phase |
| $U(3)_Q\times U(3)_u\times U(3)_d$ | The quark flavour redefinition group, dimension $27$ |
| $U(3)_L\times U(3)_e$ | The lepton flavour redefinition group, dimension $18$ |
| $2N-1=5$ | The number of phases removable by rephasing three generations |
| $9-5=4$ | The mixing parameters, three angles and one phase |

## Further Reading

- [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html). The nineteen, itemised.
- [The Coefficients the List Carries](the-coefficients-the-list-carries-eighteen-constants-and-the-one-that-multiplies-no-piece.html). The same eighteen in the broken phase, with the map to rows.
- [The CKM Matrix and CP Violation in Biquaternionic Form](the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html). The four mixing parameters and where the phase enters.
