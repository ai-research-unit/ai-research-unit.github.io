# __The Mass Matrix of the Twenty-One Gauge Bosons: Four Blocks, One Mixing, and the Nine Zeros__

## Introduction

**The twenty-one gauge directions split into four blocks, and only one of them mixes.** The blocks are eight colour directions, six leptoquark directions, three neutral directions and four charged ones, $8+6+3+4=21$. The first two are already settled at the first breaking, the third has no free angle, and the fourth — the pair $W^{\pm}_{L}$, $W^{\pm}_{R}$ — is the one place in the boson sector where a new angle appears.

**The four blocks are exact and not an approximation.** Each vacuum of the chain is a colour singlet with a definite electric charge, so every mass term carries the colour representation and the charge of both of its generators. Two generators of different colour or different charge therefore never mix, at any order of perturbation theory. The block structure is a statement about the quantum numbers the vacua carry, and it survives every correction that does not break colour or charge.

**What the article computes, and what it borrows.** It derives the charged block from the bidoublet's kinetic term, states its determinant and its two eigenvalues, shows that a massless charged boson needs alignment $\kappa=\kappa'$, and shows that at equal couplings the mixing is maximal. That last result is the reason the Standard Model's $W$ is a mixture of $W_L$ and $W_R$ and not either of them. The colour, leptoquark and neutral blocks are quoted with a pointer to the article that owns each: [The Adjoint Mass Matrix of the Fifteen](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html) for the first two and [Classification of the Bosons](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html) for the third.

**The one sentence worth carrying away.** The neutral block is blind to the ratio $\kappa'/\kappa$ and the charged block is not, so the departure from $\rho=1$ is entirely a charged-block effect:

$$
\rho=\frac{M_{W}^{2}}{M_{Z}^{2}\cos^{2}\theta_W}=1-\sin2\beta,\qquad \tan\beta=\frac{\kappa'}{\kappa},
$$

below $M_R$, at equal couplings, at tree level. That is $\rho-1=-2\kappa\kappa'/(\kappa^{2}+\kappa'^{2})$, which is the form [The Scalar Sector](the-scalar-sector-of-the-four-colours-left-right-model-twenty-four-real-components-twelve-eaten-twelve-surviving.html) states as "proportional to $\kappa\kappa'$", with its coefficient.

## The Four Blocks

**The split.** The twenty-one generator names of the declared copy are sorted by what the three vacua do to them:

| block | generators | colour | charge | scale at which it fills |
|---|---|---|---|---|
| colour | $8$ | $\mathbf8$ | $0$ | never |
| leptoquark | $6$ | $\mathbf3$ and $\bar{\mathbf3}$ | $\pm\tfrac23$ | $M_C$ |
| neutral | $3$ | $\mathbf1$ | $0$ | $M_R$ and $M_W$ |
| charged | $4$ | $\mathbf1$ | $\pm1$ | $M_R$ and $M_W$ |

$8+6+3+4=21$. The charged block counts four real generators because the two complex fields $W^{+}_{L}$ and $W^{+}_{R}$ carry two real components each.

**Why the split is exact.** A mass term is quadratic in two generators and linear in the vacuum that produces it. Every vacuum of the chain is a colour singlet with $Q=0$, so the mass term is invariant under colour and under electric charge, so it vanishes between two generators whose colour representations or charges differ. The blocks are the eigenspaces of (colour representation, $Q$), and no correction that preserves colour and charge can move a mass across them.

**What the split is not.** It is not a statement about the algebra: the four blocks are not subalgebras, and the charged and neutral blocks are not even inside $\mathfrak{su}(4)$ — their generators are the weak ones. The split is a statement about the vacua, and it is the reason each block can be computed on its own.

## The Colour Block: Eight Zeros

**The eight colour directions are massless at every scale, exactly.** Two reasons, and both are exact.

**The first vacuum.** $D=\operatorname{diag}(-3,1,1,1)$ is a multiple of the identity on the colour triple, so every colour generator commutes with it: the colour planes have $\lambda_j=\lambda_k$ and the two colour diagonals commute with it. A generator that commutes with the vacuum has zero mass, which is the kernel statement of [The Adjoint Mass Matrix as the Square of the Roots](the-adjoint-mass-matrix-as-the-square-of-the-roots-two-v-squared-double-commutator-six-planes-and-nine-zeros.html).

**The second and third vacua.** The bidoublet is a colour singlet, so its vacuum expectation value does not couple to a colour generator at all. The same holds for the $(\mathbf4,\mathbf1,\mathbf2)$ scalar, whose vacuum lies along the lepton line, and the lepton line is a colour singlet.

**The consequence.** The $8\times8$ colour block is zero, not small, and colour is unbroken at every step of the chain. This is the matrix statement of the corpus's claim that colour is a stabiliser at every scale.

## The Leptoquark Block: Six at $32v^{2}$

**The six leptoquark directions are the six planes through the lepton line, and they all take the same mass at the first breaking.** In the physics basis the block is $32v^{2}$ times the identity of dimension six:

$$
M^{2}_{\text{lepto}}=32v^{2}\,\mathrm I_{6},\qquad 32=2\cdot4^{2},\qquad 4=1-(-3).
$$

The leakage is the entry-by-entry computation of [The Adjoint Mass Matrix of the Fifteen](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html); the reason is the identity of [The Adjoint Mass Matrix as the Square of the Roots](the-adjoint-mass-matrix-as-the-square-of-the-roots-two-v-squared-double-commutator-six-planes-and-nine-zeros.html), which says that the mass on a plane is twice the square of the vacuum's eigenvalue difference across it. **The six are equal because the vacuum has one lepton line and three equal colour lines**, so all six differences are the same number.

**The later breakings add nothing here.** The bidoublet is colour-blind, and the leptoquarks have already left the unbroken algebra at $M_C$. The block stays $32v^{2}$ at tree level; the one-loop shift is the effective-potential article's.

## The Neutral Block: Rank Two and One Null Direction

**Three fields, two vacuum directions, one null vector.** The neutral block is spanned by $W^{3}_{L}$, $W^{3}_{R}$ and the surviving $\mathrm{SU}(4)$ Cartan $B'$, and each vacuum contributes a rank-one term: one from the $\mathrm{SU}(4)$ vacuum along $a_1=(0,\tfrac12,-\sqrt{\tfrac38})$ with weight $v_R^{2}$, and one from the bidoublet, which is the sum of its two diagonal entries' contributions.

**The ratio $\kappa'/\kappa$ drops out, and this is the exact statement behind "the neutral block has no angle".** The two neutral components of the bidoublet have $(T_{3L},T_{3R})=(+\tfrac12,-\tfrac12)$ and $(-\tfrac12,+\tfrac12)$ — the diagonal entries of a $(1,2,\bar2)$ — so their vacuum vectors are $(\tfrac12,-\tfrac12,0)\kappa$ and $(-\tfrac12,+\tfrac12,0)\kappa'$, which are *parallel*. Their two rank-one terms add to one,

$$
\kappa^{2}\,uu^{\mathsf T}+\kappa'^{2}\,uu^{\mathsf T}=(\kappa^{2}+\kappa'^{2})\,u\,u^{\mathsf T},\qquad u=\bigl(\tfrac12,-\tfrac12,0\bigr),
$$

so the bidoublet enters the neutral block through $\kappa^{2}+\kappa'^{2}=v^{2}$ alone. **The neutral sector sees the size of the bidoublet's vacuum and never its direction.** The coupling-weighted form of the same three-by-three is the classification article's.

**What follows.** The rank is two for every $(\kappa,\kappa')$, so there is exactly one massless neutral — the photon — and its direction is the null vector of the $3\times3$, the vector $(1,1,\sqrt{2/3})$ in the $(T_{3L},T_{3R},T^{15})$ normalisation. The direction is [The Photon as the Unbroken Mixture](the-photon-as-the-unbroken-mixture.html)'s; at $v_R=10v$ the two massive eigenvalues are $0.3994$ and $62.6$ in units of $g^{2}v^{2}$ — the numbers of the classification article — and they do not move when $\kappa'/\kappa$ moves.

**Why the block is nevertheless not free of the second vev.** It is free of the *direction*, and it is not free of the *size*: $v^{2}=\kappa^{2}+\kappa'^{2}$ is the same number for every $\beta$, so the neutral masses are the same at every $\beta$. That is exactly why the departure from $\rho=1$ has to come from somewhere else.

## The Charged Block

**The fields and the vacuum.** The charged block is spanned by $W^{+}_{L}$ and $W^{+}_{R}$, with $W^{\pm}=(W^{1}\mp iW^{2})/\sqrt2$. The bidoublet's vacuum is

$$
\langle H\rangle=\begin{pmatrix}\kappa&0\\0&\kappa'\end{pmatrix},\qquad v^{2}=\kappa^{2}+\kappa'^{2},
$$

with the two diagonal entries neutral and the two off-diagonal entries charged, and with the convention that fixes the charge assignments of [The Scalar Sector](the-scalar-sector-of-the-four-colours-left-right-model-twenty-four-real-components-twelve-eaten-twelve-surviving.html).

**The covariant derivative.** With the right factor acting by $\Phi\mapsto\Phi\,\sigma_a^{\mathsf T}/2$, which is the convention in which both diagonal entries are neutral,

$$
D_\mu H=\partial_\mu H-i g_L\frac{\sigma_a}{2}W^{a}_{L\mu}H+i g_R H\frac{\sigma_a^{\mathsf T}}{2}W^{a}_{R\mu}.
$$

Separating the charged components at the vacuum, the two off-diagonal entries are

$$
(D_\mu H)_{12}=-\frac{i}{\sqrt2}g_L\kappa'\,W^{+}_{L}+\frac{i}{\sqrt2}g_R\kappa\,W^{-}_{R},\qquad
(D_\mu H)_{21}=-\frac{i}{\sqrt2}g_L\kappa\,W^{-}_{L}+\frac{i}{\sqrt2}g_R\kappa'\,W^{+}_{R}.
$$

**The mass term.** With the kinetic term $\tfrac12\operatorname{tr}\bigl[(D_\mu H)^{\dagger}(D_\mu H)\bigr]$ and $\operatorname{tr}$ in the bidoublet's two indices,

$$
\mathcal L\supset\tfrac14 g_L^{2}v^{2}\lvert W_{L}\rvert^{2}+\tfrac14 g_R^{2}v^{2}\lvert W_{R}\rvert^{2}\pm g_Lg_R\kappa\kappa'\,\mathrm{Re}\bigl(W_{L}W_{R}\bigr),
$$

so the block is

$$
\mathcal M^{2}_{\pm}=\frac14\begin{pmatrix}g_L^{2}v^{2}&\pm2g_Lg_R\kappa\kappa'\\ \pm2g_Lg_R\kappa\kappa'&g_R^{2}v^{2}\end{pmatrix}.
$$

**The sign of the off-diagonal is a convention and no eigenvalue depends on it.** It is the relative phase of $W^{+}_{L}$ and $W^{+}_{R}$, which a redefinition $W^{+}_{R}\mapsto-W^{+}_{R}$ removes; a computation with the other sign for the right action, $\Phi\mapsto g_R\Phi$, gives the opposite sign and the same spectrum. Everything below is stated for the magnitude.

**The Standard Model limit.** Set $\kappa'=0$ and $g_L=g_R=g$. The block is $\tfrac14g^{2}v^{2}$ times the identity: two degenerate charged bosons of squared mass $\tfrac14g^{2}v^{2}$, which is the corpus's $W$ mass squared. **Alignment reproduces the Standard Model's charged mass and, as the neutral block shows, its neutral masses too.**

## The Determinant, the Eigenvalues and Alignment

**The determinant.** For a $2\times2$ block $\begin{pmatrix}A&C\\C&B\end{pmatrix}$,

$$
\det\mathcal M^{2}_{\pm}=\frac{g_L^{2}g_R^{2}}{16}\bigl[(v^{2})^{2}-4\kappa^{2}\kappa'^{2}\bigr]=\Bigl(\frac{g_Lg_R}{4}\Bigr)^{2}\bigl(\kappa^{2}-\kappa'^{2}\bigr)^{2}\ \ge 0 .
$$

**Alignment is the only way to a massless charged boson.** The determinant vanishes exactly when $\kappa=\kappa'$. At that point the two diagonal entries and the off-diagonal are equal in magnitude and the block is rank one:

$$
\mathcal M^{2}_{\pm}\Big|_{\kappa=\kappa'}=\frac14\begin{pmatrix}g_L^{2}&g_Lg_R\\ g_Lg_R&g_R^{2}\end{pmatrix}\kappa^{2}\cdot2 ,
$$

with null vector $(g_R,-g_L)$. **A massless charged boson is a physical catastrophe, so this is a bound on the scalar sector and not a curiosity**: whatever the vacuum is, $\kappa\neq\kappa'$.

**The eigenvalues.** For the general block,

$$
M^{2}_{\pm}=\tfrac18\bigl(g_L^{2}+g_R^{2}\bigr)v^{2}\pm\tfrac12\sqrt{\tfrac1{16}\bigl(g_L^{2}-g_R^{2}\bigr)^{2}v^{4}+g_L^{2}g_R^{2}\kappa^{2}\kappa'^{2}} .
$$

At equal couplings this collapses to one line:

$$
M^{2}_{\pm}=\tfrac14g^{2}v^{2}\bigl(1\mp\sin2\beta\bigr),\qquad \tan\beta=\frac{\kappa'}{\kappa},\qquad \kappa^{2}+\kappa'^{2}=v^{2}.
$$

**The light one is the Standard Model's $W$ and the heavy one is the $W_R$ partner.** At $\beta=0$ they are degenerate; at $\beta=0.3$ they are $0.1088\,g^{2}v^{2}$ and $0.3912\,g^{2}v^{2}$; at $\beta=\pi/4$ the light one is exactly zero.

**The mixing angle.** For the same block,

$$
\tan2\theta_{\pm}=\frac{2\mathcal M^{2}_{LR}}{\mathcal M^{2}_{LL}-\mathcal M^{2}_{RR}}
=\pm\frac{2g_Lg_R\sin2\beta}{g_L^{2}-g_R^{2}} .
$$

**At equal couplings the mixing is maximal for every alignment.** The denominator vanishes, the block is $\tfrac14g^{2}v^{2}$ times $\begin{pmatrix}1&\sin2\beta\\ \sin2\beta&1\end{pmatrix}$, and its eigenvectors are $(1,1)/\sqrt2$ and $(1,-1)/\sqrt2$ at every $\beta$. So the physical charged bosons are

$$
W_{1}=\frac{W_{L}+W_{R}}{\sqrt2},\qquad W_{2}=\frac{W_{L}-W_{R}}{\sqrt2},
$$

independently of the vacuum direction, with squared masses $\tfrac14g^{2}v^{2}(1\mp\sin2\beta)$. **The Standard Model's $W$ is half $W_L$ and half $W_R$.** That is the sharpest consequence of the block: at equal couplings the left–right mixing angle is not a small parameter but $\pi/4$, and what is small is the squared-mass splitting, $\propto\sin2\beta$.

**And the mixing vanishes only when a coupling does.** For $g_L\neq g_R$ the angle is small in proportion to $\sin2\beta$, and it vanishes at alignment. So "small $W_L$–$W_R$ mixing" is a statement about two things at once: a coupling splitting and a vacuum alignment.

## The $\rho$ Parameter Below $M_R$

**The two squared masses, side by side.** The light charged one carries the alignment factor and the light neutral one does not:

$$
M_{W}^{2}=\tfrac14g^{2}v^{2}\bigl(1-\sin2\beta\bigr),\qquad
M_{Z}^{2}=\tfrac14\bigl(g^{2}+g_{\mathrm Y}^{2}\bigr)v^{2},
\qquad
\cos^{2}\theta_W=\frac{g^{2}}{g^{2}+g_{\mathrm Y}^{2}} .
$$

**The ratio.** Substituting,

$$
\rho=\frac{M_{W}^{2}}{M_{Z}^{2}\cos^{2}\theta_W}
=\frac{\tfrac14g^{2}v^{2}(1-\sin2\beta)}{\tfrac14(g^{2}+g_{\mathrm Y}^{2})v^{2}\cdot\dfrac{g^{2}}{g^{2}+g_{\mathrm Y}^{2}}}
=1-\sin2\beta .
$$

**Why the departure sits entirely in the charged block.** The neutral block is blind to $\beta$ (§*The Neutral Block: Rank Two and One Null Direction*), so $M_Z$ is the Standard Model's; the charged block is not, so $M_W$ is smaller by $(1-\sin2\beta)$. **The custodial violation of this model is a charged-block phenomenon**, which is the matrix form of the statement that the two diagonal vevs give the same neutral vector and different charged ones.

**The numbers.** At $\beta=0.1$ the ratio at $v/v_R=10^{-1}$ is $0.8026$, and in the limit $v/v_R\to0$ it is $0.8013=1-\sin0.2$. At $\beta=0.3$ it is $0.436$. The measured value is $1.00038\pm0.00020$, so $\sin2\beta$ is bounded to be small — the same bound that [The Scalar Sector](the-scalar-sector-of-the-four-colours-left-right-model-twenty-four-real-components-twelve-eaten-twelve-surviving.html) states as "$\kappa\kappa'$ small", now with its coefficient.

**What this $\rho$ is not.** It is not the loop-level $\rho$. The tree-level relation above is the one the custodial symmetry of [Custodial Symmetry and the $\rho$ Parameter](custodial-symmetry-and-the-rho-parameter.html) protects; the radiative corrections are that article's, and the comparison with the measured number needs the top mass and the hypercharge running, which the framework does not supply here.

## The Count in Blocks

**Two counts, one block structure.** The blocks give both the massless and the massive count without a second ledger:

$$
\underbrace{8}_{\text{colour}}+\underbrace{1}_{\text{photon}}=9\ \text{massless},\qquad
\underbrace{6}_{\text{leptoquark}}+\underbrace{2}_{\text{neutral}}+\underbrace{4}_{\text{charged}}=12\ \text{massive}.
$$

**The nine.** The colour eight stay massless forever and the photon is a null direction of the neutral block, so the two zeros have two different reasons: one is a stabiliser of the vacuum and the other is an eigenvector of the neutral block.

**The twelve.** Six fill at $M_C$, and the six weak directions fill in two steps: the $W^{\pm}_{R}$ pair and the $Z_R$ at $M_R$, the $W^{\pm}_{L}$ pair and the $Z$ at $M_W$. **The block structure and the chain agree step by step**, which is the check that the four blocks are the right decomposition and not an arbitrary one.

## What the Article Does Not Do

**It does not fix a coupling.** Both $g_L$ and $g_R$ are symbolic, and so is the matching that produces $g_{\mathrm Y}$.

**It does not compute the heavy neutral or the heavy charged mass beyond tree level.** Threshold corrections at $M_R$ are the effective-potential article's.

**It does not treat a second bidoublet.** A second $(1,2,2)$ makes the two diagonal vevs of the two fields independent, and the charged block becomes $2\times2$ per field pair with more than one angle; the block structure survives and the alignment condition becomes a condition on the sum of the products.

**It does not treat a $(\mathbf{15},2,2)$ bidoublet.** Its components include colour octets, and a vacuum expectation value in them breaks colour directly; then the colour block is no longer zero and the four-block split is lost. That is a different model, not a correction to this one.

## The Checks

Fourteen recomputations, at tree level, with $v^{2}=\kappa^{2}+\kappa'^{2}$ and $v_R=10\,v$ where a numerical value is quoted.

| check | computation | result |
|---|---|---|
| the Standard Model limit | $\kappa'=0$, $g_L=g_R$ | $\tfrac14g^{2}v^{2}$ twice |
| the determinant | $\det$ of the $2\times2$ | $(\tfrac14g_Lg_R)^{2}(\kappa^{2}-\kappa'^{2})^{2}$ |
| the null direction | $\kappa=\kappa'$ | rank one, $(g_R,-g_L)$, eigenvalue $0$ |
| the eigenvalues at equal couplings | $\beta=0.3$ | $0.1088$, $0.3912$, against $\tfrac14(1\mp\sin0.6)$ |
| the mixing angle at equal couplings | eigenvector of $\begin{pmatrix}1&s\\s&1\end{pmatrix}$ | $\pi/4$ for every $s$ |
| the mixing angle off equal couplings | $g_L=1$, $g_R=2$, $\beta=0.3$ | $18.5^{\circ}$, against $\tfrac12\arctan\frac{4\sin0.6}{3}$ |
| the trace of the charged block | $\tfrac14(g_L^{2}+g_R^{2})v^{2}$ | $\tfrac12g^{2}v^{2}$ at equal couplings |
| the neutral block's eigenvalues | $\beta=0$, $0.1$, $0.3$ | $0$, $0.3994$, $62.6$ at every $\beta$ |
| the photon's masslessness | null vector for every $\beta$ | $0$ exactly |
| $\rho$ at $\beta=0.1$ | $v/v_R=10^{-1}$ | $0.8026$ |
| $\rho$ in the limit | $v/v_R\to0$ | $0.8013=1-\sin0.2$ |
| the colour block | $\lvert[g,D]\rvert$ for the eight | $0$ for all eight |
| the leptoquark block | from the double-commutator identity | $32v^{2}$ six times |
| the block count | $8+6+3+4$ against $9+12$ | $21$ against $21$ |

## Summary

**Four blocks.** Colour $8$, leptoquark $6$, neutral $3$, charged $4$; $8+6+3+4=21$. The split is exact because every vacuum is a colour singlet of definite charge.

**One mixing.** The charged block is $\tfrac14\begin{pmatrix}g_L^{2}v^{2}&\pm2g_Lg_R\kappa\kappa'\\ \pm2g_Lg_R\kappa\kappa'&g_R^{2}v^{2}\end{pmatrix}$; its determinant is $(\tfrac14g_Lg_R)^{2}(\kappa^{2}-\kappa'^{2})^{2}$, so a massless charged boson needs $\kappa=\kappa'$ and alignment is a bound.

**One angle, and it is maximal.** At equal couplings the mixing is $\pi/4$ for every vacuum direction: the physical charged bosons are $(W_L\pm W_R)/\sqrt2$, and what is small is the squared-mass splitting $\tfrac14g^{2}v^{2}\sin2\beta$.

**The departure from $\rho=1$ is a charged-block effect.** The neutral block is blind to $\kappa'/\kappa$, so $\rho=1-\sin2\beta=1-2\kappa\kappa'/(\kappa^{2}+\kappa'^{2})$ below $M_R$, at equal couplings.

## Summary of Notation

| symbol | meaning |
|---|---|
| $W^{\pm}_{L}$, $W^{\pm}_{R}$ | the charged gauge fields of the two weak factors |
| $\kappa$, $\kappa'$ | the two diagonal vacuum expectation values of the bidoublet |
| $v^{2}=\kappa^{2}+\kappa'^{2}$ | the electroweak vacuum, squared |
| $\beta$ | $\arctan(\kappa'/\kappa)$, the vacuum's direction |
| $\mathcal M^{2}_{\pm}$ | the $2\times2$ charged mass matrix |
| $\mathcal M^{2}$ | the $3\times3$ neutral mass matrix |
| $\theta_{\pm}$ | the $W_L$–$W_R$ mixing angle |
| $B'$ | the surviving $\mathrm{SU}(4)$ Cartan, $A^{15}$ |

## Further Reading

- [The Adjoint Mass Matrix of the Fifteen: One Number per Plane, $32v^2$ on Six and Zero on Nine](the-adjoint-mass-matrix-of-the-fifteen-one-number-per-plane.html). The colour and leptoquark blocks in full, computed entry by entry.
- [The Adjoint Mass Matrix as the Square of the Roots](the-adjoint-mass-matrix-as-the-square-of-the-roots-two-v-squared-double-commutator-six-planes-and-nine-zeros.html). Why the leptoquark block is a multiple of the identity, and why the colour block is exactly zero.
- [Classification of the Bosons in the Four Colours Left–Right Model](classification-of-the-bosons-in-the-four-colours-left-right-model-twenty-four-cells-twenty-one-generators-nine-massless-and-twelve-massive.html). The neutral block's entries and eigenvalues, and the ledger of the spectrum.
- [The Photon as the Unbroken Mixture: One Null Direction, Three Parents](the-photon-as-the-unbroken-mixture.html). The null vector of the neutral block, derived three ways.
- [The Scalar Sector of the Four Colours Left–Right Model](the-scalar-sector-of-the-four-colours-left-right-model-twenty-four-real-components-twelve-eaten-twelve-surviving.html). The bidoublet, its two diagonal vevs, and the statement that $\rho-1\propto\kappa\kappa'$.
- [Custodial Symmetry and the $\rho$ Parameter](custodial-symmetry-and-the-rho-parameter.html). The relation $\rho=1$ and its radiative corrections.
