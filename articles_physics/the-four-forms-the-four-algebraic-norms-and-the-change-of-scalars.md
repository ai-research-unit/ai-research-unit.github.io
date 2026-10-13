# __The Four Forms, the Four Algebraic Norms and the Change of Scalars__

## Introduction

The four general products of the biquaternion complex space carry four **forms**, their scalar parts, and each form carries an **algebraic norm**, its algebraic norm. This article is the third of the three reader articles that introduce the band *Focus on the 12 Algebraic Structures of Biquaternions over $\mathbb{C}$*: the first reads the four general products and the four forms they carry, the second reads the twelve products the four split into and the structures they define, and this one reads the four forms and the four algebraic norms on the six remarkable subspaces, and then reads the same objects after the change of scalars from $\mathbb{C}$ to $\mathbb{R}$ — the **realification**, which doubles the dimension, moves the twelve products and the four forms into the real forms, and carries its own trap in the counting of the structures. It also carries the ruling on the three levels of the word *metric* (§*The Metric: Three Levels*): the biquaternion norm, the two real sectors with their $ict$ metric, and the Clifford tool.

The article owns nothing but the ruling of §*The Metric: Three Levels*, which belongs here because it disambiguates the forms compared below. The forms, their count and their symmetry are *The 4 Forms over the Biquaternion $\mathbb{C}$ Space*; their algebraic norms, the multiplicativity and the definiteness are *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space*; the two on the subspaces are *Remarkable Subspaces and the Four Forms* and *Remarkable Subspaces and the Four Algebraic Norms*; and the realification is *The Realification and the Effect of the Change of Scalars*, whose two-dimensional prototype is *The Realification and the Effect of the Change of Scalars on the Complex Numbers*.

**Conventions.** $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, the relations $e_k^{2}=-e_0$, $e_1e_2=e_3$, $e_2e_3=e_1$, $e_3e_1=e_2$, and central $i$ with $i^{2}=-1$; a general element is $\tilde Q=Q_0e_0+\mathbf Q=\sum_{\mu=0}^{3}Q_\mu e_\mu$, with complex coefficients and vector part $\mathbf Q=\sum_{k=1}^{3}Q_ke_k$. The conjugations are the natural ${}^{\natural}$, fixing $i$ and negating the $e_k$; the coefficientwise $\bar{\cdot}$, conjugating the coefficients; and ${}^{*}=\bar{\cdot}\circ{}^{\natural}$. $\mathrm{Sc}$ is the scalar part, $\mathrm{Tr}=2\,\mathrm{Sc}$ the trace, and $(\mathbf P,\mathbf Q)$ and $\mathbf P\times\mathbf Q$ the complex bilinear dot and cross products of the vector parts. The remarkable subspaces are the centre $\mathbb{C}_{\mathbb{B}}=\mathbb{C}e_0$, the vector subspace $\mathrm{Vect}(\mathbb{B})$, the quaternion and antiquaternion subspaces $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, and the two sectors $\mathbb{M}_+$, $\mathbb{M}_-$. All conventions are those of *Conventions in the Biquaternion Universe*, except the ruling on the three levels of the word *metric* stated below.

## The Four Forms

The scalar part of a general product is a degree-two form of the pair of its arguments, and the four general products give exactly four forms and no more. With the one bracket whose subscript names the inserted conjugation,

$$
B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=\textstyle\sum_\mu\varepsilon_\mu P_\mu Q_\mu,
\qquad
N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=\textstyle\sum_\mu P_\mu Q_\mu,
$$

$$
H(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q^{*})=\textstyle\sum_\mu P_\mu\overline{Q_\mu},
\qquad
K(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q^{*})=\textstyle\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu},
$$

the general plain bilinear, the general quaternionic bilinear, the general plain sesquilinear and the general quaternionic sesquilinear form; they are the jobs of composition, causality, probability and gauge. The multiplication table of the units is the same in all four, so nothing but the insertion distinguishes them, and the four are **one bilinear form read through the two involutions**,

$$
N(\tilde P,\tilde Q)=B(\tilde P^{\natural},\tilde Q),\qquad
H(\tilde P,\tilde Q)=B(\tilde P,\tilde Q^{*}),\qquad
K(\tilde P,\tilde Q)=B(\tilde P^{\natural},\tilde Q^{*}),
$$

a single computation in the four cells of the grid. The symmetry separates them at once: $B$ and $N$ are symmetric and $\mathbb{C}$-bilinear, $H$ and $K$ conjugate-symmetric and sesquilinear, with $H(\tilde P,\tilde Q)=\overline{H(\tilde Q,\tilde P)}$ and $K(\tilde P,\tilde Q)=\overline{K(\tilde Q,\tilde P)}$. Their Gram matrices in the basis $e_0,e_1,e_2,e_3$ are $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$ for $B$, $\mathrm{I}_4$ for $N$, $\mathrm{I}_4$ for $H$ and $\mathrm{E}$ for $K$, the matrix being $\mathrm{E}$ exactly when the two slots are treated alike — neither conjugated, as in $B$, or both, as in $K$ — and $\mathrm{I}_4$ when exactly one is conjugated, as in $N$ and $H$: two of the four forms are the two matrices, and the four forms are pairwise distinct although two pairs share a Gram matrix, a Gram matrix seeing the basis units alone, on which the conjugations act by the sign $\varepsilon_\mu$.

**Two readings of the same object.** A form is read in two ways, and they are not the same statement. Read on the **second slot** it is either $\mathbb{C}$-bilinear — a pairing that can be iterated, the pairing of a composition — or conjugate-linear, a pairing that can only be evaluated, the pairing of a measurement. Read on the **first slot** it is either definite on each sector or signed: the two forms whose first slot is read as it stands, $B$ and $H$, are the two that measure; the two whose first slot carries ${}^{\natural}$, $N$ and $K$, are the two that carry a metric with a light cone. The second slot decides whether the form is a composability or a measurement, the first whether it measures or adds a light cone, and the four forms are the four cells of that grid.

## The Four Algebraic Norms

The **algebraic norm** of a form is its algebraic norm, the degree-two function of one element, read with the same single-value sense as the form:

$$
B(\tilde Q)=Q_0^{2}-\textstyle\sum_kQ_k^{2},\qquad
N(\tilde Q)=Q_0^{2}+\textstyle\sum_kQ_k^{2},\qquad
H(\tilde Q)=\textstyle\sum_\mu\lvert Q_\mu\rvert^{2},\qquad
K(\tilde Q)=\lvert Q_0\rvert^{2}-\textstyle\sum_k\lvert Q_k\rvert^{2}.
$$

Two of the four have a sense the others lack, and the senses are different. **$N$ is multiplicative** on the general quaternionic bilinear product,

$$
N(\tilde P^{\natural}\tilde Q)=N(\tilde P)\,N(\tilde Q),
$$

so that the units and the zero divisors of that product are closed and the light cone is closed under composition; the norm then behaves as a **charge** of the composition, and it is the norm of no other product. **$H$ is positive definite**, $H(\tilde Q)>0$ for $\tilde Q\neq0$, real on every element, and it is the unique topological norm of the space, its square root the Euclidean norm; it is the norm of no other product either. $B$ and $K$ have neither sense: $B$ is a complex bilinear algebraic norm, indefinite and anisotropic over $\mathbb{C}$, and $K$ an indefinite Hermitian algebraic norm. The separation of the **multiplicative** from the **positive definite** sense is the first thing a reader of the four norms must keep: $N$ is multiplicative and not definite, $H$ is definite and not multiplicative, and one and the same element may have a large $N$, a small $H$, or the reverse.

A second separation runs the other way. $B$ and $N$ have a **complex** algebraic norm, real on some elements and complex on others; $H$ and $K$ have a **real** one, being Hermitian. The two complex algebraic norms are the two indefinite forms of the algebras over $\mathbb{C}$; the two real algebraic norms are the two forms of the sesqualgebras. Of the four it is the two complex algebraic norms that are real on the two sectors and complex off them; and of those two, $N$ is the interval and $B$ the sector sign — $N$ indefinite on each sector, its level sets the mass shells, so that the mass is a level set of a real number.

## The Four Forms on the Remarkable Subspaces

Restricted to a subspace, each form is read by its **signature** and by its **coincidences**: two forms may agree, or agree up to sign, on a subspace where they are different on the whole algebra, and the coincidences are the sharpest anatomy of the subspaces. The inertia of the restrictions, over $\mathbb{R}$, on the six subspaces:

| subspace | $B$ | $N$ | $H$ | $K$ |
|---|---|---|---|---|
| centre $\mathbb{C}_{\mathbb{B}}$ | $(1,1)$ | $(1,1)$ | $(2,0)$ | $(2,0)$ |
| vector $\mathrm{Vect}(\mathbb{B})$ | $(3,3)$ | $(3,3)$ | $(6,0)$ | $(0,6)$ |
| quaternion $\mathbb{H}_{\mathbb{B}}$ | $(1,3)$ | $(4,0)$ | $(4,0)$ | $(1,3)$ |
| antiquaternion $i\mathbb{H}_{\mathbb{B}}$ | $(3,1)$ | $(0,4)$ | $(4,0)$ | $(1,3)$ |
| Hermitian $\mathbb{M}_+$ | $(4,0)$ | $(1,3)$ | $(4,0)$ | $(1,3)$ |
| anti-Hermitian $\mathbb{M}_-$ | $(0,4)$ | $(3,1)$ | $(4,0)$ | $(1,3)$ |

**$H$ is definite on every subspace**, positive on the complex and the real-type subspaces alike, and it is the only one of the four that is: the other three are indefinite on the whole algebra, $B$ and $N$ as complex bilinear forms of rank four and $K$ as an indefinite Hermitian form. The definiteness of $H$ is what makes it the Born form, and its presence on every subspace is what makes it the only form a state can be normalised with.

**The coincidences.** On each subspace the four forms coincide up to sign, and the pattern is the subspace's fingerprint:

| subspace | coincidences |
|---|---|
| centre $\mathbb{C}_{\mathbb{B}}$ | $B=N$ and $H=K$ |
| vector $\mathrm{Vect}(\mathbb{B})$ | $B=-N$ and $H=-K$ |
| quaternion $\mathbb{H}_{\mathbb{B}}$ | $B=K$ and $N=H$ |
| antiquaternion $i\mathbb{H}_{\mathbb{B}}$ | $B=-K$ and $N=-H$ |
| Hermitian $\mathbb{M}_+$ | $B=H$ and $N=K$ |
| anti-Hermitian $\mathbb{M}_-$ | $B=-H$ and $N=-K$ |

The pattern separates the subspaces in pairs. On the centre and the vector subspace the four forms are complex-valued and the collapse is internal to each pair, $B=N$ and $H=K$ on the centre and $B=-N$ and $H=-K$ on the vector subspace; on the Hermitian and the anti-Hermitian subspace the collapse crosses the pairs, $B=H$ and $N=K$ on $\mathbb{M}_+$ and $B=-H$ and $N=-K$ on $\mathbb{M}_-$; and the quaternion and antiquaternion subspaces are the mixed case, $B=K$ and $N=H$ on $\mathbb{H}_{\mathbb{B}}$ and $B=-K$ and $N=-H$ on $i\mathbb{H}_{\mathbb{B}}$. On the four real-type subspaces — the quaternion, the antiquaternion and the two sectors — all four forms are **real-valued**, and on the sectors it is there that the two senses of a norm — the interval $N$ and the Euclidean $H$ — are both available on the same element.

**The light cone is the norm cone and not a form cone.** $B$ and $H$ are definite on each sector, so neither has a null cone there; $N$ and $K$ are indefinite on each sector, of signatures $(3,1)$ and $(1,3)$ on the material sector and $(1,3)$ for both on the informational one, so their null sets are the light cone there, $K$ coinciding with $N$ on $\mathbb{M}_+$ and negating it on $\mathbb{M}_-$. On the whole algebra the null set of $B$ is not the light cone but the complex cone of a complex bilinear form, of real dimension six. The forms that carry the light cone are the interval $N$ and its negative, the Krein form; the forms that carry the sector sign and the Born pairing carry no cone.

## The Four Algebraic Norms on the Remarkable Subspaces

Read as norms, the four algebraic norms on the subspaces give the same table with the diagonal entries read off it, and three facts stand out.

**The sector sign.** $B$ is negative definite on $\mathbb{M}_-$ of signature $(0,4)$ and positive definite on $\mathbb{M}_+$ of signature $(4,0)$: on the sectors $B$ is a sign and not an interval, and the sign is the sector's. $H$ is positive definite on both, so it is by $H$ alone that a material and an informational element are measured on the same scale; by $B$ they are measured with opposite signs, and by $N$ or $K$ they are measured with a light cone.

**The interval.** $N$ is of signature $(3,1)$ on $\mathbb{M}_-$ — the metric of the material sector, whose null set is the light cone and whose level sets are the mass shells — and of signature $(1,3)$ on $\mathbb{M}_+$, the same form with the sign of its inertia reversed by the sector. The interval of a material element is a real number, and its level set $\{N=-m^{2}c^{2}\}$ is the mass shell.

**The Krein form.** $K$ is positive definite on the centre of signature $(2,0)$, negative definite on the vector subspace of signature $(0,6)$, and of signature $(1,3)$ on each of the other four subspaces; on the whole algebra it is indefinite of inertia $(2,6)$ as a real form. It is real at the two equal arguments wherever it is defined and its zero set is a cone, which is why it normalises nothing and is read as the gauge form rather than as a probability.

**Two cautions.** The signatures are the signatures of the **restrictions** and not new forms: a restriction may be definite where the form is indefinite, as $K$ is on the centre, and the definiteness of a restriction says nothing about the form. And a norm is not a distance until a square root is taken and a positivity declared, which only $H$ supplies; the other three are algebraic norms and not topological ones.

## The Realification and the Change of Scalars

The construction is the **change of scalars** from $\mathbb{C}$ to $\mathbb{R}$, and its two-dimensional prototype is the complex numbers read over $\mathbb{R}$. A complex vector space, read over $\mathbb{R}$, is the same set with the scalars restricted: the real dimension is **twice** the complex dimension, so that $\mathbb{B}$ of complex dimension four is of real dimension eight, and the two readings are of one algebra and not of two algebras. What the change of scalars adds to the complex space is a **complex structure**, multiplication by the central $i$,

$$
J=L_i,\qquad J^{2}=-\mathrm{id},
$$

and the two kinds of real-linear map are then distinguished by their relation to $J$: a real-linear map is **complex-linear** exactly when it commutes with $J$, $TJ=JT$, and **conjugate-linear** exactly when it anticommutes with it, $SJ=-JS$. The conjugate-linear maps of the complex reading are not a defect of the realification; they are the realification's own second kind of map, and the two block shapes they give are the two block shapes of the real matrix of a complex-linear and of a conjugate-linear map.

**The two rules of realification.** The change of scalars moves the forms by two rules, and they are the reason the four forms have the real signatures they have. A **symmetric bilinear form** realifies to the **split** signature: a complex bilinear form of complex rank $n$ becomes a real bilinear form of signature $(n,n)$. A **Hermitian form** realifies by **doubling its inertia**: a Hermitian form of complex inertia $(p,q)$ becomes a real form of signature $(2p,2q)$. Read on the four forms of $\mathbb{B}$, whose complex data are $B$ and $N$ of complex rank four, and $H$ of inertia $(4,0)$, $K$ of inertia $(1,3)$, the rules give the realified signatures

$$
B:(4,4),\qquad N:(4,4),\qquad H:(8,0),\qquad K:(2,6),
$$

all four indefinite over the reals except $H$, which stays positive definite and is the real Euclidean square. The two rules are also what the restriction table of the previous section re-derives subspace by subspace: the complex line $\mathbb{C}_{\mathbb{B}}$ realifies to a real plane, and the $(1,1)$, $(1,1)$, $(2,0)$, $(2,0)$ of the table are the two rules read on that plane.

**The dictionary, and the trap.** Realifying turns the twelve products and the four forms into operations of the real space, and two statements must be kept apart. The **objects** are the same: the twelve products exist on the same set after the change of scalars, the four forms are the same four forms, and every operation keeps its product over the real numbers, with real coefficients and real parts, since the change of scalars restricts the field and leaves the ring untouched. The **count** is not the same. On the real space a computation restricted to the real part sees ten of the twelve operations, the pairs $\mathrm{APA}=\mathrm{AQS}$ and $\mathrm{SQA}=\mathrm{SPS}$ having collapsed, and it sees the forms only through their restrictions, where the coincidences of the table replace the four distinct forms. A reader who counts the operations on the realification, or tests an identity there, therefore counts ten and reports a distinction erased; the count of twelve is the count on the complex space, and it is the count the band uses.

**What the change of scalars is not.** The realification of $\mathbb{B}$ is $\mathbb{B}$ read over the reals, and not the algebra of pairs of quaternions: the multiplication of the realification is the multiplication of the complex algebra with the scalars restricted, and the complex structure $J$ is what makes the two readings differ. The centre of $\mathbb{B}$ stays the complex line $\mathbb{C}e_0$, the field $\mathbb{C}$ read over $\mathbb{R}$ and not a split algebra; and every object read from the ring alone — the centre, the ideals, the idempotents, the zero divisors, the nilpotents, the units — is unchanged by the passage, because $i$ is an element of the algebra and not an external scalar. The change of scalars is a change of the field of a module and of the dimension, not of the ring.

## The Metric: Three Levels

The word "metric" appears at three distinct levels in the series, and most of the disagreements below are the result of the levels being conflated. They are separated here in order of priority, because the first is the convention of the framework and the third is only a convention of translation.

**Level 1 — the biquaternion norm on $\mathbb{B}$.** The algebra carries the complex-linear biquaternion norm

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_{\mu=0}^{3} Q_\mu^2 ,
$$

and with all four coefficients $Q_\mu$ complex its Gram matrix is the **identity**:

$$
\mathrm{diag}(+1,+1,+1,+1).
$$

This is the metric of the biquaternion universe, and it is the framework's primary convention. It is a metric **on $\mathbb{C}$** — a $\mathbb{C}$-bilinear form — and read that way every one of its four entries is positive: on $\mathbb{B}$ there is no minus sign in the form itself, and none is needed. That is precisely what the complex coefficients buy. A *real* direction has to be labelled positive or negative in advance, and that labelling becomes a convention that can be chosen wrongly; a complex coefficient carries its own sign in the coefficient, so all four directions can start out on an equal footing and no such commitment is required. Two cautions about it. It is not positive definite and it is not a norm in the analytic sense — it vanishes on the nonzero zero divisors, which is why $\mathbb{B}$ is not a normed division algebra. And the Hermitian form $\lvert Q_0\rvert^2 + \lvert Q_1\rvert^2 + \lvert Q_2\rvert^2 + \lvert Q_3\rvert^2$ is a *different* object: real-valued, positive definite, and $\mathbb{C}$-antilinear in its first argument. It is used only where a positive-definite inner product on a complex vector space is needed, and it is not the biquaternion norm of the algebra. The forms of the algebra, with the involution that produces each, are classified in *Conventions in the Biquaternion Universe*, §*The Involutions and the Four Forms*.

**Level 2 — the real sectors.** A minus appears only once a *real* coordinate is placed on a direction whose coefficient carries a factor of $i$. The two four-dimensional real sectors are exactly such choices, and the same level-1 form reads off differently on each:

| Sector | Basis | The norm on the basis | Signature |
|---|---|---|---|
| $\mathbb{M}_-$ (material) | $ie_0,\ e_1,\ e_2,\ e_3$ | $-1,+1,+1,+1$ | $(-,+,+,+)$ |
| $\mathbb{M}_+$ (informational) | $e_0,\ ie_1,\ ie_2,\ ie_3$ | $+1,-1,-1,-1$ | $(+,-,-,-)$ |

Throughout the series a signature is written $(p,q)$ with the **positive** directions counted first, so that the two rows above are $(3,1)$ for $\mathbb{M}_-$ and $(1,3)$ for $\mathbb{M}_+$. The parenthetical count and the $(\pm)$ string are two writings of one fact, $(3,1) = (-,+,+,+)$ and $(1,3) = (+,-,-,-)$, and are never to be read against one another. A group name is not ordered this way, since $\mathrm{O}(3,1)$ and $\mathrm{O}(1,3)$ are two names of one group; the series accordingly writes the Lorentz group indifferently as $\mathrm{SO}(3,1)$ or $\mathrm{SO}^+(1,3)$.

Read as a statement about **objects** rather than directions: an element of $\mathbb{M}_-$ carries the metric $(-,+,+,+)$, and an element of $\mathbb{M}_+$ carries $(+,-,-,-)$. This is not a separate choice made sector by sector — it is the one level-1 form read on two different real bases, and the two are mirror images of one another through the identity below.

The Minkowski interval is not postulated at this level either. It is the level-1 form read on the material sector with the time coordinate written $ict$: the four-position is $\tilde{Q} = ict\,e_0 + \mathbf{x}$, whose scalar coefficient $ict$ is imaginary, and

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural} = (ict)^2 + x^2 + y^2 + z^2 = -c^2t^2 + \mathbf{x}^2 ,
$$

with the minus arising from $i^2 = -1$ alone. Multiplication by $i$ exchanges the sectors, $i\mathbb{M}_+ = \mathbb{M}_-$, and reverses the sign of the form, $\langle i\tilde{Q},i\tilde{Q}\rangle_{\natural} = -\langle\tilde{Q},\tilde{Q}\rangle_{\natural}$; the mirror relation between the two signatures is that identity. The Lorentzian signature is therefore an *output* of the biquaternion conventions, not an input to them.

For contractions of four-vectors in the $ict$ coordinate the series writes this level-2 form as

$$
\eta = \mathrm{diag}(-1,+1,+1,+1),
$$

and at this level the series is uniform: the $ict$ metric is $(-,+,+,+)$ throughout. The two articles outside the relativistic core that carry a symbol $g = \mathrm{diag}(-1,+1,+1,+1)$ — the companion articles on the Higgs mechanism and on the Newman–Penrose formalism — mean **this** object, the $ict$-coordinate metric for index contractions, and not a Clifford metric, as their own notation tables state. They are not part of the level-3 disagreement below.

**Level 3 — the Clifford metric of the $\gamma^\mu$.** When the series writes gamma matrices it needs a further symbol $g$, defined by $\{\gamma^\mu,\gamma^\nu\} = 2g^{\mu\nu}I_4$. This is a property of the chosen generators and not of the biquaternion algebra, and it is best regarded as a **tool** rather than a convention: it can be used or not, depending on the situation, and where it is used it should not dictate any convention of the framework. The biquaternion formulation requires no gamma matrices; they are a translation into the language of the standard Dirac literature, convenient when comparing with that literature or borrowing a standard result, and dispensable otherwise. The freedom this level carries is exactly the freedom the framework treats as presentation: replacing every generator by $i\gamma^\mu$ takes $g$ to $-g$ and leaves the biquaternion algebra, the biquaternion norm, the sector split, the chirality operator and the whole of levels 1 and 2 invariant.

The value the series now uses is the standard **mostly-minus**

$$
g = \mathrm{diag}(+1,-1,-1,-1),
$$

so that $(\gamma^0)^2 = +I_4$ and $(\gamma^k)^2 = -I_4$. Two reasons fix it. First, **it is the form of the objects the tool represents**: the Clifford vectors correspond to the *Hermitian* subspace $\mathbb{M}_+$ — the dictionary's own identification is $x_\mu\gamma^\mu = \gamma^0\mathsf{M}_2(w)$ with $w \in \mathbb{M}_+$ — and $(+,-,-,-)$ is the $\mathbb{M}_+$ form, so the square of a Clifford vector agrees with the biquaternion norm of the biquaternion it represents with **no relative sign**. Second, it is the standard particle-physics convention, so articles transcribing standard results inherit the standard sign without adjustment, and the name $\mathrm{Cl}_{1,3}$ is correct in the usual counting, $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$.

The opposite sign, $g = \mathrm{diag}(-1,+1,+1,+1)$, is **not in use**. It pairs the generators with the material sector, which is a real form they do not belong to; the price is a relative minus sign between the square of a Clifford vector and the biquaternion norm of the biquaternion it represents, a mixed sign pattern in the timelike bivectors, and a non-standard naming of the algebra. It is recorded here only because the series used it previously, in the article that defines the gamma matrices and the Dirac equation, in the Dirac-algebra dictionary, and in the corresponding mathematics article on the Clifford realization of the algebra; those have been aligned to the value above.

A difference at this level would **not** be an error at level 1 or level 2, and half the reason for separating the levels is to stop it being read as one: the biquaternion norm, the $ict$ metric and the sector structure are the same for either sign. The sign decides only which *real* Clifford form the generators generate — $\mathrm{Cl}_{1,3} \cong M_2(\mathbb{H})$ for $(+,-,-,-)$, $\mathrm{Cl}_{3,1} \cong M_4(\mathbb{R})$ for $(-,+,+,+)$ — and the even subalgebra, which is $\mathbb{B}$ itself, is the same for both, so no dictionary entry and no biquaternion identity depends on it.

The order of authority is therefore one-way. The algebra and its level-1 and level-2 conventions are the framework; the gamma matrices and their metric are a translation of it, adopted per article for whatever the article is doing. The tool serves the framework and not the reverse: a Clifford computation is never a reason to change a biquaternion convention, and where the two appear to disagree, the disagreement is in the translation and is resolved by adjusting the generators, the adjoint, or the explicit factors of $i$ — never by altering the biquaternion norm, the $ict$ assignment, or the sector split.

One consequence does reach the physics, and it is the only place where a level-3 choice is not free. The Dirac adjoint is $\bar{\psi} = \psi^\dagger\gamma^0$, so it carries $\gamma^0$ and changes with the convention. With the mostly-minus generators $\bar{\psi}\gamma^0\psi = +\psi^\dagger\psi$, the positive number density; with the mostly-plus generators the same expression gives $-\psi^\dagger\psi$. A spinor bilinear written as $\bar{\psi}\Gamma\psi$ therefore requires the adjoint to be defined consistently with the generators in use. No article in the series currently writes a spinor bilinear in the mostly-plus convention, so no statement in the series is in error on this count; the point is recorded so that one is not introduced. This sign is not part of the freedom that $\gamma^\mu \mapsto i\gamma^\mu$ leaves behind.

**The levels are also distinguished by the law the form obeys.** Beyond their sign, the levels differ in what they do under a product. The level-1 norm is **multiplicative**, $N(\tilde{P}\tilde{Q})=N(\tilde{P})N(\tilde{Q})$, so its level sets multiply and the unit-norm elements form a group; the level-2 interval inherits this multiplicativity on the material sector, which is why a Lorentz transformation preserves the interval and why the rotors are exactly the unit-norm elements. The level-2 Euclidean square and the level-3 Clifford metric are **not** multiplicative, and the positivity of the Hermitian form is what replaces multiplicativity on the state side: the Born weight is not a product of weights but the trace of a product, a pairing rather than a homomorphism. A form that multiplies gives a group of isometries; a form that does not gives a pairing and a Born rule.

## Physical Readings

The four forms are the four quantities a relativistic quantum theory evaluates, and the change of scalars is the passage between the complex formulation and the real one. The readings are the framework's naming of a proved algebra and are labelled as readings.

**The four forms.** The sector sign $B$ is the flag of the two sectors: positive definite on the informational sector and negative definite on the material one, it says which half an element is in and measures neither. The interval $N$ is the metric of the material sector, of signature $(3,1)$ there, its zero set the light cone and its level sets the mass shells, and its multiplicativity is the law by which the causal type of a composite is the product of the causal types. The Born form $H$ is the positive definite pairing of a state and an observable; it is the only form definite on every subspace, hence the only one a probability can be built from, and it is the same form on the informational and the material side. The Krein form $K$ is the indefinite Hermitian form of a gauge calibration, real at the two equal arguments and unable to normalise a state; on the material sector it is minus the interval, so the interval and the gauge form are one form read with a sign.

**The subspaces.** The restriction table is the algebra's own answer to which form belongs to which sector. The material sector carries the interval and the Krein form with the light cone, and the sector sign and the Born form with none; the informational sector carries the interval with the opposite inertia and the sector sign with the opposite sign; the Hermitian and anti-Hermitian subspaces are where the four forms collapse to two pairs, $B=H$ and $N=K$ on $\mathbb{M}_+$, and the collapse is the algebra's statement that on the observable sector the sector sign and the Born form are one form and the interval and the gauge form another. On the sectors the four forms are real, and this realness on the sectors is what makes the mass shell a real level set.

**The change of scalars.** Realifying is what a computation, a simulation or a matrix model does, and it costs exactly the ten-to-twelve distinction: the realification is where the framework is written in real matrices, and it is where the complex witness of the Jacobi failure of $\mathrm{AQS}$ disappears and the two coincident pairs merge. The practical reading is that a real implementation must use the complex space, or must remember which of its ten operations stands for two. The two rules of realification are also the framework's reading of why the interval is indefinite — of inertia $(3,1)$ on the material sector — while the Euclidean form is positive definite of inertia $(8,0)$: one is the restriction of a realified complex bilinear form and the other the realification of a Hermitian one, and the framework treats neither as the other.

## Summary

The four general products of the biquaternion complex space carry four forms, $B$, $N$, $H$, $K$, the four cells of one bilinear form read through the two involutions, of Gram matrices $\mathrm{E}$, $\mathrm{I}_4$, $\mathrm{I}_4$ and $\mathrm{E}$; they carry four algebraic norms. Two of the four norms have a sense the others lack and the senses differ: $N$ is multiplicative on the quaternionic product, so that the units and the light cone are closed and the norm reads as a charge, and $H$ is positive definite and is the unique topological norm. On the six remarkable subspaces each form has a signature and the four forms coincide up to sign, with the pattern $B=N$, $H=K$ on the centre, $B=K$, $N=H$ on the quaternion subspace, $B=H$, $N=K$ on the Hermitian one, and the sign-reversed coincidences on their partners; $H$ is definite on every subspace, $B$ is the sector sign and no cone, and $N$ is the interval whose inertia is $(3,1)$ on the material sector and whose zero set is the light cone.

The change of scalars from $\mathbb{C}$ to $\mathbb{R}$ is the realification: the same algebra read over the reals, of real dimension twice the complex one, with the complex structure $J=L_i$ distinguishing the complex-linear from the conjugate-linear real maps, and with two rules that move the forms — a complex bilinear form realifies to the split signature $(n,n)$ and a Hermitian form doubles its inertia — giving the realified signatures $B:(4,4)$, $N:(4,4)$, $H:(8,0)$, $K:(2,6)$. The objects survive the change and the count does not: a real computation sees ten of the twelve products and the collapsed forms, and the count of twelve belongs to the complex space.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $B$, $N$, $H$, $K$ | the four forms: general plain bilinear, general quaternionic bilinear, general plain sesquilinear, general quaternionic sesquilinear |
| $B(\tilde Q),N(\tilde Q),H(\tilde Q),K(\tilde Q)$ | the four algebraic norms, the algebraic norms of the forms |
| $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$ | the Gram matrix of $B$ and of $K$; $\mathrm{I}_4$ of $N$ and of $H$ |
| $N(\tilde P^{\natural}\tilde Q)=N(\tilde P)N(\tilde Q)$ | the multiplicativity of the quaternionic norm |
| $H(\tilde Q)=\sum_\mu\lvert Q_\mu\rvert^{2}$ | the positive definite norm, the unique topological one |
| $(p,q)$ | the inertia of a form, positive and negative counts of a diagonalisation |
| $J=L_i$, $J^{2}=-\mathrm{id}$ | the complex structure the realification adds |
| $TJ=JT$, $SJ=-JS$ | the criteria for a real-linear map to be complex-linear, respectively conjugate-linear |
| $(n,n)$ and $(2p,2q)$ | the two rules of realification, for a bilinear and a Hermitian form |

## Further Reading

- *The 4 Forms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-forms-over-the-biquaternion-c-space.md`), for the four forms, their count, their Gram matrices and their symmetry.
- *The 4 Algebraic Norms over the Biquaternion $\mathbb{C}$ Space* (`articles_maths/the-4-algebraic-norms-over-the-biquaternion-c-space.md`), for the four algebraic norms, the multiplicativity of $N$ and the definiteness of $H$.
- *Remarkable Subspaces and the Four Forms* (`articles_maths/remarkable-subspaces-and-the-four-forms.md`) and *Remarkable Subspaces and the Four Algebraic Norms* (`articles_maths/remarkable-subspaces-and-the-four-algebraic-norms.md`), for the restriction table and the coincidences of the four forms on the six subspaces.
- *Remarkable Subspaces and the Four General Products* (`articles_maths/remarkable-subspaces-and-the-four-general-products.md`), for the closure of the products on the subspaces.
- *The Realification and the Effect of the Change of Scalars* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars.md`), for the construction, the two rules and the dictionary of the complex and the real statements.
- *The Realification and the Effect of the Change of Scalars on the Complex Numbers* (`articles_maths/the-realification-and-the-effect-of-the-change-of-scalars-on-the-complex-numbers.md`), for the two-dimensional prototype.
- *Conventions in the Biquaternion Universe* (`articles_physics/conventions-in-the-biquaternion-universe.md`), for the conventions of the algebra and the remarkable subspaces.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard particle-physics metric and gamma-matrix conventions.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the metric and normalisation conventions of quantum field theory, and the consequences of changing them.
- Companion articles *The Four General Products and the Degree-2 Forms of the Biquaternion Space* (`articles_physics/the-four-general-products-and-the-degree-2-forms-of-the-biquaternion-space.md`) and *The Twelve Products and the Twelve Algebraic Structures* (`articles_physics/the-twelve-products-and-the-twelve-algebraic-structures.md`).
