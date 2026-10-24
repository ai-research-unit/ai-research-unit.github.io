# __The Null Quadric and Its Projective Geometry__

## Introduction

The general quaternionic bilinear form of the biquaternion algebra, $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_{1,\mu} Q_{2,\mu}$, is non-degenerate, and a non-degenerate form in four variables has a projective geometry: its null set is a quadric. This article is that geometry. The quadric, the two rulings of its null planes, its polarity, its automorphism group and its complement are the projective reading of the form, and they sit beside the affine reading of the same form on the algebra and on the remarkable real subspaces.

Two further readings belong to the same quadric and are collected here. The spinor factorisation of a null element reads the two rulings as the two families of spinor lines, the projectivisations of the two chiral spinor spaces. The real forms of the quadric carry the Lorentzian, the split and the conformal geometries: the null cone of a Lorentzian slice, the celestial sphere with its Möbius action, the split quadric ruled by real lines, and the conformal group of Lorentzian space with its double cover $SU(2,2)$. The three are the same projective object seen over $\mathbb{R}$ and over $\mathbb{C}$.

The article is the companion of *The Isotropic Structure of the General Quaternionic Algebra*, which reads the same form affinely — the cone of real dimension $6$, its isotropic lines, its restrictions to the remarkable subspaces — and of *The Four Forms and the Four Algebraic Norms*, which owns the form and its diagonal. The cone whose projectivisation is the quadric is studied as a topological space, with no form entering, in *The Topology of the Zero-Divisor Cone*; the real forms of the form and their signatures are *Remarkable Subspaces under the General Quaternionic Algebra*, §*The Signatures and the Restriction Matrices*; the spinor spaces and the Clifford module are *Spin Representations and Clifford Modules with Inner Conjugation*, the ideals are *Ideals and Peirce Decompositions of the Biquaternion Algebra*, and the reality types are *Real Spinors and Reality Conditions with Inner Conjugation*; the Lorentz group and its double cover are *Biquaternion Rotations and Lorentz Transformations*; the algebra and its fixed-point subspaces are *The Biquaternion Algebra and Its Vector Spaces*; the classical groups that act are *Lie Groups*; and the conformal model of Euclidean space and the Lorentzian framework are *The Conformal Model of Euclidean Space* and *Pseudo-Riemannian and Lorentzian Geometry* of Part IV.

## The Segre Embedding

Choose on $\mathbb{B}$ the linear coordinates

$$
Z_0=Q_t-iQ_z,\qquad Z_1=-iQ_x-Q_y,\qquad Z_2=-iQ_x+Q_y,\qquad Z_3=Q_t+iQ_z,
$$

an invertible $\mathbb{C}$-linear change of the coordinates $Q_t,\dots,Q_z$. In them the form is a split form,

$$
\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^2=Z_0Z_3-Z_1Z_2,
$$

since $Z_0Z_3=(Q_t-iQ_z)(Q_t+iQ_z)=Q_t^2+Q_z^2$ and $Z_1Z_2=(-iQ_x-Q_y)(-iQ_x+Q_y)=-Q_x^2-Q_y^2$. The null cone is therefore the affine hypersurface $Z_0Z_3=Z_1Z_2$, and each of its nonzero points is a pair of one-dimensional subspaces of $\mathbb{C}^2$. Indeed, for nonzero $u=(\alpha,\beta)$ and $v=(\gamma,\delta)$ the point

$$
(Z_0,Z_1,Z_2,Z_3)=(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta)
$$

lies on the null cone, since $\alpha\gamma\cdot\beta\delta=\alpha\delta\cdot\beta\gamma$, and conversely every null point is of this form: if $Z_0\neq0$ the pair $u=(1,Z_2/Z_0)$, $v=(Z_0,Z_1)$ reproduces it, and the other cases are the same argument applied to a coordinate that is nonzero. The pair is determined only up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$.

Projectivising gives the **Segre embedding**

$$
s:\mathbb{P}^1\times\mathbb{P}^1\longrightarrow\mathbb{P}^3,\qquad ([u],[v])\mapsto[\alpha\gamma:\alpha\delta:\beta\gamma:\beta\delta],
$$

whose image is exactly the projective null quadric

$$
\mathbb{P}(\mathcal{N})=\{[\tilde{Q}]\in\mathbb{P}^3:\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0\}.
$$

The affine null cone is the cone over the Segre variety $\mathbb{P}^1\times\mathbb{P}^1$, and the zero-divisor set is that cone with its apex removed (*The Topology of the Zero-Divisor Cone*).

## The Two Rulings of Null Planes

In the coordinates above the polar form of $N$ is

$$
\langle\tilde Q_1,\tilde S\rangle_{\natural}=\tfrac12\bigl(Z_0Z'_3+Z_3Z'_0-Z_1Z'_2-Z_2Z'_1\bigr),
$$

the polarisation of $Z_0Z_3-Z_1Z_2$, which returns the norm on the diagonal, $\langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}$. For each $[u]=[\alpha:\beta]\in\mathbb{P}^1$ the two-dimensional subspace

$$
W_{[u]}=\operatorname{span}\{(\alpha,0,\beta,0),\,(0,\alpha,0,\beta)\}=\{(\alpha\sigma,\alpha\tau,\beta\sigma,\beta\tau):\sigma,\tau\in\mathbb{C}\}
$$

is totally isotropic: for $\tilde Q_1$ built from $\sigma,\tau$ and $\tilde S$ from $\sigma',\tau'$ the form above gives $\langle\tilde Q_1,\tilde S\rangle_{\natural}=\tfrac12\alpha\beta(\sigma\tau'+\tau\sigma'-\tau\sigma'-\sigma\tau')=0$. Since $\dim W_{[u]}=2$ is the maximal isotropic dimension for a non-degenerate form in dimension $4$, $W_{[u]}$ is a **null plane**, and the same holds for

$$
W^{[v]}=\operatorname{span}\{(\gamma,\delta,0,0),\,(0,0,\gamma,\delta)\},\qquad [v]=[\gamma:\delta].
$$

Their projectivisations $\ell_{[u]}=\mathbb{P}(W_{[u]})$ and $m_{[v]}=\mathbb{P}(W^{[v]})$ are the **two rulings**: each family is a $\mathbb{P}^1$ of lines; every quadric point lies on exactly one line of each family; lines of the same family are disjoint, while lines of different families meet in exactly one point, the point $[(\alpha\gamma,\alpha\delta,\beta\gamma,\beta\delta)]$ that the pair $([u],[v])$ determines.

## Spinors and the Rulings

**Theorem (a null biquaternion is a mixed spinor of rank one).** Under the identification of the complexified Lorentz algebra with $\mathfrak{sl}_2(\mathbb{C})\oplus\mathfrak{sl}_2(\mathbb{C})$, the algebra is the tensor product

$$
\boxed{\;\mathbb{B}\cong\Delta^+\otimes\Delta^-,\qquad \dim_{\mathbb{C}}\Delta^\pm=2\;},
$$

so that a biquaternion is a **mixed spinor** $A_\alpha{}^{\bar\beta}$ with one unbarred and one barred index. Its matrix image has rank one exactly when it is null, and then

$$
\boxed{\;A_\alpha{}^{\bar\beta}=\phi_\alpha\,\pi^{\bar\beta},\qquad \phi\in\Delta^+,\ \pi\in\Delta^-\;}.
$$

**Proof.** The determinant of $\mathsf{M}_2(A)$ is $\langle A\rangle_{\natural}$, so $A$ is null exactly when the matrix has rank at most one; a nonzero matrix of rank one is $uv^{\mathsf T}$ for a column $u$ and a row $v^{\mathsf T}$, and the entries reproduce the Segre coordinates of the previous section. The column is the unbarred factor $\phi$ and the row the barred factor $\pi$.

**Corollary (the rulings are the two families of spinor lines).** Fixing $\phi$ and varying $\pi$ traces the line $\ell_{[\phi]}\cong\mathbb{P}(\Delta^-)=\mathbb{P}^1$; fixing $\pi$ and varying $\phi$ traces $m_{[\pi]}\cong\mathbb{P}(\Delta^+)=\mathbb{P}^1$. The two rulings of $Q^2$ are therefore the **barred and unbarred spinor lines**, and the incidence of the two families is the pairing of a spinor with a cospinor.

**Remark (chirality is not the minimal-ideal splitting).** The two minimal left ideals of $\mathbb{B}\cong M_2(\mathbb{C})$ are $\mathbb{B}\tilde\Pi_1$ and $\mathbb{B}\tilde\Pi_2$, cut out by a complete pair of orthogonal idempotents; each is a copy of $\mathbb{C}^2$ and the algebra is their direct sum, so the spin representation is realised inside the algebra (*Ideals and Peirce Decompositions of the Biquaternion Algebra*). Neither ideal is a chiral half: each of them complexifies to $S_+\oplus S_-$. The chirality belongs to the algebra, as the tensor splitting $\Delta^+\otimes\Delta^-$; on the module, the Clifford multiplication $c(\gamma_k)=\sigma_k$ has $c(\omega)=iI$ for the volume element, so the module carries no real chirality splitting, and the $\pm i$ eigenspaces appear only after complexification, where they are the two Weyl spaces. The reality type is complex and there is no Majorana spinor (*Spin Representations and Clifford Modules with Inner Conjugation*, *Real Spinors and Reality Conditions with Inner Conjugation*).

**Remark (the operator).** The Clifford structure also defines the Dirac operator $D=\sum_\mu e_\mu\partial_\mu$ on the algebra, whose square is the d'Alembertian, $D^2=\Box$, and whose kernel is the space of regular functions. Its analytic theory — the kernel, the Cauchy integral and the decomposition of the space of functions — is *Fueter Theory for Biquaternions* and *Biquaternion Regular Functions* in Analysis. It is cited here and not restated: the operator belongs to the Clifford structure, while its analysis belongs to those articles.

**Remark (two Clifford structures).** The algebra carries two Clifford structures, and they must not be confused. The first attaches the spinor module to Lorentzian space, using $\mathbb{B}\cong\mathrm{Cl}^+_{1,3}$: the module is the pair of Weyl spinors of the Lorentz group, and the geometry is the spin geometry of Lorentzian space. The second attaches a module to the algebra itself as a quadratic space, using $\mathrm{Cl}(\mathbb{B},N)\cong\mathrm{Cl}_4(\mathbb{C})$, whose even part has the two chiral summands. Both modules are two-dimensional over $\mathbb{C}$ and both carry a Dirac operator, and the algebra is the bridge between them: it is the even Clifford algebra of one quadratic space and a quadratic space in its own right. The general construction is *Spin Geometry* and *The Dirac Operator* of Part IV, and the Clifford classification is *Biquaternion Other Algebraic Element Representations*.

## The Projective Null Quadric $Q^2$

The projectivised null cone

$$
Q^2=\{[\tilde{Q}]\in\mathbb{P}^3:\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0\}
$$

is a smooth irreducible quadric surface, isomorphic to $\mathbb{P}^1\times\mathbb{P}^1$; it is the classical **Segre quadric**. Non-degeneracy of the form gives smoothness, and over $\mathbb{C}$ all smooth quadric surfaces in $\mathbb{P}^3$ are projectively equivalent.

Its real points depend on the real form of the general quaternionic bilinear form (*Remarkable Subspaces under the General Quaternionic Algebra*, §*The Signatures and the Restriction Matrices*): empty for the definite form, the sphere $S^2$ for the Lorentzian form, the torus $S^1\times S^1$ for the split form. The three cases, with their groups and their conformal readings, are §*The Real Slices: Lorentzian, Split and Conformal* below.

## Lines in $\mathbb{P}^3$, the Klein Quadric and the Plücker Embedding

A line in $\mathbb{P}^3$ is $\mathbb{P}(U)$ for a two-dimensional subspace $U\subset\mathbb{C}^4$. With a basis $\tilde Q_2,\tilde Q_1$ of $U$, the **Plücker coordinates** are the six minors

$$
p_{ij}=Q_{2,i}Q_{1,j}-Q_{2,j}Q_{1,i},\qquad 0\le i < j\le3,
$$

the coordinates of the decomposable bivector $\tilde Q_2\wedge\tilde Q_1\in\Lambda^2\mathbb{C}^4$, defined up to an overall scalar. This gives the **Plücker embedding**

$$
\mathrm{Gr}(2,4)\hookrightarrow\mathbb{P}(\Lambda^2\mathbb{C}^4)=\mathbb{P}^5,
$$

whose image is the **Klein quadric**, the quadric hypersurface of dimension $4$ cut out by the Plücker relation

$$
\boxed{\;p_{01}p_{23}-p_{02}p_{13}+p_{03}p_{12}=0\;}.
$$

Over $\mathbb{R}$ the Plücker form has signature $(3,3)$. This Klein quadric in $\mathbb{P}^5$ is distinct from the null quadric $Q^2$ in $\mathbb{P}^3$: it is the variety of lines of the projective space in which $Q^2$ sits.

The rulings of $Q^2$ appear in this picture as follows. A line of $Q^2$ is a maximal isotropic two-plane, and its Plücker point lies on the Klein quadric. The lines on $Q^2$ form two components, the two rulings, each a $\mathbb{P}^1$; their Plücker images are two conics on the Klein quadric. (The maximal isotropic subspaces of the Klein quadric itself are two families of projective planes $\mathbb{P}^2$: the stars of lines through a fixed point and the plane fields of lines in a fixed plane.)

## Tangency and Polarity

The form defines a **polarity**, the correlation

$$
[\tilde Q_1]\longmapsto[\tilde Q_1]^{\perp}=\{[\tilde Q_2]:\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=0\},
$$

well defined by bilinearity and bijective by non-degeneracy. The quadric is the locus of self-polar points, $[\tilde Q_1]\in Q^2\iff \langle\tilde Q_1,\tilde Q_1\rangle_{\natural}=0$. For $[\tilde Q_1]\in Q^2$, since the differential of $N$ at $\tilde Q_1$ is $2\langle\tilde Q_1,\cdot\,\rangle_{\natural}$, the polar hyperplane is the **tangent hyperplane**, and its intersection with the quadric is the pair of ruling lines through $[\tilde Q_1]$,

$$
Q^2\cap[\tilde Q_1]^{\perp}=\ell_{[u]}\cup m_{[v]},
$$

one line from each family. For two distinct null points $[\tilde Q_1],[\tilde Q_2]$, the form on the line $\tilde Q_1+t\tilde Q_2$ is $2t\,\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$, so

$$
[\tilde Q_1][\tilde Q_2]\subset Q^2\iff \langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=0,
$$

in which case the two points lie on a common ruling line. A line through $[\tilde Q_1]\in Q^2$ is therefore tangent exactly when its direction lies in the tangent hyperplane; the two ruling lines are tangent, and every other tangent line meets the quadric only at $[\tilde Q_1]$.

## Automorphisms of the Quadric

The projective automorphisms of $Q^2$ are induced by the complex orthogonal group of the form:

$$
\boxed{\;\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})=O_4(\mathbb{C})/\{\pm I\}\;},
$$

acting on $\mathbb{P}^1\times\mathbb{P}^1$ by $([u],[v])\mapsto([Au],[Bv])$, with the $\mathbb{Z}/2$ exchanging the rulings. Its identity component $PSO_4(\mathbb{C})$ preserves each ruling; the outer component swaps them. The Lorentz group is not the whole of this group: $SO^+(1,3)$ is the conformal group of the projective null cone $S^2$ of the Lorentzian real form, and it acts on $Q^2$ as the three-complex-dimensional subgroup of left multiplications, not as the full automorphism group.

## The Real Slices: Lorentzian, Split and Conformal

The complex quadric has a real locus for each real form of the form, and the sign of the restricted form is the organising datum. The group of motions is the invariant of the geometry; the same algebra carries all the geometries at once, and the passage from one to another is a change of real form, not a change of algebra.

| real form | signature | real points of $Q^2$ | group of motions |
|---|---|---|---|
| $\mathbb{H}_{\mathbb{B}}$ | $(4,0)$ | empty | $Sp(1)=S^3$ |
| $i\mathbb{H}_{\mathbb{B}}$ | $(0,4)$ | empty | $Sp(1)=S^3$ |
| $\mathbb{M}_+$ | $(1,3)$ | $S^2$ | $SO^+(1,3)$ |
| $\mathbb{M}_-$ | $(3,1)$ | $S^2$ | $SO^+(1,3)$ |
| the split form | $(2,2)$ | $S^1\times S^1$ | $SO^+(2,2)$ |

The definite forms give no real null point except the apex of the cone, so their real quadric is empty; the indefinite Lorentzian forms give a sphere; the neutral split form gives a torus.

**Theorem (the null cone of a Lorentzian slice).** Write an element of $\mathbb{M}_-$ as $\tilde Q=iq'_te_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, with real coordinates. The restriction of the norm is

$$
\langle\tilde Q\rangle_{\natural}=-(q'_t)^2+q_x^2+q_y^2+q_z^2,
$$

so $\mathbb{M}_-\cong\mathbb{R}^{3,1}$; on $\mathbb{M}_+$ the signs are opposite and the signature is $(1,3)$. Either slice is identified with Lorentzian space $\mathbb{R}^{1,3}$, and its null set,

$$
\boxed{\;\langle\tilde Q\rangle_{\natural}=0\iff(q'_t)^2=q_x^2+q_y^2+q_z^2\;},
$$

is the **null cone**, a double cone with apex at the origin. Intersecting with the unit sphere of the slice gives $q'_t=\pm1/\sqrt2$ and $q_x^2+q_y^2+q_z^2=1/2$, so the link of the cone is $S^2\sqcup S^2$, one sphere per nappe, and the complement of the cone in the slice has three connected components: the future timelike, the past timelike and the spacelike regions (*Remarkable Subspaces under the General Quaternionic Algebra*, §*The Signatures and the Restriction Matrices*).

**Remark (two dimensions that must not be confused).** The null cone of the slice is a real cone of real dimension $3$ in $\mathbb{M}_-\cong\mathbb{R}^4$. The full null cone $\mathcal{N}\subset\mathbb{B}$ is a complex cone of complex dimension $3$ and real dimension $6$, and the cone of the slice is its intersection with $\mathbb{M}_-$. The Lorentz group acts on the slice without being contained in it: $\mathbb{M}_+$ has real dimension four and $SO^+(1,3)$ real dimension six. Its double cover $\mathbb{B}^{\times}_1$ is a level set in the algebra, and the group itself is the projective complement of the quadric (*Biquaternion Rotations and Lorentz Transformations*).

**The celestial sphere and the Möbius action.** The projectivisation of the null cone of $\mathbb{M}_+$ is the **celestial sphere**

$$
\boxed{\;\mathbb{P}(\mathcal{N}\cap\mathbb{M}_+)\cong S^2\;},
$$

a real slice of $Q^2$. The proper orthochronous Lorentz group acts on $S^2=\mathbb{C}\mathbb{P}^1$ by Möbius transformations, the orientation-preserving conformal diffeomorphisms, and the full Lorentz group $O(1,3)$ acts by all Möbius transformations, the additional ones being complex conjugation.

Two qualifications fix the sense of the word conformal. First, $SO^+(1,3)$ is not the automorphism group of the complex quadric: that is the larger $PO_4(\mathbb{C})$ of complex dimension $6$ and real dimension $12$, of which the Lorentz group is the group of a real form, of real dimension $6$. Second, the conformal group here is that of the celestial sphere $S^2$, not that of Lorentzian space: the conformal group of $\mathbb{R}^{1,3}$ is the larger $O(2,4)$ below. The Lorentz group is the conformal group of the **projective null cone** only.

**The conformal group of Lorentzian space.** The conformal compactification of $\mathbb{R}^{1,3}$ is a quadric in $\mathbb{R}^{2,4}$, and its transformation group is $O(2,4)$, of real dimension $15$, with identity component $SO^+(2,4)\cong SO(4,2)$. Its double cover is

$$
\boxed{\;SU(2,2)\cong Spin(4,2)\;},
$$

acting on a four-dimensional complex space that carries a Hermitian form of signature $(2,2)$; that space is the biquaternion algebra read as a complex vector space. The fifteen dimensions are the six of the Lorentz group, the four of the translations, the four of the special conformal transformations and the one of the dilation. This group is not a subgroup of $\mathbb{B}^{\times}$: it shares the Lorentz subgroup but enlarges it by transformations that are not multiplications of the algebra (*Biquaternion Objects and Their Matrix Correspondences*, §*The Bigger Groups of the Twisted Spinor*).

**The conformal model.** In the conformal model of Euclidean space $\mathbb{R}^n$ the flat space is recovered from a null cone in $\mathbb{R}^{n+1,1}$. Two null vectors are distinguished, the origin $n$ and the point at infinity $n_\infty$, with $\langle n,n_\infty\rangle=-1$; a point $X\in\mathbb{R}^n$ is represented by a null vector whose inner products with $n$ and $n_\infty$ fix its coordinates. A sphere is the vector $S=P-\tfrac12r^2n_\infty$ for a point $P$ and a radius $r$, a plane is a vector orthogonal to $n_\infty$, and a point lies on a sphere or a plane exactly when the corresponding vectors are orthogonal. The transformations are the versors of the Clifford algebra $\mathrm{Cl}_{n+1,1}$, acting by the signed inner conjugation; in the matrix form of the Vahlen matrices they are the analogues of the Möbius transformations, and the sandwich action of a biquaternion on the projective line is the case $n=2$. The construction is that of *The Conformal Model of Euclidean Space*, and the Lorentzian framework is that of *Pseudo-Riemannian and Lorentzian Geometry*, both of Part IV; nothing beyond the cited statements is used here.

**The split slice.** For the split real form of signature $(2,2)$ the real quadric is

$$
S^1\times S^1\cong\mathbb{P}^1_{\mathbb{R}}\times\mathbb{P}^1_{\mathbb{R}},
$$

and the rulings are real, so the quadric is doubly ruled by real lines; the connected group is $SO^+(2,2)$, acting on the two factors separately. In the Lorentzian case no real line lies on the real quadric: the real points form $S^2$, and the rulings exist only over $\mathbb{C}$. The signature thus decides whether the rulings are visible over $\mathbb{R}$ or only over $\mathbb{C}$.

## The Complement of the Quadric

The quadric and its complement exhaust the projective space. The condition $\langle\tilde Q\rangle_{\natural}=0$ is homogeneous of degree two, so it descends to $\mathbb{P}^3=\mathbb{P}(\mathbb{B})$, and the complement is the set of the classes of the units,

$$
\boxed{\;\mathbb{P}^3\setminus Q^2=\{[\tilde Q]\in\mathbb{P}^3:\langle\tilde Q\rangle_{\natural}\neq0\}=\mathbb{B}^{\times}/\mathbb{C}^{\times}e_t\cong PGL(2,\mathbb{C})\;}.
$$

Under the isomorphism $\mathbb{B}\cong M_2(\mathbb{C})$, a class is an invertible matrix up to a nonzero scalar, and the multiplication of classes is the multiplication of matrices up to scalars. Every nonzero complex number is a square, so every class has a representative of determinant one, and

$$
PGL(2,\mathbb{C})=PSL(2,\mathbb{C})\cong SO^+(1,3).
$$

The complement is therefore, as a real Lie group, isomorphic to the proper orthochronous Lorentz group itself, not to its double cover: the quotient by the central scalars has already been taken, and the two central signs $\pm e_t$ are the same projective class. The affine level set $\{\langle\tilde Q\rangle_{\natural}=1\}\cong SL(2,\mathbb{C})$ is the double cover of the same group inside $\mathbb{B}$ (*Biquaternion Objects and Their Matrix Correspondences*).

The complement is open in $\mathbb{P}^3$, of complex dimension $3$ and real dimension $6$; it is a complex submanifold, and it is not a linear subspace. It is a submanifold of the projective space, not of the affine space $\mathbb{B}$: the quotient by the scalars is what passes from the double cover to the group. The projective line through $[e_t]$ and $[\vec e_x]$ has the affine part $[e_t+t\vec e_x]$, whose norm is $1+t^2$, together with the point $[\vec e_x]$ at infinity, and it meets the quadric at the two points $t=\pm i$; a linear subspace contained in the complement would meet the quadric in none.

The same group acts on the quadric. A class $[A]\in PGL(2,\mathbb{C})$ sends $[\tilde Q]$ to $[A\tilde Q]$, which preserves the determinant and hence the quadric; in the Segre coordinates $([u],[v])$ this is $([Au],[v])$, the action on the first factor only. The image is a three-complex-dimensional subgroup of $\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})$, which has complex dimension $6$. The Lorentz group acts on the quadric, and its underlying manifold is the complement of the quadric; the two statements are different, and neither makes it the full automorphism group.

## Summary

- The projective null cone $Q^2=\mathbb{P}(\mathcal{N})$ is the smooth irreducible quadric surface $\mathbb{P}^1\times\mathbb{P}^1$, the Segre quadric; the affine null cone is the cone over it and the zero-divisor set is that cone minus its apex.
- The **Segre embedding** $s:\mathbb{P}^1\times\mathbb{P}^1\to\mathbb{P}^3$, $([u],[v])\mapsto[\alpha\gamma:\alpha\delta:\beta\gamma:\beta\delta]$, has the quadric as its image; in the coordinates $Z_0,\dots,Z_3$ the form is $Z_0Z_3-Z_1Z_2$ and the quadric is the locus of self-polar points.
- The two **rulings** are the two families of maximal isotropic null planes, each a $\mathbb{P}^1$; every quadric point lies on exactly one line of each family.
- A null biquaternion is a **mixed spinor of rank one**, $\mathbb{B}\cong\Delta^+\otimes\Delta^-$ and $A_\alpha{}^{\bar\beta}=\phi_\alpha\pi^{\bar\beta}$; the two rulings are the projectivisations of the two chiral spinor spaces, the barred and unbarred spinor lines. The minimal left ideals are not the chiral halves.
- The **real loci** depend on the real form: empty for the definite forms, the sphere $S^2$ for the Lorentzian forms, the torus $S^1\times S^1$ for the split form. The null cone of a Lorentzian slice is a real cone of dimension $3$ against the complex cone of dimension $6$; its projectivisation is the celestial sphere, on which $SO^+(1,3)$ acts by Möbius transformations. The conformal group of Lorentzian space is the larger $O(2,4)$, with double cover $SU(2,2)\cong Spin(4,2)$; the conformal model of Euclidean space is that of Part IV, cited.
- The quadric sits in the **Plücker–Klein geometry** of the lines of $\mathbb{P}^3$; its rulings are two conics on the Klein quadric in $\mathbb{P}^5$.
- The **polarity** of the form gives the tangency: at a point of the quadric the polar hyperplane is the tangent hyperplane and its intersection with the quadric is the pair of ruling lines through the point.
- $\operatorname{Aut}(Q^2)\cong PO_4(\mathbb{C})$, its identity component preserving each ruling and the outer component swapping them; the Lorentz group is the three-complex-dimensional subgroup of left multiplications, not the full automorphism group.
- The **complement** $\mathbb{P}^3\setminus Q^2=\mathbb{B}^{\times}/\mathbb{C}^{\times}e_t\cong PGL(2,\mathbb{C})=PSL(2,\mathbb{C})\cong SO^+(1,3)$ is the Lorentz group itself; it is open, of complex dimension $3$ and real dimension $6$, a complex submanifold and not a linear subspace; the group acts on $Q^2$ by left multiplication, as a three-complex-dimensional subgroup of $\operatorname{Aut}(Q^2)$, not as the full automorphism group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural} = \sum_\mu Q_{1,\mu} Q_{2,\mu}$ | the general quaternionic bilinear form; polar form of the algebraic norm |
| $Z_0,\dots,Z_3$ | Linear coordinates in which the form is $Z_0Z_3 - Z_1Z_2$ |
| $\mathbb{P}(\mathcal{N}) = Q^2 \cong \mathbb{P}^1 \times \mathbb{P}^1$ | Projectivised null cone, the Segre quadric |
| $s : \mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^3$ | Segre embedding, $([u],[v]) \mapsto [\alpha\gamma:\alpha\delta:\beta\gamma:\beta\delta]$ |
| $[u] = [\alpha:\beta]$, $[v] = [\gamma:\delta]$ | The two factors of a null point, up to $(u,v)\mapsto(\lambda u,\lambda^{-1}v)$ |
| $W_{[u]}$, $W^{[v]}$ | The two families of maximal isotropic null planes |
| $\ell_{[u]}, m_{[v]}$ | The two rulings of $Q^2$ |
| $\Delta^\pm$ | The two chiral spinor spaces, $\dim_{\mathbb{C}}\Delta^\pm=2$ |
| $A_\alpha{}^{\bar\beta}=\phi_\alpha\pi^{\bar\beta}$ | Factorisation of a null biquaternion; $\ell_{[\phi]}\cong\mathbb{P}(\Delta^-)$, $m_{[\pi]}\cong\mathbb{P}(\Delta^+)$ |
| $\mathbb{M}_+\cong\mathbb{R}^{1,3}$, $\mathbb{M}_-\cong\mathbb{R}^{3,1}$ | The Lorentzian real slices; their null cones are real cones of dimension $3$ |
| $\mathbb{P}(\mathcal{N}\cap\mathbb{M}_+)\cong S^2$ | The celestial sphere, a real slice of $Q^2$ |
| $O(2,4)\supset SO(4,2)$, $SU(2,2)\cong Spin(4,2)$ | The conformal group of Lorentzian space and its double cover |
| $S^1\times S^1$ | Real quadric of the split form of signature $(2,2)$, ruled by real lines |
| $p_{ij} = Q_{2,i}Q_{1,j}-Q_{2,j}Q_{1,i}$ | Plücker coordinates; the Klein quadric in $\mathbb{P}^5$ is their Plücker locus |
| $[\tilde Q_1]^{\perp}$ | Polar hyperplane of $[\tilde Q_1]$; the tangent hyperplane when $[\tilde Q_1] \in Q^2$ |
| $\operatorname{Aut}(Q^2) \cong PO_4(\mathbb{C})$ | Projective automorphisms of the quadric |
| $\mathbb{P}^3\setminus Q^2 \cong PGL(2,\mathbb{C}) \cong SO^+(1,3)$ | Complement of the quadric, the Lorentz group as an open submanifold of $\mathbb{P}^3$ |

## Further Reading

- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* **4** (1873) 381–395.
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992).
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978).
- Igor R. Shafarevich, *Basic Algebraic Geometry 1: Varieties in Projective Space* (Springer, 3rd ed., 2013).
- P. Anglès, *Conformal Groups in Geometry and Spin Structures* (Birkhäuser, 2008).
- J. P. Ward, *Quaternions and Cayley Numbers: Algebra and Applications* (Kluwer, 1997).
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991).
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995).
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989).
