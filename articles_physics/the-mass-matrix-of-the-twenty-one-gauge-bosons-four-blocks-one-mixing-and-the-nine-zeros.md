# __The Mass Matrix of the Twenty-One Gauge Bosons: Four Blocks, the Nine Zeros, and No Tree-Level Charged Mixing__

## Introduction

**The twenty-one gauge directions split into four blocks, and in the minimal content none of them mixes.** The blocks are eight colour directions, six leptoquark directions, three neutral directions and four charged ones, $8+6+3+4=21$. The first two are settled at the transition, the third has no free angle, and the fourth is diagonal because the two weak factors are broken by two different fields.

**The four blocks are exact and not an approximation.** Each vacuum of the chain is a colour singlet with a definite electric charge, so every mass term carries the colour representation and the charge of both of its generators. Two generators of different colour or different charge therefore never mix, at any order of perturbation theory. The block structure is a statement about the quantum numbers the vacua carry, and it survives every correction that does not break colour or charge.

**What the article computes, and what it borrows.** It states the four blocks, derives the charged block from the two scalar kinetic terms, and shows that the block is diagonal: $M_{W}^{2}=\tfrac14g_L^{2}v^{2}$ and $M_{W_R}^{2}=\tfrac14g_R^{2}v_C^{2}$, with no off-diagonal entry and therefore $W=W_L$ and $\rho=1$ at tree level. **A $W_L$–$W_R$ mixing angle exists only if a scalar carries both weak indices**, and the minimal content has none: $H$ is an $\mathrm{SU}(2)_R$ singlet and $\Phi$ is an $\mathrm{SU}(2)_L$ singlet. The bidoublet that would mix them is treated in §*The Bidoublet Extension* and is excluded by the measured $\rho$. The colour, leptoquark and neutral blocks are quoted with a pointer to the article that owns each: [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html) for the first two and [The Neutral Sector](the-neutral-sector-three-ingredients-rank-two-one-null-direction.html) for the third.

**The one sentence worth carrying away.** In the minimal content the charged block is diagonal, so

$$
\rho=\frac{M_{W}^{2}}{M_{Z}^{2}\cos^{2}\theta_W}=1\quad\text{at tree level, exactly.}
$$

**The departure from $1$ needs a scalar with both weak indices, and the measured value $1.00038\pm0.00020$ says the mixing is at most of order $10^{-4}$.** That is a statement about the content, not a tuning.

## The Four Blocks

**The split.** The twenty-one field names of the ledger are sorted by what the two vacua do to them:

| block | generators | colour | charge | scale at which it fills |
|---|---|---|---|---|
| colour | $8$ | $\mathbf8$ | $0$ | never |
| leptoquark | $6$ | $\mathbf3$ and $\bar{\mathbf3}$ | $\pm\tfrac23$ | $M_C$ |
| neutral | $3$ | $\mathbf1$ | $0$ | $M_C$ and $v$ |
| charged | $4$ | $\mathbf1$ | $\pm1$ | $M_C$ and $v$ |

$8+6+3+4=21$. The charged block counts four real generators because the two complex fields $W^{+}_{L}$ and $W^{+}_{R}$ carry two real components each.

**Why the split is exact.** A mass term is quadratic in two generators and linear in the vacuum that produces it. Every vacuum of the chain is a colour singlet with $Q=0$, so the mass term is invariant under colour and under electric charge, so it vanishes between two generators whose colour representations or charges differ. The blocks are the eigenspaces of (colour representation, $Q$), and no correction that preserves colour and charge can move a mass across them.

**What the split is not.** It is not a statement about the algebra: the four blocks are not subalgebras, and the charged and neutral blocks are not even inside $\mathfrak{su}(4)$ — their generators are the weak ones. The split is a statement about the vacua, and it is the reason each block can be computed on its own.

## The Colour Block: Eight Zeros

**The eight colour directions are massless at every scale, exactly.** Two reasons, and both are exact.

**The first vacuum.** $D=\operatorname{diag}(-3,1,1,1)$ is a multiple of the identity on the colour triple, so every colour generator commutes with it: the colour planes have $\lambda_j=\lambda_k$ and the two colour diagonals commute with it. A generator that commutes with the vacuum has zero mass, which is the kernel statement of [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html).

**The second vacuum.** $H$ is a colour singlet, so its vacuum expectation value does not couple to a colour generator at all. The same holds for $\Phi$, whose vacuum lies along the lepton line, and the lepton line is a colour singlet.

**The consequence.** The $8\times8$ colour block is zero, not small, and colour is unbroken at every step of the chain. This is the matrix statement of the corpus's claim that colour is a stabiliser at every scale.

## The Leptoquark Block: Six at $32v^{2}$

**The six leptoquark directions are the six planes through the lepton line, and they all take the same mass at the first breaking.** In the physics basis the block is $32v^{2}$ times the identity of dimension six:

$$
M^{2}_{\text{lepto}}=32v^{2}\,\mathrm I_{6},\qquad 32=2\cdot4^{2},\qquad 4=1-(-3).
$$

The leakage is the entry-by-entry computation of [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html); the reason is the identity of [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html), which says that the mass on a plane is twice the square of the vacuum's eigenvalue difference across it. **The six are equal because the vacuum has one lepton line and three equal colour lines**, so all six differences are the same number.

**The later breaking adds nothing here.** $H$ is colour-blind, and the leptoquarks have already left the unbroken algebra at $M_C$. The block stays $32v^{2}$ at tree level; the one-loop shift is the effective-potential article's.

## The Neutral Block: Rank Two and One Null Direction

**Three fields, two vacuum directions, one null vector.** The neutral block is spanned by $W^{3}_{L}$, $W^{3}_{R}$ and the surviving $\mathrm{SU}(4)$ Cartan $B'$, and each vacuum contributes a rank-one term: one from $\Phi$'s vacuum along $a_1=\bigl(0,\tfrac12,-\sqrt{\tfrac38}\bigr)$ with weight $v_C^{2}$, and one from $H$'s vacuum along $a_2=\bigl(-\tfrac12,0,\sqrt{\tfrac38}\bigr)$ with weight $v^{2}$.

**The two vectors are independent, and that is the whole of the neutral sector.** Their norms are both $\tfrac58$ and their overlap is $-\tfrac38$, so the rank is two and there is exactly one massless neutral. **The direction is the cross product and nothing else**: $a_1\times a_2=\tfrac{\sqrt6}{8}\bigl(1,1,\sqrt{\tfrac23}\bigr)$, the photon, in the $(T_{3L},T_{3R},T^{15})$ normalisation. The full derivation, the Schur complement and the checks are [The Neutral Sector](the-neutral-sector-three-ingredients-rank-two-one-null-direction.html)'s.

**The numbers.** At $v_C=10v$ the two massive eigenvalues are $0.3986$ and $62.7$ in units of $g^{2}v^{2}$: the light one is $\tfrac25g^{2}v^{2}$ to leading order in $v/v_C$, the heavy one $\tfrac58g^{2}v_C^{2}$.

**Why there is no angle here.** A $3\times3$ block fed by two rank-one terms has one free direction in the vector pair and no more, and both vectors are fixed by the quantum numbers of the fields that take the vevs. **So the neutral sector has no adjustable angle and the charged sector has none either**: the only angle a left–right model can have comes from a scalar that takes two vevs at once, which is the bidoublet of §*The Bidoublet Extension*.

## The Charged Block: Diagonal

**The fields and the two vacua.** The charged block is spanned by $W^{+}_{L}$ and $W^{+}_{R}$. It is fed by two fields, each with one weak index: $H$ is an $\mathrm{SU}(2)_L$ doublet and an $\mathrm{SU}(2)_R$ singlet, and $\Phi$ is the reverse. **So each field gives a mass to its own pair and to nothing else**, and no operator connects $W_L$ to $W_R$ at tree level.

**The two masses.** With $\langle H\rangle$ along the lower component and $\langle\Phi\rangle$ along the lepton line of the right doublet,

$$
M_{W}^{2}=\tfrac14g_L^{2}v^{2},\qquad M_{W_R}^{2}=\tfrac14g_R^{2}v_C^{2},
$$

and the $2\times2$ block is

$$
\mathcal M^{2}_{\pm}=\frac14\begin{pmatrix}g_L^{2}v^{2}&0\\ 0&g_R^{2}v_C^{2}\end{pmatrix}.
$$

**Three consequences, and they are the article's point.**

**The physical $W$ is $W_L$, exactly.** The eigenvectors are the unit vectors, so no admixture of $W_R$ survives in the light state at tree level. **The observed $W$ couples purely left-handedly, and this block says the same thing algebraically.**

**$\rho=1$ exactly.** $M_Z^{2}=\tfrac14\bigl(g_L^{2}+g_Y^{2}\bigr)v^{2}$ from the neutral block, so the ratio is $1$ at tree level with no correction to absorb. **The corpus's earlier $1-\sin2\beta$ was a property of content the minimal model does not have.**

**The ratio of the two charged masses is the same number as the leptoquark ratio.** $M_X^{2}/M_{W_R}^{2}=2g_4^{2}/g_R^{2}$, because the sextet and the right pair are the two indices of one field at one scale.

## The Bidoublet Extension

**Why it is here, and what it is.** A scalar in $(\mathbf1,\mathbf2,\mathbf2)$ carries both weak indices, so its vacuum can mix the two charged pairs. **The minimal content has no such field; the section is the ledger of what adding one would cost.**

**The vacuum and the two entries.** Let the bidoublet's vacuum be

$$
\langle B\rangle=\begin{pmatrix}\kappa&0\\0&\kappa'\end{pmatrix},\qquad v^{2}=\kappa^{2}+\kappa'^{2},
$$

with the two diagonal entries neutral and the two off-diagonal entries charged. With the right factor acting by $B\mapsto B\,\sigma_a^{\mathsf T}/2$,

$$
D_\mu B=\partial_\mu B-i g_L\frac{\sigma_a}{2}W^{a}_{L\mu}B+i g_R B\frac{\sigma_a^{\mathsf T}}{2}W^{a}_{R\mu},
$$

and the off-diagonal entries at the vacuum are

$$
(D_\mu B)_{12}=-\frac{i}{\sqrt2}g_L\kappa'\,W^{+}_{L}+\frac{i}{\sqrt2}g_R\kappa\,W^{-}_{R},\qquad
(D_\mu B)_{21}=-\frac{i}{\sqrt2}g_L\kappa\,W^{-}_{L}+\frac{i}{\sqrt2}g_R\kappa'\,W^{+}_{R}.
$$

**The block.** With the kinetic term $\tfrac12\operatorname{tr}\bigl[(D_\mu B)^{\dagger}(D_\mu B)\bigr]$,

$$
\mathcal M^{2}_{\pm}=\frac14\begin{pmatrix}g_L^{2}v^{2}&\pm2g_Lg_R\kappa\kappa'\\ \pm2g_Lg_R\kappa\kappa'&g_R^{2}v^{2}\end{pmatrix}.
$$

**The sign of the off-diagonal is a convention and no eigenvalue depends on it.** It is the relative phase of $W^{+}_{L}$ and $W^{+}_{R}$, which a redefinition removes.

**The determinant, and why alignment is a bound.** For a $2\times2$ block $\begin{pmatrix}A&C\\C&B\end{pmatrix}$,

$$
\det\mathcal M^{2}_{\pm}=\frac{g_L^{2}g_R^{2}}{16}\bigl[(v^{2})^{2}-4\kappa^{2}\kappa'^{2}\bigr]=\Bigl(\frac{g_Lg_R}{4}\Bigr)^{2}\bigl(\kappa^{2}-\kappa'^{2}\bigr)^{2}\ \ge 0 ,
$$

so the determinant vanishes exactly when $\kappa=\kappa'$ and the block is then rank one with null vector $(g_R,-g_L)$. **A massless charged boson is a physical catastrophe, so whatever the vacuum is, $\kappa\neq\kappa'$.**

**The eigenvalues and the two physical states.** At equal couplings,

$$
M^{2}_{\pm}=\tfrac14g^{2}v^{2}\bigl(1\mp\sin2\beta\bigr),\qquad \tan\beta=\frac{\kappa'}{\kappa},\qquad \kappa^{2}+\kappa'^{2}=v^{2},
$$

and the eigenvectors are $(1,1)/\sqrt2$ and $(1,-1)/\sqrt2$ at every $\beta$. **So the extension predicts a $W$ that is half $W_L$ and half $W_R$, with mixing angle $\pi/4$ at equal couplings and a splitting $\propto\sin2\beta$.**

**And that is why the minimal content has none of it.** A half-right-handed $W$ is excluded by the charged-current couplings, and the same block moves $\rho$:

$$
\rho=\frac{M_{W}^{2}}{M_{Z}^{2}\cos^{2}\theta_W}=1-\sin2\beta ,
$$

which at $\beta=0.1$ is $0.8013=1-\sin0.2$ against a measured $1.00038\pm0.00020$. **The measurement reads it as $\tan\beta=-(1.9\pm1.0)\times10^{-4}$: the mixing must vanish to four orders.** A bidoublet is therefore not a variant of the minimal content but a different model, and the corpus's charged block belongs to it.

**What the extension does not touch.** The determinant identity, the alignment bound and the $\pi/4$ result are correct for the theory they describe. **They describe a theory with a bidoublet; the corpus's content has none.**

## The Count in Blocks

**Two counts, one block structure.** The blocks give both the massless and the massive count without a second ledger:

$$
\underbrace{8}_{\text{colour}}+\underbrace{1}_{\text{photon}}=9\ \text{massless},\qquad
\underbrace{6}_{\text{leptoquark}}+\underbrace{2}_{\text{neutral}}+\underbrace{4}_{\text{charged}}=12\ \text{massive}.
$$

**The nine.** The colour eight stay massless forever and the photon is a null direction of the neutral block, so the two zeros have two different reasons: one is a stabiliser of the vacuum and the other is an eigenvector of the neutral block.

**The twelve.** Six fill at $M_C$ and three of the weak six fill at the same scale: the $W^{\pm}_{R}$ pair and the $Z_R$. The remaining three — the $W^{\pm}_{L}$ pair and the $Z$ — fill at $v$. **The block structure and the chain agree step by step**: four blocks, two scales, and every mass at the scale of the vacuum that produced it.

## What the Article Does Not Do

**It does not fix a coupling.** Both $g_L$ and $g_R$ are symbolic, and so is the matching that produces $g_{\mathrm Y}$.

**It does not compute the heavy neutral or the heavy charged mass beyond tree level.** Threshold corrections at $M_C$ are the effective-potential article's.

**It does not treat the bidoublet as content.** §*The Bidoublet Extension* computes what one would do; the minimal content has none, and the measured $\rho$ excludes it. **A second bidoublet changes nothing about that conclusion**, since it only adds more angles of the same excluded kind.

**It does not treat a $(\mathbf{15},2,2)$ bidoublet.** Its components include colour octets, and a vacuum expectation value in them breaks colour directly; then the colour block is no longer zero and the four-block split is lost. That is a different model, not a correction to this one.

## The Checks

Fourteen recomputations, at tree level, with $v_C=10\,v$ where a numerical value is quoted.

| check | computation | result |
|---|---|---|
| the minimal charged block | two fields, one weak index each | $\operatorname{diag}(\tfrac14g_L^{2}v^{2},\tfrac14g_R^{2}v_{C}^{2})$, off-diagonal $0$ |
| the physical $W$ | eigenvector of a diagonal block | $W_L$ exactly, no $W_R$ admixture |
| $\rho$ in the minimal content | $\tfrac14g_L^{2}v^{2}$ over $\tfrac14(g_L^{2}+g_Y^{2})v^{2}\cos^{2}\theta_W$ | $1$ exactly |
| the two charged masses' ratio | $M_X^{2}/M_{W_R}^{2}$ | $2g_4^{2}/g_R^{2}$ |
| the determinant of the extension | $\det$ of the $2\times2$ | $(\tfrac14g_Lg_R)^{2}(\kappa^{2}-\kappa'^{2})^{2}$ |
| the extension's null direction | $\kappa=\kappa'$ | rank one, $(g_R,-g_L)$, eigenvalue $0$ |
| the extension's eigenvalues | $\beta=0.3$, equal couplings | $0.1088$, $0.3912$, against $\tfrac14(1\mp\sin0.6)$ |
| the extension's mixing angle | eigenvector of $\begin{pmatrix}1&s\\s&1\end{pmatrix}$ | $\pi/4$ for every $s$ |
| the mixing angle off equal couplings | $g_L=1$, $g_R=2$, $\beta=0.3$ | $18.5^{\circ}$, against $\tfrac12\arctan\frac{4\sin0.6}{3}$ |
| the extension's $\rho$ | $\beta=0.1$ | $0.8013$, against $1.00038$ measured |
| the neutral block's eigenvalues | $v_C=10v$ | $0$, $0.3986$, $62.7$ |
| the photon's masslessness | null vector of two independent rank-one terms | $0$ exactly |
| the colour block | $\lvert[g,D]\rvert$ for the eight | $0$ for all eight |
| the block count | $8+6+3+4$ against $9+12$ | $21$ against $21$ |

## Summary

**Four blocks.** Colour $8$, leptoquark $6$, neutral $3$, charged $4$; $8+6+3+4=21$. The split is exact because every vacuum is a colour singlet of definite charge.

**Nine zeros.** Twelve of the twenty-one directions acquire mass — six leptoquarks, two neutral, four charged — so the matrix has rank $12$ and kernel $9$ at the bottom: the eight gluons and the photon. **That is the $9$ of the ledger $21\to12\to9$.**

**The minimal charged block is diagonal.** $M_{W}^{2}=\tfrac14g_L^{2}v^{2}$ and $M_{W_R}^{2}=\tfrac14g_R^{2}v_C^{2}$: no scalar carries both weak indices, so no entry mixes them, so the physical $W$ is $W_L$ and $\rho=1$ exactly at tree level.

**A mixing angle needs a bidoublet, and the bidoublet is excluded.** The extension's determinant is $(\tfrac14g_Lg_R)^{2}(\kappa^{2}-\kappa'^{2})^{2}$, its mixing is $\pi/4$ at equal couplings, and its $\rho=1-\sin2\beta$ is $0.8013=1-\sin0.2$ at $\beta=0.1$ against $1.00038$ measured. **The corpus's charged block is the ledger of content the model does not have.**

## Summary of Notation

| symbol | meaning |
|---|---|
| $W^{\pm}_{L}$, $W^{\pm}_{R}$ | the charged gauge fields of the two weak factors |
| $v$, $v_C$ | the electroweak vacuum and the transition condensate |
| $\mathcal M^{2}_{\pm}$ | the $2\times2$ charged mass matrix |
| $\mathcal M^{2}$ | the $3\times3$ neutral mass matrix |
| $a_1$, $a_2$ | the two neutral vacuum vectors |
| $\kappa$, $\kappa'$ | the bidoublet's two diagonal vevs, in the extension only |
| $\beta$ | $\arctan(\kappa'/\kappa)$, the extension's vacuum direction |
| $\theta_{\pm}$ | the $W_L$–$W_R$ mixing angle, in the extension only |
| $B'$ | the surviving $\mathrm{SU}(4)$ Cartan, $A^{15}$ |

## Further Reading

- [The Breaking of the Primordial Force](the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.html). The colour and leptoquark blocks in full, computed entry by entry.
- [The Neutral Sector: Three Ingredients, Rank Two, One Null Direction](the-neutral-sector-three-ingredients-rank-two-one-null-direction.html). The neutral block's vectors, its Schur complement and its checks.
- [The Scalar Content: One Quartet, One Doublet, Eight Survivors](the-scalar-content-one-quartet-one-doublet-and-eight-survivors.html). Why no field in the minimal content carries both weak indices.
- [The Photon as the Unbroken Mixture: One Null Direction, Three Parents](the-photon-as-the-unbroken-mixture.html). The null vector of the neutral block, derived three ways.
- [Custodial Symmetry and the $\rho$ Parameter](custodial-symmetry-and-the-rho-parameter.html). The relation $\rho=1$ and its radiative corrections.
