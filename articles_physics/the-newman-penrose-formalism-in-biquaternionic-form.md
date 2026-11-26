# __The Newman–Penrose Formalism in Biquaternionic Form__

## Introduction

The Newman–Penrose formalism rewrites the local geometry of four-dimensional spacetime in a basis adapted to the light cone. In place of an orthonormal frame it uses a **null tetrad** $(l, n, m, \bar m)$: two real null vectors $l$ and $n$, and a complex-conjugate pair $m, \bar m$ that are also null. The ten independent components of the Weyl tensor become five complex scalars $\tilde{Ξ}_{0}, \dots, \tilde{Ξ}_{4}$; the connection becomes twelve complex **spin coefficients**; and the Petrov classification of the curvature is read off from which of the five scalars vanish. The formalism is the standard language of the algebraically special solutions of general relativity.

This article places that formalism in the biquaternion framework of the read-list articles, and the placement is not an analogy. The primitive object of the Newman–Penrose construction is a null vector, and the primitive algebraic object of the framework is the **zero divisor**: in the material sector $\mathbb{B}_{\Phi}$ the light cone *is* the zero-divisor cone, a nonzero null vector is a zero divisor of $\mathbb{B}$, and under the matrix realization $\mathsf{M}_2 : \mathbb{B} \to M_2(\mathbb{C})$ it is a rank-one matrix (*Four-Vectors and the Interval*; *The Topology of the Zero-Divisor Cone*). Every leg of a Newman–Penrose tetrad is therefore a zero divisor of the algebra, and the tetrad itself is the image of a normalized spinor dyad under the framework's spinor bilinear. That identification is the centre of this article, and it is verified below rather than asserted.

Three claims organise the discussion.

**First, the null tetrad is algebraic and native, and it is not merely *constructible* from the algebra.** The four legs are elements of $\mathbb{B}$ — $l$ and $n$ in the real material sector $\mathbb{B}_{\Phi}$, with $m$ and $\bar m$ exchanged by star — and each is a zero divisor. Their inner products $l\cdot n = -1$ and $m\cdot\bar m = +1$, and their vanishing self-products, follow from the normalization of the spinor dyad and from the framework's biquaternion norm; the interval is recovered from the tetrad by the completeness relation. The stronger statement is that the tetrad **is** the algebra's matrix-unit basis up to one factor: it is the Peirce basis at a real axis, scaled by $\sigma=\sqrt2\,i$. Three consequences follow and are developed below — the multiplication table of the four legs, the block-antidiagonal pairing that forces the basis to be null, and the trace that distinguishes the two idempotent legs from the two nilpotent ones.

**Second — and developed in the two companion articles on the coefficients and on the scalars — the spin coefficients and the Weyl scalars are hosted but not generated.** The twelve spin coefficients are the components in the null basis of a connection valued in $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}$ — the six-dimensional bivector subspace of $\mathbb{B}$ that the parent article identifies — and the five Weyl scalars are the components of the self-dual Weyl spinor $\tilde{Ξ}_{ABCD} \in \mathrm{sym}^4 S$, where $S$ is the framework's spinor module. The algebra supplies the tetrad, the dyad, and the home of both objects; it supplies neither the connection nor the Weyl tensor.

**Third, and developed in the companion article on the scalars, the weights and the classification are representation-theoretic.** Under the boost–spin subgroup of the tetrad rotations the scalars scale with definite **boost weights**, $\tilde{Ξ}_{\imath} \mapsto A^{2-k} \exp(\,i(2-k)\theta_{\mathrm{cen}})\,\tilde{Ξ}_{\imath}$; the Petrov types are the multiplicity patterns of the principal null directions, equivalently the multiplicity patterns of the roots of the binary quartic $\sum_{A,B,C,D}\tilde{Ξ}_{ABCD}k_Ak_Bk_Ck_D$.

Here $\theta_{\mathrm{cen}}$ is the central phase: it is the argument of a unit complex number, so it is real.

The section closes by separating what the framework contains from what remains unbuilt, and the separation is sharp: the null structure of the tetrad is native, and the curvature that the tetrad is used to describe is not.

The section runs in five articles. This one establishes the identification itself: the tetrad, its multiplication, its pairing, the sector it lives in, the frame in which the identification is exact, the interval it rebuilds and the dyad behind it. *Newman–Penrose and General Relativity: The Equivalence That Is a Change of Basis* states what the formalism is worth against tensor general relativity, and separates the equivalence of the formalism from the identification made here. *The Twelve Spin Coefficients in the Null Tetrad* treats the connection. *The Five Weyl Scalars: Ten Real Components, One Quartic* treats the curvature and the classification. *The Gap: What the Algebra Supplies and What It Does Not* collects the ledger.

The conventions are inherited from the read-list articles and none is redefined. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ satisfying $\vec e_{\imath}^2 = -e_t$ and $\vec e_x \vec e_y = \vec e_z$, and scalar imaginary $i$ commuting with the quaternion units. The anti-Hermitian and Hermitian subspaces are $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$, the real-quaternion subspace is $\mathbb{B}_{H}$, and the biquaternion norm is $\langle\tilde Q\rangle_{\natural} = \tilde Q\tilde Q^{\natural}$. The material sector is $\mathbb{B}_{\Phi} = \{i r'_t e_t + r_x\vec e_x + r_y\vec e_y + r_z\vec e_z : r'_t, r_{\imath} \in \mathbb{R}\}$, with four-vector coordinates $(r'_t,r_x,r_y,r_z)$, and the bilinear (polar) form on it is

$$
\langle \tilde Q_1, \tilde Q_2\rangle_{\natural} \;=\; \mathrm{Sc}\big(\tilde Q_1\tilde Q_2^{\natural}\big) \;=\; -c^2r'_{1t}r'_{2t} + r_{1x}r_{2x} + r_{1y}r_{2y} + r_{1z}r_{2z} ,
$$

of inertia $(3,1)$ in the read list's counting — three positive directions and one negative. The matrix realization is the $\mathbb{C}$-algebra isomorphism

$$
\mathsf{M}_2 : \mathbb{B} \longrightarrow M_2(\mathbb{C}), \qquad
\mathsf{M}_2(e_t) = I_2, \quad \mathsf{M}_2(\vec e_{\imath}) = -i\sigma_{\imath}, \quad \mathsf{M}_2(i) = iI_2,
$$

so that $\langle\tilde Q\rangle_{\natural} = \det\mathsf{M}_2(\tilde Q)$, Hermitian conjugation corresponds to the conjugate transpose, and $\mathbb{B}_{\Phi}$ corresponds to the anti-Hermitian matrices. The spinor module is $S = \mathbb{C}^2$, the unique simple module of $\mathbb{B}$, on which the algebra acts by left multiplication; the Weyl spinor modules are $S = (\tfrac12,0)$ and its conjugate $\bar S = (0,\tfrac12)$. $SU(2)$ is $\{\tilde U : \tilde U\tilde U^{\natural} = e_t\} \cong SL(2,\mathbb{C})$, acting on $\mathbb{B}_{\Phi}$ by rotor conjugation $\tilde{Q} \mapsto \tilde U\tilde{Q}\tilde U^{*}$, with covering homomorphism $\mathrm{Ad}$ onto $SO^+(1,3)$ and kernel $\{\pm e_t\}$. The trace of the matrix image in the informational sector is $\operatorname{tr}\bigl(\mathsf{M}_2(\tilde{H}_{\Psi,1})\mathsf{M}_2(\tilde{H}_{\Psi,2})\bigr) = 2\,\mathrm{Sc}(\tilde{H}_{\Psi,1}\tilde{H}_{\Psi,2})$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum speed.

## Conventions: Signs and the Tetrad Normalization

A null tetrad is defined only up to a six-parameter local Lorentz transformation, and the inner products of its legs are fixed by a convention that must be stated before anything is computed from it. Two conventions are in common use and they differ by signs. This article fixes

$$
l\cdot l = n\cdot n = m\cdot m = \bar m\cdot\bar m = 0, \qquad
l\cdot n = -1, \qquad m\cdot\bar m = +1, \qquad
l\cdot m = l\cdot\bar m = n\cdot m = n\cdot\bar m = 0,
\tag{1}
$$

where $\cdot$ is the general quaternionic bilinear form $\langle\cdot,\cdot\rangle_{\natural}$ of the material sector, the interval, extended $\mathbb{C}$-bilinearly to $\mathbb{C}\otimes_\mathbb{R}\mathbb{B}_{\Phi}$. This is the normalization appropriate to the inertia $(3,1)$ with $\varepsilon=(1,-1,-1,-1)$ that the read list uses; with the opposite metrical convention one takes $l\cdot n = +1$ and $m\cdot\bar m = -1$. Fixed once here, the convention (1) is held throughout.

Two features of (1) are worth naming because they are the source of most sign errors in this subject. First, the tetrad is **not** an orthonormal frame: its legs are null, so the metric in tetrad components is off-diagonal, and the completeness relation that inverts (1) carries the off-diagonal signs. Second, $l$ and $n$ are real four-vectors while $m$ and $\bar m$ are complex conjugates; the tetrad is a basis of the complexified material sector, of complex dimension four, not of the real $\mathbb{B}_{\Phi}$.

The tetrad legs are labelled in the order $(e_1, e_2, e_3, e_4) = (l, n, m, \bar m)$ when a tetrad index is needed. Greek letters ${\imath},\jmath,\dots$ run over the coordinate directions of the material sector, and tetrad indices $a,b,\dots$ over the four legs. The components of a leg in the tetrad carry the same low index, $l_a, n_a, m_a, \bar m_a$, and every contraction over tetrad or spinor indices is written as an explicit sum.

## The Null Tetrad as a Frame of Zero Divisors

The framework's criterion for a zero divisor is a statement about the biquaternion norm: $N$-degeneracy. A nonzero biquaternion $\tilde Q$ is a zero divisor if and only if it is $N$-degenerate, $\langle\tilde Q\rangle_{\natural}=0$, and under the isomorphism $\mathsf{M}_2$ the nonzero zero divisors are exactly the rank-one matrices (*N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors*). Restricted to the material sector, $\langle\tilde Q\rangle_{\natural} = -c^2(r'_t)^2+r_x^2+r_y^2+r_z^2$, so a nonzero element of $\mathbb{B}_{\Phi}$ is a zero divisor exactly when its four-vector is null. The Newman–Penrose construction asks for four null vectors; the framework has a name for them already.

Take the tetrad

$$
l = \frac{i}{\sqrt2}e_t - \frac{1}{\sqrt2}\vec e_z, \qquad
n = \frac{i}{\sqrt2}e_t + \frac{1}{\sqrt2}\vec e_z, \qquad
m = -\frac{1}{\sqrt2}\vec e_x - \frac{i}{\sqrt2}\vec e_y, \qquad
\bar m = -\frac{1}{\sqrt2}\vec e_x + \frac{i}{\sqrt2}\vec e_y .
\tag{2}
$$

In four-vector coordinates $(r'_t,r_x,r_y,r_z)$ the four legs read

$$
l = \big(\tfrac{1}{\sqrt2},0,0,-\tfrac{1}{\sqrt2}\big), \quad
n = \big(\tfrac{1}{\sqrt2},0,0,\tfrac{1}{\sqrt2}\big), \quad
m = \big(0,-\tfrac{1}{\sqrt2},-\tfrac{i}{\sqrt2},0\big), \quad
\bar m = \big(0,-\tfrac{1}{\sqrt2},\tfrac{i}{\sqrt2},0\big),
$$

so $l$ and $n$ are real four-vectors — elements of the real material sector $\mathbb{B}_{\Phi}$ — while $m$ and $\bar m$ are exchanged by complex conjugation. The biquaternion norm vanishes on each leg,

$$
\langle l\rangle_{\natural}=\langle n\rangle_{\natural}=\langle m\rangle_{\natural}=\langle \bar m\rangle_{\natural}=0,
$$

and no leg is zero, so **every leg of the null tetrad is a zero divisor of $\mathbb{B}$**. Under $Ξ$ the legs are the matrix units:

$$
\mathsf{M}_2(l)=\sqrt2\,i\,E_{11}, \quad \mathsf{M}_2(n)=\sqrt2\,i\,E_{22}, \quad \mathsf{M}_2(m)=\sqrt2\,i\,E_{12}, \quad \mathsf{M}_2(\bar m)=\sqrt2\,i\,E_{21},
\tag{3}
$$

where $E_{ij}$ has $1$ in position $(i,j)$ and $0$ elsewhere. Each image has rank one, so the zero-divisor property is visible by rank as well as by norm.

Equation (3) is the precise sense in which the null tetrad is native to the algebra. Up to the common factor $\sqrt2\,i$, the Newman–Penrose tetrad **is** the matrix-unit basis of $\mathbb{B}\cong M_2(\mathbb{C})$. The spinor-module article already names that basis:

$$
\tilde\Pi_{\mathrm{id},1} = \tfrac12(e_t+i\vec e_z), \quad \tilde\Pi_{\mathrm{id},2} = \tfrac12(e_t-i\vec e_z), \quad \vec\Pi_{\mathrm{nil},1} = \tfrac12(i\vec e_x-\vec e_y), \quad \vec\Pi_{\mathrm{nil},2} = \tfrac12(i\vec e_x+\vec e_y),
$$

with $\mathsf{M}_2(\tilde\Pi_{\mathrm{id},1})=E_{11}$, $\mathsf{M}_2(\tilde\Pi_{\mathrm{id},2})=E_{22}$, $\mathsf{M}_2(x)=E_{12}$, $\mathsf{M}_2(y)=E_{21}$, and with $\tilde\Pi_{\mathrm{id},1},\tilde\Pi_{\mathrm{id},2}$ the primitive orthogonal idempotents: $\tilde\Pi_{\mathrm{id},1}^2=\tilde\Pi_{\mathrm{id},1}$, $\tilde\Pi_{\mathrm{id},2}^2=\tilde\Pi_{\mathrm{id},2}$, $\tilde\Pi_{\mathrm{id},1}\tilde\Pi_{\mathrm{id},2}=\tilde\Pi_{\mathrm{id},2}\tilde\Pi_{\mathrm{id},1}=0$. Therefore

$$
\boxed{\;l = \sqrt2\,i\,\tilde\Pi_{\mathrm{id},1}, \qquad n = \sqrt2\,i\,\tilde\Pi_{\mathrm{id},2}, \qquad m = \sqrt2\,i\,x, \qquad \bar m = \sqrt2\,i\,y\;}.
\tag{4}
$$

The two real null directions are the two primitive idempotents, and the complex pair is the off-diagonal pair. The tetrad is the Peirce decomposition of the algebra read as a null frame: the "physical" content of the tetrad — two real null directions — is exactly the idempotent content of $\mathbb{B}$.

The inner products (1) now follow from (4) and the pairing formula $\langle \tilde Q_1,\tilde Q_2\rangle_{\natural} = \mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$. Because $\bar{\tilde\Pi_{\mathrm{id}}}_2 = \tilde\Pi_{\mathrm{id},1}$ and $\tilde\Pi_{\mathrm{id},1}^2=\tilde\Pi_{\mathrm{id},1}$,

$$
\langle l,n\rangle_{\natural} = (\sqrt2\,i)^2\,\mathrm{Sc}(\tilde\Pi_{\mathrm{id},1}\,\bar{\tilde\Pi_{\mathrm{id}}}_2) = -2\,\mathrm{Sc}(\tilde\Pi_{\mathrm{id},1}^2) = -1 ,
$$

and because $\bar{\vec\Pi_{\mathrm{nil},2}} = -\vec\Pi_{\mathrm{nil},2}$ and $\vec\Pi_{\mathrm{nil},1}\vec\Pi_{\mathrm{nil},2} = \tilde\Pi_{\mathrm{id},1}$ in the matrix-unit relations,

$$
\langle m,\bar m\rangle_{\natural} = (\sqrt2\,i)^2\,\mathrm{Sc}(\vec\Pi_{\mathrm{nil},1}\,\bar{\vec\Pi_{\mathrm{nil},2}}) = 2\,\mathrm{Sc}(\vec\Pi_{\mathrm{nil},1}\vec\Pi_{\mathrm{nil},2}) = 2\,\mathrm{Sc}(\tilde\Pi_{\mathrm{id},1}) = +1 .
$$

The subscript is $\natural$ and not $*$: the form is the symmetric bilinear one, and the Hermitian form of the same letters is a different object, with $\langle l,l\rangle_{*}=+1$ and $\langle l,n\rangle_{*}=0$. Only the bilinear form is a metric, and only the bilinear form gives (1).

The mixed products vanish because the off-diagonal units have vanishing scalar part, $\mathrm{Sc}(x)=\mathrm{Sc}(y)=0$, and the relevant products are off-diagonal matrix units. All ten inner products were recomputed from (4); the result is the off-diagonal tetrad metric

$$
g_{ab}[\mathrm{NP}] =
\begin{pmatrix}
0 & -1 & 0 & 0\\
-1 & 0 & 0 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 1 & 0
\end{pmatrix},
\qquad (e_1,e_2,e_3,e_4)=(l,n,m,\bar m).
\tag{5}
$$

The metric is off-diagonal because the basis is null; there is no orthonormal frame hidden in (2). The four diagonal zeros are the null conditions, and the two $\pm1$ entries are the normalizations fixed in (1) and held.

## What the Four Corners Multiply To

Equation (4) says the tetrad is the matrix-unit basis. The matrix-unit basis has a multiplication table, and the table is the part of the identification the article has so far not used. Writing $\sigma=\sqrt2\,i$ so that $l=\sigma\tilde\Pi_{\mathrm{id},1}$, $n=\sigma\tilde\Pi_{\mathrm{id},2}$, $m=\sigma x$, $\bar m=\sigma y$, and multiplying in $\mathbb{B}$ as in $M_2(\mathbb{C})$,

$$
l^{2}=\sigma l,\quad n^{2}=\sigma n,\quad ln=nl=0,\quad m^{2}=\bar m^{2}=0,
$$
$$
lm=mn=\sigma m,\quad \bar ml=n\bar m=\sigma\bar m,\quad m\bar m=\sigma l,\quad \bar mm=\sigma n,
$$
$$
l\bar m=nm=ml=\bar mn=0 .
$$

Every entry was computed on the explicit legs (2); the table is homogeneous of degree one in $\sigma$, so it fixes no normalisation and only closes because $\sigma$ is the same factor in all four legs.

Three lines of it are worth reading physically, because each is a statement about null geometry in algebraic form.

**$ln=nl=0$: the two real null directions annihilate each other.** The two real legs are zero divisors of one another, not merely zero divisors each on its own. A null plane is a square-zero ideal, and the plane spanned by $l$ and $n$ is the simplest instance: any combination of them squares to zero, because the cross terms vanish in both orders.

**$m\bar m=\sigma l$ and $\bar mm=\sigma n$: the transverse pair multiplies into the longitudinal direction.** The complex legs are the nilpotents whose product is the idempotent, which is the corner rule $\vec\Pi_{\mathrm{nil},1}\vec\Pi_{\mathrm{nil},2}=\tilde\Pi_{\mathrm{id},1}$ of the companion maths article, carried into the physics normalisation. A reader who knows only that the four legs are null will not guess this; it is a property of the *particular* four null directions, and it is why the tetrad closes rather than merely spanning.

**$lm=\sigma m$ while $ml=0$: the algebra is not commutative, and the torsion-free null geometry is not either.** Left multiplication by $l$ keeps $m$; right multiplication kills it. That asymmetry is the matrix-unit rule $\tilde\Pi_{\mathrm{id},1} x = x$, $x\tilde\Pi_{\mathrm{id},1}=0$ read in NP letters, and it is the algebraic reason the four spin coefficients built on $\vec\nabla_\Phi l$ and the four built on $\vec\nabla_\Phi n$ stand in no algebraic relation to one another, so that the twelve fall into three groups of four rather than one undifferentiated set.

## Why a Null Basis and Not an Orthonormal One

The numbers in (5) invite the question the framing has not answered: why does the algebra's own matrix basis happen to be null? The answer is in the pairing, and it is structural.

On the four Peirce corners the bilinear form is block-antidiagonal. It pairs the two idempotent corners with each other and the two nilpotent corners with each other, and vanishes on every other combination:

$$
\langle\tilde\Pi_{\mathrm{id},1},\tilde\Pi_{\mathrm{id},2}\rangle_{\natural}=\tfrac12,\qquad
\langle\vec\Pi_{\mathrm{nil},1},\vec\Pi_{\mathrm{nil},2}\rangle_{\natural}=-\tfrac12,\qquad
\langle\tilde\Pi_{\mathrm{id},1},\vec\Pi_{\mathrm{nil},1}\rangle_{\natural}=\langle\tilde\Pi_{\mathrm{id},1},\vec\Pi_{\mathrm{nil},2}\rangle_{\natural}=0,\qquad
\langle\tilde\Pi_{\mathrm{id},1}\rangle_{\natural}=\langle\vec\Pi_{\mathrm{nil},1}\rangle_{\natural}=0 .
$$

So the metric on the Peirce grading is two hyperbolic planes: one spanned by $(\tilde\Pi_{\mathrm{id},1},\tilde\Pi_{\mathrm{id},2})$ and one by $(\vec\Pi_{\mathrm{nil},1},\vec\Pi_{\mathrm{nil},2})$. The corners are the eigenspaces of an idempotent, the form is a duality between complementary corners, and a duality between complementary eigenspaces forces a null basis — it cannot be diagonalised in the corner basis, because each corner is isotropic. That is the structural reason a null tetrad exists at all, and it is stronger than the observation that four null vectors can be found: **the algebra's multiplication basis is null for its own norm, by construction.**

## The Trace Separates Idempotents from Nilpotents

Four arbitrary null directions do not make a Peirce basis. The separation is a trace, and it costs one line.

The four corners carry traces $\mathrm{tr}\,\tilde\Pi_{\mathrm{id},1}=\mathrm{tr}\,\tilde\Pi_{\mathrm{id},2}=1$ and $\mathrm{tr}\,\vec\Pi_{\mathrm{nil},1}=\mathrm{tr}\,\vec\Pi_{\mathrm{nil},2}=0$; in the matrix image these are the traces of $E_{11},E_{22},E_{12},E_{21}$. So the trace splits the tetrad into two legs of weight one and two legs of weight zero, and the split is invariant: no change of basis inside the algebra moves a trace-one element to trace zero. Equivalently, the corner condition is

$$
\tilde Q^{2}=\sigma\tilde Q \iff \tilde Q \text{ is a scaled idempotent},\qquad
\tilde Q^{2}=0 \iff Q_t=0 \text{ and } \langle\tilde Q\rangle_{\natural}=0 ,
$$

the second of which is the nilpotency criterion of *The Square Roots of Zero and the Nilpotents of the Biquaternion Algebra*. The criterion was checked here on two thousand random biquaternions with no mismatch: nilpotence is not the same condition as nullity, and the difference is exactly the vanishing of the time component. A null vector with $Q_t\ne 0$ satisfies $\tilde Q^2=(\mathrm{tr}\,M)\tilde Q\ne0$ by Cayley–Hamilton, and only the null vectors with vanishing time component are nilpotent.

This is what rules out four arbitrary null directions. Given four null vectors, nothing forces two of them to be idempotents and two nilpotents; the Peirce basis is the sub-case in which the traces are $(1,1,0,0)$, and that is a condition on the frame, not a consequence of nullity.

## The Sphere of Idempotents, and the Link of the Null Cone

The idempotents have a shape, and the shape is the sphere. Every primitive idempotent of $\mathbb{B}$ is

$$
\tilde\Pi_{\mathrm{id}}=\tfrac12\bigl(e_t+i\vec u\bigr),\qquad \vec u\in S^{2},
$$

and $\tilde\Pi_{\mathrm{id}}^{2}=\tilde\Pi_{\mathrm{id}}$, $\mathrm{tr}\,\tilde\Pi_{\mathrm{id}}=1$, $\mathrm{rank}\,\tilde\Pi_{\mathrm{id}}=1$ hold for every unit $\vec u$; this was checked on three directions, including a non-axis one. So the idempotents are a two-sphere, the transverse direction is a circle, and a Peirce basis is a point of $S^{2}\times S^{1}$ — axis and transverse phase. The full null tetrad has six parameters, so the Peirce bases form a three-dimensional slice inside the six-dimensional space of tetrads.

The cone statement follows, and the article has so far only cited it. The null cone $\mathcal N=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=0\}$, with the origin adjoined, is exactly the zero-divisor set; it has real dimension six, and its link on the Euclidean seven-sphere is

$$
L=\mathcal N\cap S^{7}_{E}\cong S^{2}\times S^{3},
$$

by *The Topology of the Zero-Divisor Cone*. Read against the previous paragraph, that identification is not a curiosity: the $S^{2}$ factor is the sphere of idempotents, and the $S^{3}$ factor is the spinor frame that produces the dyad. **The fibre of a null frame field is the link of the algebraic null cone.** That is the precise sense in which light-cone structure is native here rather than imposed: the cone of the algebra's own norm is the cone the physics uses, and its link is the space of null frames up to scale.

## Which Sector the Tetrad Lives In

The tetrad is often described as informational, because the idempotents are. That is half true and the half that is false matters.

The idempotents are Hermitian: $\tilde\Pi_{\mathrm{id}}^{*}=\tilde\Pi_{\mathrm{id}}$, so they lie in $\mathbb{B}_{\Psi}$. The nilpotents do not: $\vec\Pi_{\mathrm{nil},1}^{*}=\vec\Pi_{\mathrm{nil},2}$ and $\vec\Pi_{\mathrm{nil},2}^{*}=\vec\Pi_{\mathrm{nil},1}$, so star exchanges them and neither is an eigenvector. The tetrad legs are material: on the explicit legs, $\star l=-l$, $\star n=-n$, $\star m=-\bar m$, $\star\bar m=-m$, so $l$ and $n$ have star eigenvalue $-1$ and lie in $\mathbb{B}_{\Phi}$, while $m$ and $\bar m$ lie in neither sector and are exchanged by star up to sign.

The factor $\sqrt2\,i$ is therefore doing work. A projector is Hermitian; multiplying by $i$ makes it anti-Hermitian; the tetrad leg is material precisely because of that factor. **The same $i$ that makes a boost generator Hermitian in the derivative article makes a projector into a real light ray.** Without it there is no real null vector anywhere in the construction, and a version of the tetrad written with Hermitian projectors would be a complex null frame with no real legs at all.

## The Fixing Condition in Which the Identification Holds

The statement "the tetrad **is** the Peirce basis, up to $\sqrt2\,i$" needs one qualification, and the qualification is a boost.

A Peirce basis has three parameters, the tetrad has six. Three Lorentz parameters therefore take a tetrad off the Peirce slice, and the simplest is the boost along the axis. Under $l\mapsto A l$, $n\mapsto A^{-1}n$ with real $A$, the leg $l=\sigma\tilde\Pi_{\mathrm{id},1}$ becomes $(A\sigma)\tilde\Pi_{\mathrm{id},1}$ and $n$ becomes $(A^{-1}\sigma)\tilde\Pi_{\mathrm{id},2}$: each leg alone is still a scaled idempotent, but the common factor $\sigma$ is gone. The identification holds in the **unit-boost frame**, in which the two real legs share one normalisation, and $\sigma$ is that normalisation rather than an invariant.

This costs a sentence and prevents an overclaim. The correct statement is that the null tetrad is the Peirce basis in the representative where the two real legs have opposite and equal normalisation; in any other representative it is the Peirce basis rescaled leg by leg, which is still a statement about the algebra but no longer a statement about a single $\sigma$.

## The Interval Recovered from the Tetrad

The tetrad is a complex basis of $\mathbb{B}$ as a four-dimensional complex vector space, and the interval is recovered from it by the completeness relation. Since the matrix $\varrho_{\mathrm{ifm}}$ in (5) squares to the identity, the expansion of an arbitrary element $\tilde{Q}\in\mathbb{B}$ in the tetrad is

$$
\tilde{Q} = -\langle \tilde{Q},l\rangle_{\natural}\,n - \langle \tilde{Q},n\rangle_{\natural}\,l + \langle \tilde{Q},m\rangle_{\natural}\,\bar m + \langle \tilde{Q},\bar m\rangle_{\natural}\,m ,
\tag{6}
$$

and, writing $l_{\imath},n_{\imath},m_\mu,\bar m_\mu$ for the components of the legs in the orthonormal coordinate basis of the material sector, the interval's coefficients are

$$
\boxed{\;g_{\imath\jmath} = -l_{\imath} n_{\jmath} - n_{\imath} l_{\jmath} + m_\mu\bar m_{\jmath} + \bar m_\mu m_{\jmath}\;}.
\tag{7}
$$

Substituting (2), the right-hand side of (7) reproduces the interval $-c^2(r'_t)^2+r_x^2+r_y^2+r_z^2$: the four zero divisors rebuild the material-sector interval, and its one minus is the square of the $i$ in $Q_t=i q'_t$. No other input is used. Both (6) and (7) were recomputed symbolically; (6) was checked on a general element $\tilde{Q}$ with all four coefficients arbitrary, and (7) on the explicit legs.

Equation (7) is the null-tetrad counterpart of the frame relation $g_{\imath\jmath} = \langle\tilde E_{\Phi,\imath},\tilde E_{\Phi,\jmath}\rangle_{\natural}$ of the parent article. There the frame was orthonormal and its legs lay in $\mathbb{B}_{\Phi}$; here the frame is null and complex, and its legs are zero divisors. At each point the two are related by the local Lorentz transformation that carries one basis to the other, so the parent's remark — that the algebra supplies the local Lorentz group and the home of the frame, but not the frame itself — applies here verbatim.

## The Spinor Dyad Behind the Tetrad

Equation (3) also exhibits the tetrad's spinorial origin. Writing the two column spinors

$$
o = \begin{pmatrix}1\\0\end{pmatrix}, \qquad o' = \begin{pmatrix}0\\1\end{pmatrix} \in S,
$$

the matrix units factorize as $E_{11} = o\,o^\dagger$, $E_{22} = o'\,o'{}^\dagger$, $E_{12} = o\,o'{}^\dagger$, $E_{21} = o'\,o^\dagger$. Hence

$$
l = \sqrt2\,i\,o\,o^\dagger, \quad n = \sqrt2\,i\,o'\,o'{}^\dagger, \quad m = \sqrt2\,i\,o\,o'{}^\dagger, \quad \bar m = \sqrt2\,i\,o'\,o^\dagger .
\tag{8}
$$

This is the Newman–Penrose **spinor dyad** $\{o,o'\}$ in the framework's notation, the prime marking the second element, and (8) is the sense in which the tetrad is the image of the dyad under the bilinear map $S\times\bar S\to\mathbb{B}$, $(u,v)\mapsto i\,uv^\dagger$, the framework's form of the algebra-level outer product $u\,v^\dagger$, whose Hermitian part the spinor-module article identifies with the vector representation. The dyad is normalized by the invariant symplectic pairing of the spinor module,

$$
\varepsilon(o,o') = o^{T}\epsilon\,o' = 1, \qquad \varepsilon(g o, g o') = \varepsilon(o,o') \ \text{ for } g\in SL(2,\mathbb{C}),
$$

the form $g^{T}\epsilon\,g = \epsilon$ of the read list; it is exactly this normalization, and not the choice of basis, that produces $l\cdot n = -1$ and $m\cdot\bar m = +1$.

The construction is not tied to the basis dyad. For any dyad with $\varepsilon(o,o')=1$ the four legs defined by (8) are null, satisfy $l\cdot n=-1$ and $m\cdot\bar m=+1$, and have all mixed products zero; this was checked symbolically for a general complex dyad, and independently on the explicit real dyad $o=(2,1)$, $o'=(3,2)$, whose symplectic product is $2\cdot2-1\cdot3=1$. That second dyad was chosen for the check rather than being the one that suggested the construction, and the inner products came out as in (1) on it. For the physical tetrad (2), in which the dyad is real, $\bar m$ is the complex conjugate of $m$; a complex dyad (a spin-boost of the frame) complexifies the legs while leaving the inner products (1) unchanged.

## Further Reading

- [Curved Spacetime and the Biquaternion Framework](curved-spacetime-and-the-biquaternion-framework.html), for the frame field and the curvature bivector.
- [Linearized Gravity in Biquaternionic Form](linearized-gravity-in-biquaternionic-form.html), for the Weyl tensor and the self-dual and anti-self-dual bivectors recorded there as an open problem.
- [Gravitational Waves in Biquaternionic Form](gravitational-waves-in-biquaternionic-form.html), for the null wave vector and the component count $10\to6\to2$ that the null tetrad is used to organise.
- [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html), for the spinor module $S$, the matrix units $\tilde\Pi_{\mathrm{id},1},\tilde\Pi_{\mathrm{id},2},x,y$, the symplectic form, and the left and right actions on which the dyad construction rests.
- [The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$](../articles_maths/the-forms-the-norms-and-the-singular-set-of-m4c.html), and [The Topology of the Zero-Divisor Cone](../articles_maths/the-topology-of-the-zero-divisor-cone.html), for the rank-one description, the factorization of null biquaternions into mixed spinors, and the link $S^{2}\times S^{3}$.
- [The Companion Nilpotents of the Biquaternion Algebra](../articles_maths/the-companion-nilpotents-of-the-biquaternion-algebra.html), for the corner decomposition of the algebra into matrix units, the square-zero off-diagonal corners, and the multiplication table on which this article's table is the physics normalisation.
- [The Square Roots of Zero and the Nilpotents of the Biquaternion Algebra](../articles_maths/the-square-roots-of-zero-and-the-nilpotents-of-the-biquaternion-algebra.html), for the nilpotency criterion $Q_t=0$ with vanishing norm that separates the nilpotent legs from the idempotent ones.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the biquaternion-norm criterion and the classification of zero divisors used throughout.
- [Helicity in Biquaternionic Form](helicity-in-biquaternionic-form.html), for the factorization of a null momentum into a spinor bilinear, of which the null tetrad is the four-legged version.
- [Four-Vectors and the Interval](four-vectors-and-the-interval.html), for the material sector, its biquaternion norm, and the identification of its null cone with the zero divisors.
- *Spinors*, for the two-component spinor conventions.
