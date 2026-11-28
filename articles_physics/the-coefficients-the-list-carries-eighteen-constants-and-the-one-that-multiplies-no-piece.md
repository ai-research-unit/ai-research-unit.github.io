# __The Coefficients the List Carries: Eighteen Constants and the One That Multiplies No Piece__

## Introduction

**The claim.** The forty-seven pieces carry eighteen constants, and the theory has nineteen parameters. The nineteenth multiplies no piece. This article prints the map from constant to rows, both parametrisations of the eighteen, and the reason the nineteenth is counted apart.

**The answer.**

$$
\boxed{\;18=1+1+1+1+1+9+4,\qquad 18+1=19\;}
$$

**Why a map and not a table of numbers.** The corpus prints a measured strength only where the [Data Boundary](the-data-boundary.html) allows, and this category is not one of those places. Every constant below appears as a symbol and every relation as an equation, so the article states which pieces are fixed by which parameter and prints no value.

**The standing.** The eighteen are the Standard Model's, transcribed. The map is standard bookkeeping, with one structural point the bookkeeping makes visible: the parameter count is the same in the broken phase and in the symmetric one, and the maps between them are invertible.

## The Eighteen

**By group, with the rows each constant fixes.**

| Constant | Pieces it fixes | Rows |
|---|---|---|
| $g_s$ | gluon kinetic, QCD | $2$ |
| $e$ | photon kinetic, QED, $\gamma W^+W^-$, $W^+W^-AA$ | $4$ |
| $\theta_W$ | $Z$ kinetic, $ZWW$, $WWZZ$, $WWAZ$, neutral current, $hZZ$, $hhZZ$ | $7$ |
| $v$ | $W$ and $Z$ masses, $hWW$, $hZZ$, $hhWW$, $hhZZ$, nine $h\bar ff$ | $15$ |
| $m_h$ | Higgs mass, $h^3$, $h^4$ | $3$ |
| $m_f$, one per species | that species' mass, that species' $h\bar ff$ | $18$ |
| four mixing parameters | the two charged-current pieces | $2$ |

**The rows are shared, and the column does not sum to forty-seven.** The $W^+W^-ZZ$ vertex needs both $e$ and $\theta_W$; a mass needs $v$ and the species' constant; a $h\bar ff$ piece needs $v$ and the species' mass. A map from parameters to rows is not a partition, and the article does not present it as one.

**The nine masses are the nine Yukawa eigenvalues times the vacuum value.** Writing them as masses rather than as couplings is a choice, and it is the choice the broken phase makes: in the mass basis each of the nine rows carries one number, and the mixing is carried by the two charged-current pieces alone.

**The four mixing parameters are three angles and one phase.** They enter no mass, no kinetic term and no neutral-current piece at tree level; they enter the charged current, and through it every flavour-changing process.

## The Two Parametrisations

**Broken and symmetric, with the same count.**

| Broken phase | Symmetric phase | Relation |
|---|---|---|
| $g_s$ | $g_s$ | identical |
| $e$ | $g$, $g_{\mathrm Y}$ | $e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$ |
| $\theta_W$ | $g$, $g_{\mathrm Y}$ | $\tan\theta_W=g_{\mathrm Y}/g$ |
| $v$ | $\mu^2$, $\varpi_{\mathrm{cpl}}$ | $v^2=\mu^2/\varpi_{\mathrm{cpl}}$ |
| $m_h$ | $\varpi_{\mathrm{cpl}}$, $v$ | $m_h^2=2\varpi_{\mathrm{cpl}}v^2$ |
| $m_f$ | $y_f$, $v$ | $m_f=y_fv/\sqrt2$ |
| four mixing parameters | the Yukawa matrices | the mismatch of the two diagonalisations |

**The gauge pair is a change of coordinates on a plane.** The symmetric phase carries $g$ and $g_{\mathrm Y}$; the broken phase carries $e$ and $\theta_W$. Two numbers on each side, and the map is invertible: $g=e/\sin\theta_W$ and $g_{\mathrm Y}=e/\cos\theta_W$.

**The scalar pair is a change of coordinates and not a simplification.** The symmetric phase carries $\mu^2$ and $\varpi_{\mathrm{cpl}}$; the broken phase carries $v$ and $m_h$. The map is invertible: $\varpi_{\mathrm{cpl}}=m_h^2/(2v^2)$ and $\mu^2=\varpi_{\mathrm{cpl}}v^2=m_h^2/2$. The broken pair looks more physical and carries the same two numbers.

**The nine masses are nine to nine.** Nine Yukawa eigenvalues become nine masses at one scale $v$. What the change of variables buys is that the $h\bar ff$ coupling is then a number in units of $v$, which is the statement that the Higgs couples in proportion to mass.

## The Nineteen in Two Columns

**Ten masses, one scale, eight dimensionless numbers.**

| Column | Entries | Count |
|---|---|---|
| masses | nine fermion masses and $m_h$ | $10$ |
| one scale | $v$ | $1$ |
| dimensionless | $g_s$, $e$, $\theta_W$, the four mixing parameters, $\theta_{\mathrm{QCD}}$ | $8$ |

**Why the Higgs mass is in the first column.** It is a mass and it is measured like one; putting it with the couplings because it comes from $\varpi_{\mathrm{cpl}}$ would be a statement about the symmetric variables and not about the broken list.

**Why $v$ is alone.** It is the only number with the dimension of mass that is not a particle's mass. Every dimensionful entry is either a mass or this one scale, and the scale is what converts the nine Yukawa eigenvalues into masses.

**Why the vacuum angle is in the third column although it multiplies no row.** The columns are sorted by dimension and not by the census. $\theta_{\mathrm{QCD}}$ is dimensionless, so it belongs with the dimensionless numbers, and the fact that no row carries it is stated in the next section.

**The count.** $10+1+8=19$, and the same table read without the vacuum angle is $10+1+7=18$, which is the count of the constants that carry rows.

## The One That Multiplies No Piece

**$\theta_{\mathrm{QCD}}$, and why it is counted.** The operator $G^a_{\mu\nu}\tilde G^{a\mu\nu}$ is a total derivative, so it contributes no vertex at any order of the tree expansion and is not a piece of the list. Its parameter is nevertheless a parameter of the theory, for two reasons: no field redefinition that leaves the rest of the list fixed removes it, and its effect is not zero, because the fermion measure is not invariant under the chiral rotation that would remove it.

**Where nineteen comes from.** Eighteen constants multiply the forty-seven rows, and the nineteenth multiplies the operator that is not a row. A count that omitted it would be a count of the couplings of the list and not of the parameters of the theory, and [The Complete Lagrangian](the-census-in-one-display-forty-seven-terms-fifty-three-vertices-twenty-blocks-and-nineteen-parameters.html) says which of the two it prints.

**Why it is not a piece.** A piece changes a vertex, and this parameter changes none. It changes the vacuum, and through the vacuum the neutron's electric dipole moment. The distinction is the distinction between a coupling and a vacuum angle, and [The Theta Parameter and Strong CP](the-theta-parameter-and-strong-cp-in-biquaternionic-form.html) carries it.

## Why the Symbols

**One rule, obeyed by construction.** A page that printed the eighteen values would be a fifteenth entry in the register of the [Data Boundary](the-data-boundary.html), and the register is closed. The category therefore prints relations: $M_W=gv/2$, $M_Z=M_W/\cos\theta_W$, $m_h=\sqrt{2\varpi_{\mathrm{cpl}}}\,v$, $m_f=y_fv/\sqrt2$.

**What the symbols buy.** A relation is checkable and a number is not. The reader can verify that $m_f=y_fv/\sqrt2$ has the dimensions of a mass, that $M_Z=M_W/\cos\theta_W$ gives $\rho=1$, and that $m_h^2=2\varpi_{\mathrm{cpl}}v^2$ makes the cubic and quartic self-couplings functions of one number. A table of values would show none of the three.

**What the symbols cost.** A reader who wants the numbers must go to the parameter table of [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html), where they are printed once with scheme and scale. That is the price of one register, paid deliberately.

## Checks

1. The count. $1+1+1+1+1+9+4=18$, and $18+1=19$.
2. The invertibility. $(g,g_{\mathrm Y})\leftrightarrow(e,\theta_W)$ is two to two; $(\mu^2,\varpi_{\mathrm{cpl}})\leftrightarrow(v,m_h)$ is two to two; nine $y_f\leftrightarrow$ nine $m_f$ at fixed $v$.
3. The dimensions. $m_f=y_fv/\sqrt2$ is a dimensionless number times a mass; $m_h^2=2\varpi_{\mathrm{cpl}}v^2$ is dimensionless times a mass squared; $M_Z=M_W/\cos\theta_W$ is a ratio.
4. The coverage. Each of the eighteen appears in at least one row of the first table, and every row of the forty-seven is fixed by at least one of them.
5. The non-partition. $e$ and $\theta_W$ share the $W^+W^-ZZ$ row; $v$ and $m_f$ share every $h\bar ff$ row.
6. The theta check. $G\tilde G$ is a total derivative, contributes no vertex, and is not removable by any field redefinition that preserves the rest of the list.
7. The register. No numeric value of any of the eighteen appears in this article or in its companions; the values are the parameter table's.
8. The symmetric-phase count. $g_s$, $g$, $g_{\mathrm Y}$, $\mu^2$, $\varpi_{\mathrm{cpl}}$, nine $y_f$ and four mixing parameters is $1+1+1+1+1+9+4=18$.

## Summary

The forty-seven pieces carry eighteen constants: the strong coupling, the electric charge, the weak mixing angle, the vacuum value, the Higgs mass, nine fermion masses and four mixing parameters. Each constant fixes a set of rows, the sets overlap, and the map from constants to rows is not a partition.

The same eighteen appear in the symmetric phase as two gauge couplings, two scalar parameters, nine Yukawa eigenvalues and four mixing parameters. The two parametrisations are related by invertible changes of variables on the gauge pair and on the scalar pair, so the count is preserved. Nine Yukawa couplings becoming nine masses at one scale is a change of variables that exposes the proportionality of the Higgs coupling to mass.

The nineteenth parameter, $\theta_{\mathrm{QCD}}$, multiplies no piece. Its operator is a total derivative, contributes no vertex, and is not removable, so it counts as a parameter of the theory and not as a coupling of the list.

The category prints symbols and relations and no values, by the rule of the data boundary. The values live in the parameter table, where they are printed once.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $g_s$ | Strong coupling |
| $e$ | Electric charge, $e=g\sin\theta_W=g_{\mathrm Y}\cos\theta_W$ |
| $\theta_W$ | Weak mixing angle, $\tan\theta_W=g_{\mathrm Y}/g$ |
| $v$ | Vacuum value, $M_W=gv/2$ |
| $m_h$ | Higgs mass, $m_h^2=2\varpi_{\mathrm{cpl}}v^2$ |
| $m_f$ | A fermion mass, $m_f=y_fv/\sqrt2$ |
| four mixing parameters | Three angles and one phase of the quark mixing matrix |
| $\theta_{\mathrm{QCD}}$ | The vacuum angle, the parameter that multiplies no piece |
| $\varpi_{\mathrm{cpl}}$ | The quartic of the potential, the symmetric-phase partner of $m_h$ |

## Further Reading

- [The Data Boundary: Two Claims, Sixteen Measured Strengths, and a Deletion Test](the-data-boundary.html). The register that keeps the values out of this category.
- [The Standard Model: Content, Quantum Numbers and the Nineteen Parameters](the-standard-model-content-quantum-numbers-and-the-nineteen-parameters.html). The values themselves, with scheme and scale.
- [The Parameter Count as the Measure of the Framework's Boundary](the-parameter-count-as-the-measure-of-the-frameworks-boundary.html). The nineteen typed by the kind of object each one is.
- [Nineteen and Nineteen](nineteen-and-nineteen-the-parameter-count-before-and-after-the-rotation.html). The two-column count, sector by sector.
- [The Theta Parameter and Strong CP in Biquaternionic Form](the-theta-parameter-and-strong-cp-in-biquaternionic-form.html). The operator whose parameter multiplies no piece.
