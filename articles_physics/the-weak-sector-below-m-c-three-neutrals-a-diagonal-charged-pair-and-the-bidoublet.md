# __The Weak Sector Below $M_C$: Three Neutrals of Rank Two, a Diagonal Charged Pair, and the Bidoublet That Would Mix Them__

## Introduction

**The question.** Seven weak vector fields stand below the transition under five names: three neutral, $W^3_L$, $W^3_R$ and $B'$, and two charged pairs, $W^{+}_{L}$ with $W^{-}_{L}$ and $W^{+}_{R}$ with $W^{-}_{R}$, each pair one complex field. Two
vacua act on them. How many bosons survive, what are their masses, and is there any mixing?

**The answer, in one line per half.** The neutral half is a $3\times3$ matrix of rank two, so it leaves one null direction — the photon — and two masses,
$\tfrac25g^2v^2$ and $\tfrac58g^2v_C^2$. The charged half is diagonal, because each of the two vacua carries one weak index and no field carries both:
$M_W^2=\tfrac14g_L^2v^2$ and $M_{W_R}^2=\tfrac14g_R^2v_C^2$.

**And the two halves are one article because they meet in one number.** $\rho=M_W^2/(M_Z^2\cos^2\theta_W)$ is a ratio across the two blocks, and it is
exactly $1$ at tree level for the same reason both blocks are simple: no scalar in the content carries both weak indices. **A mixing angle is what would
break that, and the bidoublet that would supply one is computed in §*The Bidoublet Extension* and excluded by the measured $\rho$.**

**What this article is, and what it is not.** It is the weak half of [Classification of the
Bosons](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html), cut out so that the grid article stays
about the grid. **It is not part of the model's gauge content.** The model fixing conditions fifteen directions, all of them $\mathfrak{su}(4)$ (*The Mass Matrix of
the Fifteen Connections*); six of the seven fields here arrive at $M_C$ with the doublet index of the condensate (*Rank Five From Three*) and are counted
from there down.

## What Arrives, and Why It Is Not in the Group

**Above the transition there is one factor and no weak field.** The algebra is $\mathfrak{su}(4)$, of rank three and dimension fifteen. **Below it the
weak sector is seven real vector fields, and six of them arrive**: the doublet index supplies two triples, $W_L$ and $W_R$, and the seventh is $B'$, the
model's own fifteenth Cartan, which was there all along. **None of the six is a generator of the model; $B'$ is.**

**Three neutral, and why exactly three.** Neutral connections are those with $Q=0$: $W^3_L$, $W^3_R$, and the $\mathrm{SU}(4)$ Cartan direction that
survives the first breaking. The other two $\mathrm{SU}(4)$ Cartans, $T^{c}_{3}$ and $T^{c}_{8}$, are neutral but are colour and never mix with anything,
because colour is unbroken. So the mixing sector is exactly three fields:

$$
\{W^3_L,\ W^3_R,\ B'\},\qquad B'\equiv A^{15}.
$$

All three are connections, and none of them is one of the scalar sector's neutral states.

**Two charged.** $W^{+}_{L}$ and $W^{+}_{R}$, one complex field for each weak factor, four real components in all.

**The dimension of the neutral sector.** It is three-dimensional from the first breaking onward, and it stays three-dimensional until the last. **Before
that breaking it is one-dimensional**: the only neutral direction among the surviving Cartans is the corner $B'$, and the weak Cartans do not exist yet.

## The Neutral Matrix: Three Fields, Rank Two

**Why they mix.** Each of the two vacua is annihilated by a different combination. The first vacuum, along the unit line, is annihilated by
$Y=T_{3R}+\tfrac12(B-L)$; the second, along the doublet direction, by $Q=T_{3L}+Y$. Two conditions on three fields leave exactly one direction, and that
direction is the photon. That is the whole of the neutral sector in one sentence.

**The matrix.** With the two vacuum vectors $a_1,a_2\in\mathbb R^3$ written in the basis of couplings,

$$
\mathcal M^2=v_C^2\,a_1a_1^{\mathsf T}+v^2\,a_2a_2^{\mathsf T},
\qquad
a_1=\bigl(0,\tfrac12,-\sqrt{\tfrac38}\bigr),
\qquad
a_2=\bigl(-\tfrac12,0,\sqrt{\tfrac38}\bigr),
$$

where the entries are the eigenvalues of $(T_{3L},\,T_{3R},\,T^{15})$ on the field that takes the vev, with $T^{15}$ the Cartan normalised by
$\operatorname{tr}(T^{15})^{2}=\tfrac12$ and hence $B-L=\sqrt{8/3}\,T^{15}$. So $a_1$ is the lepton line — $T_{3R}=+\tfrac12$, $B-L=-1$, hence
$T^{15}=-\sqrt{3/8}$ — and $a_2$ is the lower component of the electroweak doublet $H$ — $T_{3L}=-\tfrac12$, $T_{3R}=0$, $B-L=+1$, hence
$T^{15}=+\sqrt{3/8}$. Two annihilations fix the relative signs. Hypercharge is unbroken on the first vacuum, $Y=T_{3R}+\tfrac12(B-L)=0$, and both vacua
must leave the photon massless, $Q=T_{3L}+T_{3R}+\tfrac12(B-L)$, which in this normalisation is the vector $(1,1,\sqrt{2/3})$: it gives
$0+\tfrac12+\sqrt{2/3}\cdot(-\sqrt{3/8})=0$ on $a_1$ and $-\tfrac12+0+\sqrt{2/3}\cdot\sqrt{3/8}=0$ on $a_2$. **The two vectors are antiparallel in their
$B-L$ components and parallel in nothing else, which is why they stay independent and the rank stays two.** Only the products $a_ia_i^{\mathsf T}$ enter
$\mathcal M^2$, so the overall sign of each $a_i$ is free; the relative signs are not, and the two tests above are what fixes them.

**The rank.** $\mathcal M^2$ is a sum of two rank-one matrices, so its rank is at most two, so it has at least one zero eigenvalue. It has exactly one,
because $a_1$ and $a_2$ are independent: $a_1\cdot a_2=-\tfrac38v_Cv\ne0$ and they are not parallel. So there is one massless neutral and two massive,
always, for any two independent neutral vacua. **A frame with two neutral vacua and no massless neutral would violate this, and that is the structural
reason the photon is not optional.**

## The Photon, Which Is a Mixture and Not a Factor

**Not a connection.** The unbroken abelian factor at the end of the chain is generated by $B'$, the fifteenth $\mathrm{SU}(4)$ Cartan. The photon is not
$B'$. It is the combination of $W_L^3$, $W_R^3$ and $B'$ that annihilates both neutral vacua, and its coefficients are the null vector of the neutral mass
matrix:

$$
a_1\times a_2\ \propto\ \bigl(\sqrt{\tfrac38},\ \sqrt{\tfrac38},\ \tfrac12\bigr)
\qquad\Longrightarrow\qquad
A_{\imath}\ \propto\ W^3_{L\imath}+W^3_{R\imath}+\sqrt{\tfrac23}\,B'_{\imath} .
$$

The coefficients are $(1,\,1,\,\sqrt{2/3})$ up to an overall sign that no measurement can fix. **The third component is fixed by the normalisation of
$T^{15}$ and by nothing dynamical.** It is the fifteenth Cartan's value on the unit line, and the same choice $\operatorname{tr}(T^{15})^2=\tfrac12$ is
what writes $B-L$ proportional to $(-1,\tfrac13,\tfrac13,\tfrac13)$.

**Why it holds for any couplings.** The two vacua annihilate two different combinations of the three neutral generators, so the requirement that one
combination survives both gives one null direction. That is a rank statement about a sum of two rank-one matrices, so the mixing pattern is fixed and only
the numerical size of each coefficient moves with the couplings.

**Where the rest is.** This article states the direction; it does not state the angle that follows from it. [The Photon as the Unbroken Mixture: One Null
Direction, Three Parents](the-photon-as-the-unbroken-mixture.html) derives the direction three ways and shows it to be the coefficient vector of $Q$; the
angle is [The Weinberg Angle and the Three Neutral States](the-weinberg-angle-and-the-three-neutral-states.html)'s.

## The Two Massive Neutrals

**Both eigenvalues.** Exactly, in the minimal vacuum.

**The light neutral.** It lands on the Standard Model relation.

$$
M_Z^2=\tfrac14\bigl(g_L^2+g_Y^2\bigr)v^2 .
$$

At equal couplings, with $g_Y^2=\tfrac35g^2$ from the matching relation, the predicted value is $\tfrac14(g_L^2+g_Y^2)v^2=\tfrac25g^2v^2$, and the light
eigenvalue of $\mathcal M^2$ is $0.4\,g^2v^2$. The two are the same number, and that is the check: the normalisations entering $a_1$ and $a_2$ reproduce
the Standard Model's relation $M_Z^2=\tfrac14(g_L^2+g_Y^2)v^2$ and not merely its group. The agreement is the leading term in $v/v_C$ — the eigenvalue is
$0.3986\,g^2v^2$ at $v/v_C=10^{-1}$ — which is the sense in which the Standard Model is recovered below $M_C$, at tree level.

**The heavy neutral.** Its coefficient is $\tfrac58$.

$$
M_{Z_R}^2=\tfrac58\,g^2v_C^2 .
$$

The heavy eigenvalue at $v\to0$ is $0.625\,g^2v_C^2=\tfrac58g^2v_C^2$, and the $\tfrac58$ is nothing but $|a_1|^2=\tfrac14+\tfrac38$: one quarter from
$T_{3R}$ and three eighths from the $B-L$ normalisation. At $v=0$ the matrix is rank one, so the other two eigenvalues vanish there: the $Z_R$ mass is
entirely $M_C$'s, and the light neutral's comes entirely from $v$. The $Z_R$ is therefore heavier than the $W_R$ by the ratio of the two coefficients,
$\sqrt{(5/8)/(1/4)}=\sqrt{5/2}\simeq1.58$ at equal couplings; with the couplings split the squared ratio is $1+\tfrac32(g_4/g_R)^2$, which carries
$g_4/g_R$ and is the coupling article's business.

**What these two numbers are.** They are the vacuum's and not the couplings'. The coefficient is fixed by which component of which multiplet takes the vev,
the normalisation of that vev is the scalar sector's business, and the overall size is the coupling article's.

## The Charged Block: Two Fields, Two Vacua, No Off-Diagonal

**The fields and the vacua.** The charged block is spanned by $W^{+}_{L}$ and $W^{+}_{R}$. It is fed by two fields, each with one weak index: $H$ is a left
doublet and a right singlet, and $Ξ$ is the reverse. **So each field gives a mass to its own pair and to nothing else**, and no operator connects $W_L$
to $W_R$ at tree level.

**The two masses.** With $\langle H\rangle$ along the lower component and $\langleΞ\rangle$ along the lepton line of the right doublet,

$$
(D_\mu H)^{\dagger}(D_\mu H)\supset\tfrac14g_L^{2}v^{2}\,W^{+}_{L}W^{-}_{L},
\qquad
(D_\muΞ)^{\dagger}(D_\muΞ)\supset\tfrac14g_R^{2}v_C^{2}\,W^{+}_{R}W^{-}_{R},
$$

and the block is diagonal:

$$
\mathcal M^{2}_{\pm}=\frac14\begin{pmatrix}g_L^{2}v^{2}&0\\0&g_R^{2}v_C^{2}\end{pmatrix}.
$$

**The diagonality is not an assumption about the numbers; it is the statement that no scalar in the content carries both indices.** The two
fields, the ten survivors and the reason no field carries both weak indices are [The Scalar
Content](the-scalar-content-one-matrix-and-ten-survivors.html)'s.

## What the Two Halves Say Together

**The physical $W$ is $W_L$, exactly.** The eigenvectors of a diagonal matrix are the unit vectors, so no admixture of $W_R$ survives in the light state at
tree level. **The observed $W$ couples purely left-handedly, and this block says the same thing algebraically.**

**$\rho=1$ exactly.** $M_Z^{2}=\tfrac14\bigl(g_L^{2}+g_Y^{2}\bigr)v^{2}$ from the neutral half, so the ratio is $1$ at tree level with no correction to
absorb:

$$
\rho=\frac{M_{W}^{2}}{M_{Z}^{2}\cos^{2}\theta_W}=1 .
$$

**The departure from $1$ needs a scalar with both weak indices, and the measured value $1.00038\pm0.00020$ says the mixing is at most of order
$10^{-4}$.** That is a statement about the content, not a tuning.

**The two charged masses' ratio is the leptoquark ratio.** Because the sextet and the right pair are the two indices of one field at one scale,

$$
\frac{M_X^{2}}{M_{W_R}^{2}}=\frac{2g_4^{2}}{g_R^{2}},
$$

with the $\sqrt2$ belonging to the group and the ratio free. **The ratio is a test of the arrival, not a prediction of a number.**

## The Bidoublet Extension

**Why it is here, and what it is.** A scalar in $(\mathbf1,\mathbf2,\mathbf2)$ carries both weak indices, so its vacuum can mix the two charged pairs and
move $\rho$. **The minimal content has no such field; the section is the ledger of what adding one would cost.**

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

**The sign of the off-diagonal is a convention and no eigenvalue depends on it.** It is the relative phase of $W^{+}_{L}$ and $W^{+}_{R}$, which a
redefinition removes.

**The determinant, and why alignment is a bound.** For a $2\times2$ block $\begin{pmatrix}A&C\\C&B\end{pmatrix}$,

$$
\det\mathcal M^{2}_{\pm}=\frac{g_L^{2}g_R^{2}}{16}\bigl[(v^{2})^{2}-4\kappa^{2}\kappa'^{2}\bigr]
=\Bigl(\frac{g_Lg_R}{4}\Bigr)^{2}\bigl(\kappa^{2}-\kappa'^{2}\bigr)^{2}\ \ge 0 ,
$$

so the determinant vanishes exactly when $\kappa=\kappa'$ and the block is then rank one with null vector $(g_R,-g_L)$. **A massless charged boson is a
physical catastrophe, so whatever the vacuum is, $\kappa\neq\kappa'$.**

**The eigenvalues and the two physical states.** At equal couplings,

$$
M^{2}_{\pm}=\tfrac14g^{2}v^{2}\bigl(1\mp\sin2\beta\bigr),\qquad \tan\beta=\frac{\kappa'}{\kappa},\qquad \kappa^{2}+\kappa'^{2}=v^{2},
$$

and the eigenvectors are $(1,1)/\sqrt2$ and $(1,-1)/\sqrt2$ at every $\beta$. **So the extension predicts a $W$ that is half $W_L$ and half $W_R$, with
mixing angle $\pi/4$ at equal couplings and a splitting $\propto\sin2\beta$.**

**And that is why the minimal content has none of it.** A half-right-handed $W$ is excluded by the charged-current couplings, and the same block moves
$\rho$:

$$
\rho=\frac{M_{W}^{2}}{M_{Z}^{2}\cos^{2}\theta_W}=1-\sin2\beta ,
$$

which at $\beta=0.1$ is $0.8013=1-\sin0.2$ against a measured $1.00038\pm0.00020$. **The measurement reads it as $\tan\beta=-(1.9\pm1.0)\times10^{-4}$: the
mixing must vanish to four orders.** A bidoublet is therefore not a variant of the minimal content but a different model.

## What the Extension Does Not Touch

**The determinant identity, the alignment bound and the $\pi/4$ result are correct for the theory they describe.** They describe a theory with a
bidoublet; the corpus's content has none.

**A second bidoublet changes nothing about that conclusion.** It adds more angles of the same excluded kind.

**A $(\mathbf{15},\mathbf2,\mathbf2)$ bidoublet is a different model again.** Its components include colour octets, and a vacuum expectation value in them
breaks colour directly; then the colour block is no longer zero and the model's two-block split is lost.

## What the Article Does Not Do

**It does not fix a coupling.** $g_L$, $g_R$ and $g_Y$ are symbolic, and so is the matching that produces $g_Y$.

**It does not compute the masses beyond tree level.** Threshold corrections at $M_C$ are the effective-potential article's.

**It does not derive the weak factors.** That they arrive with the doublet index rather than emerge from the breaking is [Rank Five From
Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html)'s one postulate, and this article uses it.

**It does not claim these seven vectors are generators of the model.** They are not: the fifteen are nine massless and six at $32v_C^2$, and every field
here is counted below the transition.

## The Checks

Eighteen recomputations, at tree level, with $v_C=10\,v$ where a numerical value is quoted.

| check | computation | result |
|---|---|---|
| the two neutral vacuum vectors | $\lvert a_1\rvert^2=\tfrac58$, $\lvert a_2\rvert^2=\tfrac58$, $a_1\cdot a_2=-\tfrac38$ | both lengths $\sqrt{5/8}$ |
| the neutral rank | $a_1\cdot a_2\ne0$, two independent rank-one terms | rank exactly two |
| the neutral determinant | $0$ for every $v$ and $v_C$ | one null direction and no more |
| the null direction | $a_1\times a_2=\tfrac{\sqrt6}{8}\bigl(1,1,\sqrt{\tfrac23}\bigr)$ | the photon is $\bigl(1,1,\sqrt{\tfrac23}\bigr)$ |
| $Q$ on the two neutral vacua | $(1,1,\sqrt{2/3})\cdot a_1$ and $(1,1,\sqrt{2/3})\cdot a_2$ | $0$ and $0$ |
| the heavy neutral coefficient | $\lvert a_1\rvert^2=\tfrac14+\tfrac38$ | $\tfrac58$ |
| the light neutral coefficient | $\lvert a_2\rvert^2-(a_1\cdot a_2)^2/\lvert a_1\rvert^2=\tfrac58-\tfrac9{40}$ | $\tfrac25$ |
| the neutral eigenvalues | $v_C=10\,v$ | $0$, $0.3986$, $62.7$ in $g^2v^2$ |
| the neutral eigenvalues, small $v$ | $v=0.3$, $v_C=1$ | $0.03481$, $0.64644$, against $0.036$, $0.625$ |
| the $Z_R/Z$ ratio | $\sqrt{(5/8)/(1/4)}$ | $1.5811$ at equal couplings |
| the minimal charged block | two fields, one weak index each | $\operatorname{diag}(\tfrac14g_L^{2}v^{2},\tfrac14g_R^{2}v_{C}^{2})$, off-diagonal $0$ |
| the physical $W$ | eigenvector of a diagonal block | $W_L$ exactly, no $W_R$ admixture |
| $\rho$ in the minimal content | $\tfrac14g_L^{2}v^{2}$ over $\tfrac14(g_L^{2}+g_Y^{2})v^{2}\cos^{2}\theta_W$ | $1$ exactly |
| the charged mass ratio | $M_X^{2}/M_{W_R}^{2}$ | $2g_4^{2}/g_R^{2}$ |
| the extension's determinant | $\det$ of the $2\times2$ | $(\tfrac14g_Lg_R)^{2}(\kappa^{2}-\kappa'^{2})^{2}$ |
| the extension's null direction | $\kappa=\kappa'$ | rank one, $(g_R,-g_L)$, eigenvalue $0$ |
| the extension's eigenvalues | $\beta=0.3$, equal couplings | $0.1088$, $0.3912$, against $\tfrac14(1\mp\sin0.6)$ |
| the extension's mixing and $\rho$ | eigenvector of $\begin{pmatrix}1&s\\s&1\end{pmatrix}$, $\beta=0.1$ | $\pi/4$ for every $s$; $\rho=0.8013$ |

## Summary

**Neutral: three fields, rank two, one null direction, two masses.** The rank is two because there are two vacua and each contributes one rank-one term.
The null direction is the cross product of the two vacuum vectors, so its coefficients are fixed by the normalisation of the fifteenth Cartan and by
nothing dynamical. The two masses are norms and overlaps of the same two vectors, $\tfrac25g^2v^2$ light and $\tfrac58g^2v_C^2$ heavy.

**Charged: two fields, one weak index each, no off-diagonal.** $M_{W}^{2}=\tfrac14g_L^{2}v^{2}$ and $M_{W_R}^{2}=\tfrac14g_R^{2}v_C^{2}$, so the physical
$W$ is $W_L$ and $\rho=1$ exactly at tree level.

**The two halves are joined by $\rho$.** It is a ratio across the two blocks, and it is $1$ for the single reason both blocks are simple: no scalar
carries both weak indices.

**A mixing angle needs a bidoublet, and the bidoublet is excluded.** The extension's determinant is $(\tfrac14g_Lg_R)^{2}(\kappa^{2}-\kappa'^{2})^{2}$, its
mixing is $\pi/4$ at equal couplings, and its $\rho=1-\sin2\beta$ is $0.8013$ at $\beta=0.1$ against $1.00038$ measured. **The extension is the ledger of
content the model does not have.**

**Seven vectors below the transition under five names, six of them arriving.** The fifteen are nine massless and six at $32v_C^{2}$; the weak sector is
what the doublet index supplies plus $B'$, counted from $M_C$ down.

## Summary of Notation

| symbol | what it is |
| --- | --- |
| $W^3_L$, $W^3_R$ | the two neutral weak redundant directions |
| $W^{\pm}_{L}$, $W^{\pm}_{R}$ | the charged connections of the two weak factors |
| $B'$ | the fifteenth $\mathrm{SU}(4)$ Cartan, the corner cell of the grid |
| $T^{c}_{3}$, $T^{c}_{8}$ | the two colour Cartans, removed by the first breaking |
| $T^{15}$ | the corner generator, normalised by $\operatorname{tr}(T^{15})^{2}=\tfrac12$ |
| $B-L$ | $\sqrt{8/3}\,T^{15}$, the charge of the corner |
| $a_1$, $a_2$ | the two neutral vacuum vectors in $\mathbb{R}^3$, both of length $\sqrt{5/8}$ |
| $\mathcal M^2$ | the $3\times3$ neutral mass matrix, $v_C^2a_1a_1^{\mathsf T}+v^2a_2a_2^{\mathsf T}$ |
| $\mathcal M^{2}_{\pm}$ | the $2\times2$ charged mass matrix |
| $v$, $v_C$ | the electroweak and the transition vacuum values |
| $\kappa$, $\kappa'$ | the bidoublet's two diagonal vevs, in the extension only |
| $\beta$ | $\arctan(\kappa'/\kappa)$, the extension's vacuum direction |

## Further Reading

- [Classification of the Bosons in the $\mathrm{SU}(4)$ Model](classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.html).
The grid, the ledger and the fates of all fifteen — the article this one is cut from.
- [The Photon as the Unbroken Mixture: One Null Direction, Three Parents](the-photon-as-the-unbroken-mixture.html). The same null direction derived three
ways.
- [The Mass Matrix of the Fifteen Connection](the-mass-matrix-of-the-fifteen-gauge-bosons-the-u3-kernel-and-the-sextet.html). What the model itself
fixing conditions, and why the weak directions have no row there.
- [The Weinberg Angle and the Three Neutral States](the-weinberg-angle-and-the-three-neutral-states.html). The angle that the null direction leaves free.
- [The Scalar Content: One Quartet, One Doublet, Eight Survivors](the-scalar-content-one-matrix-and-ten-survivors.html). Why no field in
the minimal content carries both weak indices.
- [Rank Five From Three](rank-five-from-three-the-weak-factors-as-a-condensate-index.html). Why the weak factors arrive rather than emerge.
- S. Weinberg, *The Quantum Theory of Fields, Vol. II*, Cambridge University Press, 1996 — the neutral mass matrix, the rank argument, and the photon as
the null direction.
- J. F. Gunion, H. E. Haber, G. Kane and S. Dawson, *The Higgs Hunter's Guide*, Addison-Wesley, 1990 — left-right mixing and the $\rho$ parameter as the
check on the $Z$ mass.
