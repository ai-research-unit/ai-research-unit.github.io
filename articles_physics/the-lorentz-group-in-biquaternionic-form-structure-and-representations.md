# __The Lorentz Group in Biquaternionic Form — Structure and Representations__

## Introduction

The companion articles have developed the biquaternion description of a single Lorentz transformation and of the spinor module on which the Lorentz group acts. The present article treats the Lorentz group as an algebraic object in its own right. Its subject is the **group structure**, the **Lie algebra**, and the **representation theory** of the group of unit-norm biquaternions and of the group of units that contains it, finite-dimensional and unitary. The parametrisation of one transformation, and the construction of the spinor module with its one-sided action, are used here but not re-derived; they belong to the companions cited below.

Three questions organize the discussion.

**Composition.** A pure rotation and a pure boost are both unit-norm biquaternions, but only the rotations close under multiplication. The product of two boosts is, in general, a boost together with a rotation. The angle of that rotation is the **Thomas–Wigner rotation**, and it is the group-theoretic root of the non-commutativity of the boosts. This is the content of the composition law.

**Infinitesimal structure.** The Lie algebra of the group of unit-norm biquaternions is the real Lie algebra $\mathrm{SL}(2,\mathbb{C})$ of traceless $2\times2$ complex matrices. Its complexification splits into two commuting copies of $\mathrm{SU}(2)$. The rotation generators and the boost generators sit in the real algebra in a definite way, and the failure of the boosts to close is visible in the bracket of two boost generators.

**Representations.** The group of units is $GL_2(\mathbb{C})$, the group of invertible biquaternions, with the unit-norm group $SL(2,\mathbb{C})$ as its kernel of the norm. The finite-dimensional irreducible representations are labelled by a pair $(m,n)$ of half-integers, of dimension $(2m+1)(2n+1)$. The biquaternion algebra itself carries the four-dimensional vector representation $(\tfrac12,\tfrac12)$; the two Weyl spinors are $(\tfrac12,0)$ and $(0,\tfrac12)$. The two-to-one cover of the Lorentz group by $SL(2,\mathbb{C})$ determines which of these representations descend to the Lorentz group and which are genuine spin representations. Unitarity is preserved by complexification only for the compact subgroup, so the unitary representations of the non-compact group are the infinite-dimensional principal and complementary series.

The conventions are those of the companion articles. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$ and $e_1e_2=e_3$, and the scalar imaginary is $i$, which commutes with the quaternion units. The anti-Hermitian and Hermitian subspaces are
$$
\mathbb{M}_-=\{\tilde{Q}:\tilde{Q}^{*}=-\tilde{Q}\},\qquad
\mathbb{M}_+=\{\tilde{Q}:\tilde{Q}^{*}=\tilde{Q}\},
$$
and $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace, the fixed-point set of complex conjugation. Throughout, $c$ denotes the speed of light in the medium, $c=1/\sqrt{\epsilon\mu}$, and $c_0$ the vacuum speed of light. The symbol $\mathbf{u}$ (or $\hat{\mathbf{u}}$) denotes a boost direction and $\psi$ a rapidity.

## Rotors, Boosts, and Rotations

A **Lorentz rotor** is a biquaternion of unit norm,
$$
\tilde{\Lambda}\in\mathbb{B},\qquad \tilde{\Lambda}\tilde{\Lambda}^{\natural}=e_0,
$$
where $\tilde{\Lambda}^{\natural}$ is the quaternion conjugate. It acts on the material sector $\mathbb{M}_-$ by **rotor conjugation**
$$
\tilde{Q}\ \longmapsto\ \tilde{\Lambda}\,\tilde{Q}\,\tilde{\Lambda}^{*},\qquad \tilde{Q}\in\mathbb{M}_-.
$$
The set of unit-norm biquaternions is a group under biquaternion multiplication; under the algebra isomorphism $\mathsf{M}_2:\mathbb{B}\to M_2(\mathbb{C})$ (with $\mathsf{M}_2(e_k)=-i\sigma_k$ and $\mathsf{M}_2(i)=iI_2$) it is exactly
$$
SL(2,\mathbb{C})=\{\tilde{\Lambda}\in\mathbb{B}:\tilde{\Lambda}\tilde{\Lambda}^{\natural}=e_0\}
\;\cong\;\{g\in M_2(\mathbb{C}):\det g=1\},
$$
because the biquaternion norm is the determinant, $N(\tilde{Q}) = \langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\tilde{Q}\tilde{Q}^{\natural}=\det\mathsf{M}_2(\tilde{Q})$ (see the companion article on the biquaternion algebra and its matrix representation).

Two families of rotors have a direct geometric meaning.

A **pure boost** along the unit direction $\hat{\mathbf{u}}\in\mathbb{H}_{\mathbb{B}}$ (a pure real unit quaternion, $\hat{\mathbf{u}}^2=-e_0$) with **rapidity** $\psi$ is
$$
\tilde{\Lambda}=\exp\!\left(\frac{\psi}{2}\,i\hat{\mathbf{u}}\right)
=\cosh\frac{\psi}{2}+i\sinh\frac{\psi}{2}\,\hat{\mathbf{u}},
\qquad \tanh\psi=\frac{u}{c},
$$
where $u=|\mathbf{u}|$ is the speed of the boosted frame. It is Hermitian, $\tilde{\Lambda}^{*}=\tilde{\Lambda}$, hence lies in $\mathbb{M}_+$, and it has unit norm. A **pure spatial rotation** about $\hat{\mathbf{n}}\in\mathbb{H}_{\mathbb{B}}$ by angle $\theta$ is
$$
\tilde{R}=\exp\!\left(\frac{\theta}{2}\,\hat{\mathbf{n}}\right)
=\cos\frac{\theta}{2}+\sin\frac{\theta}{2}\,\hat{\mathbf{n}},
$$
a real quaternion of unit norm, lying in $\mathbb{H}_{\mathbb{B}}$. The distinction between the two is exactly the factor of $i$ in the vector part: $(\hat{\mathbf n})^2=-e_0$ for a rotation, $(i\hat{\mathbf u})^2=+e_0$ for a boost.

The group $\mathsf{M}_2^{-1}(SU(2))=SL(2,\mathbb{C})\cap\mathbb{H}_{\mathbb{B}}$ of unit real quaternions is the group of rotations; it is the double cover of $SO(3)$. The sets
$$
\mathcal{B}=\{\text{Hermitian unit-norm biquaternions}\}\subset\mathbb{M}_+,
\qquad
\mathcal{R}=SU(2)\subset\mathbb{H}_{\mathbb{B}}
$$
are the boosts and the rotations. The parametrisation of a single transformation by a rotor, its verification against the standard component formulas, and the relation $\tilde{\Lambda}=\sqrt{-(i/c)\tilde{U}^{\natural}}$ between a boost rotor and a four-velocity $\tilde{U}$ are established in the companion article *The Lorentz Transformation as a Biquaternionic Rotation*; they are not repeated here.

## The Group of Unit-Norm Biquaternions

This section collects the group-theoretic facts that do not depend on the detailed parametrisation.

**Group law.** The product of two unit-norm biquaternions is again of unit norm, because the biquaternion norm is multiplicative:
$$
N(\tilde{\Lambda}_1\tilde{\Lambda}_2)=N(\tilde{\Lambda}_1)N(\tilde{\Lambda}_2)=e_0 .
$$
The identity is $e_0$, and the inverse is the quaternion conjugate,
$$
\tilde{\Lambda}^{-1}=\tilde{\Lambda}^{\natural},
$$
since $\tilde{\Lambda}\tilde{\Lambda}^{\natural}=\tilde{\Lambda}^{\natural}\tilde{\Lambda}=N(\tilde{\Lambda})=e_0$; the biquaternion norm of a biquaternion is central, so the two-sided inverse is the quaternion conjugate. For a boost this gives $\tilde{\Lambda}(\hat{\mathbf u},\psi)^{-1}=\tilde{\Lambda}(\hat{\mathbf u},-\psi)=\tilde{\Lambda}^{\natural}$, and for a rotation $\tilde{R}(\hat{\mathbf n},\theta)^{-1}=\tilde{R}(\hat{\mathbf n},-\theta)$.

**Dimension and topology.** As a real Lie group, $SL(2,\mathbb{C})$ has real dimension $6$ (complex dimension $3$); its maximal compact subgroup is $SU(2)$, the rotation group. It is connected and simply connected. These facts belong to the companion articles on the exponential and on biquaternion topology; the relevant consequence is used below.

**The action and its kernel.** Rotor conjugation defines a map
$$
\mathrm{Ad}:\ SL(2,\mathbb{C})\longrightarrow SO^+(1,3),\qquad
\mathrm{Ad}(\tilde{\Lambda}):\ \tilde{Q}\longmapsto \tilde{\Lambda}\tilde{Q}\tilde{\Lambda}^{*} ,
$$
into the restricted (proper orthochronous) Lorentz group. It is well defined because the conjugate of an anti-Hermitian element is anti-Hermitian, it preserves the biquaternion norm, and it is a group homomorphism:
$$
\mathrm{Ad}(\tilde{\Lambda}_2\tilde{\Lambda}_1)=\mathrm{Ad}(\tilde{\Lambda}_2)\circ\mathrm{Ad}(\tilde{\Lambda}_1),
$$
as follows from $(\tilde{\Lambda}_2\tilde{\Lambda}_1)\tilde{Q}(\tilde{\Lambda}_2\tilde{\Lambda}_1)^{*}=\tilde{\Lambda}_2(\tilde{\Lambda}_1\tilde{Q}\tilde{\Lambda}_1^{*})\tilde{\Lambda}_2^{*}$. Its kernel is
$$
\ker\mathrm{Ad}=\{\pm e_0\}\cong\mathbb{Z}/2\mathbb{Z},
$$
because $-e_0$ is central and the two signs cancel in a conjugation. Hence
$$
SO^+(1,3)\cong SL(2,\mathbb{C})/\{\pm e_0\},
$$
and $\mathrm{Ad}$ is a two-to-one covering homomorphism. The detailed proof, together with the contrast between the two-sided four-vector action and the one-sided spinor action, is the subject of the companion article *The Biquaternion Spinor Module and Its Lorentz Action*.

**The rotation subgroup and the boosts.** The rotations $\mathcal{R}=SU(2)$ are a subgroup. The boosts $\mathcal{B}$ are not: they are closed under inverse but not under multiplication, as the next two sections show. The set $\mathcal{B}$ is instead a symmetric submanifold of $SL(2,\mathbb{C})$ of dimension $3$. The group is generated by its boosts and rotations: every unit-norm biquaternion admits a decomposition
$$
\tilde{\Lambda}=\tilde{B}\,\tilde{R},
\qquad \tilde{B}\in\mathcal{B},\quad \tilde{R}\in SU(2),
$$
unique if $\tilde{B}$ is required to have positive-definite matrix image; equivalently, $\mathcal{B}\cong SL(2,\mathbb{C})/SU(2)$. This is the **Cartan (polar) decomposition**, and it parametrises a general transformation by three boost parameters (the rapidity vector) and three rotation parameters (the axis and angle), matching the six real dimensions of the group.

## The Group of Units and Its Representations

The unit-norm group is the kernel of the norm inside the full group of units. The **group of units** is
$$
\mathbb{B}^{\times}=\{\tilde{Q}:N(\tilde{Q})\neq0\}\cong GL_2(\mathbb{C}),
$$
the group of invertible matrices under $\mathsf{M}_2$, of real dimension $8$, with centre $\mathbb{C}^{\times}$; the unit-norm subgroup $SL(2,\mathbb{C})=\mathbb{B}^{\times}_1$ is the kernel of the norm, and the unitary biquaternions $\tilde{Q}^{*}\tilde{Q}=e_0$ form the maximal compact subgroup $U(2)$.

Physically the unit group is the whole linear group of the framework: $GL_2(\mathbb{C})$ is the group of invertible biquaternions, its centre $\mathbb{C}^{\times}$ is the complex phase that every conjugation ignores and the norm only sees through its modulus, and the unit-norm subgroup is the Lorentz group of the preceding sections.

**Representations of the unit group.** As a reductive group, $GL_2(\mathbb{C})$ has finite-dimensional algebraic (rational) representations parameterised by highest weights $(\lambda_1,\lambda_2)\in\mathbb{Z}^2$ with $\lambda_1\geq\lambda_2$; the irreducible one is $\operatorname{Sym}^{\lambda_1-\lambda_2}(\mathbb{C}^2)\otimes(\det)^{\lambda_2}$, of dimension $\lambda_1-\lambda_2+1$, with central character $z\mapsto z^{\lambda_1+\lambda_2}$. Restriction to $SL(2,\mathbb{C})$ forgets the determinant twist, leaving the highest weight $2j=\lambda_1-\lambda_2\geq0$, that is, the irreducible $V_j$ below with spin $j\in\tfrac12\mathbb{Z}_{\geq0}$.

## Boosts Do Not Close: The Composition Law

The elementary reason that the boosts do not form a subgroup is visible in the product of two boost rotors. Let
$$
\tilde{\Lambda}_1=\cosh\frac{\psi_1}{2}+i\sinh\frac{\psi_1}{2}\hat{\mathbf u}_1,
\qquad
\tilde{\Lambda}_2=\cosh\frac{\psi_2}{2}+i\sinh\frac{\psi_2}{2}\hat{\mathbf u}_2,
$$
and write $c_i=\cosh(\psi_i/2)$, $s_i=\sinh(\psi_i/2)$. Using $\hat{\mathbf u}_1\hat{\mathbf u}_2=-\,\hat{\mathbf u}_1\cdot\hat{\mathbf u}_2+\hat{\mathbf u}_1\times\hat{\mathbf u}_2$ for pure real unit quaternions, the product is
$$
\tilde{\Lambda}_1\tilde{\Lambda}_2
= \underbrace{\bigl(c_1c_2+s_1s_2\,\hat{\mathbf u}_1\cdot\hat{\mathbf u}_2\bigr)
+ i\bigl(c_1s_2\,\hat{\mathbf u}_2+s_1c_2\,\hat{\mathbf u}_1\bigr)}_{\text{Hermitian part}}
\;-\;\underbrace{s_1s_2\,\hat{\mathbf u}_1\times\hat{\mathbf u}_2}_{\text{anti-Hermitian part}} .
$$
The first line is Hermitian: it is a real scalar plus a purely imaginary vector. The second line is a real vector, hence anti-Hermitian. Therefore the product is Hermitian — that is, a boost — **if and only if** the anti-Hermitian part vanishes,
$$
\hat{\mathbf u}_1\times\hat{\mathbf u}_2=0,
$$
i.e. if and only if the two boosts are collinear (or one of the rapidities vanishes). Since $\tilde{\Lambda}_1,\tilde{\Lambda}_2$ are Hermitian, the product is Hermitian exactly when the two rotors commute, and two boost rotors commute exactly when their directions are parallel. So:

> Two boosts combine to a boost exactly when they are collinear. Otherwise their product is a boost together with a rotation.

This is the **non-closure of the boosts** at the level of the group. Its infinitesimal shadow, $[K_j,K_k]\neq0$, appears in the Lie algebra section below.

**The Thomas–Wigner rotation.** Since every unit-norm biquaternion has a unique polar decomposition, the product can be written
$$
\tilde{\Lambda}_1\tilde{\Lambda}_2=\tilde{B}\,\tilde{R},
\qquad \tilde{B}\in\mathcal{B},\quad \tilde{R}\in SU(2).
$$
The factor $\tilde{B}$ is a boost; the factor $\tilde{R}$ is the **Thomas–Wigner rotation**. If $\theta\in[0,\pi]$ is the angle between the two boost directions, the rotation angle $\delta$ is determined by
$$
\boxed{\ \tan\frac{\delta}{2}
=\frac{\sinh\frac{\psi_1}{2}\,\sinh\frac{\psi_2}{2}\,\sin\theta}
{\cosh\frac{\psi_1}{2}\,\cosh\frac{\psi_2}{2}
+\sinh\frac{\psi_1}{2}\,\sinh\frac{\psi_2}{2}\,\cos\theta}\ }
$$
and the rotation axis is the line through $\hat{\mathbf u}_1\times\hat{\mathbf u}_2$. With the rotation rotor written as $\tilde{R}=\cos(\delta/2)+\sin(\delta/2)\hat{\mathbf n}$, the axis for the product $\tilde{\Lambda}_1\tilde{\Lambda}_2$ in the order written is
$$
\hat{\mathbf n}=-\frac{\hat{\mathbf u}_1\times\hat{\mathbf u}_2}{|\hat{\mathbf u}_1\times\hat{\mathbf u}_2|};
$$
reversing the order of the two boosts reverses the sense of the rotation, while leaving the angle $\delta$ unchanged.

The boost factor $\tilde B$ has rapidity $\psi_{\mathrm c}$ fixed by the usual composite-rapidity relation
$$
\cosh\psi_{\mathrm c}
=\cosh\psi_1\cosh\psi_2+\sinh\psi_1\sinh\psi_2\cos\theta ,
$$
that is, the rapidity of the relativistic composition of the two boost velocities. The rotation factor is the obstruction to the composed transformation being a pure boost.

Several special cases are worth recording.

- **Collinear boosts** ($\theta=0$ or $\theta=\pi$): $\sin\theta=0$, so $\delta=0$ and the product is a pure boost. For $\theta=0$ the rapidities add, $\psi_{\mathrm c}=\psi_1+\psi_2$; for $\theta=\pi$ they subtract, $\psi_{\mathrm c}=|\psi_1-\psi_2|$. In both cases rapidities combine exactly as for collinear velocities.
- **One trivial boost** ($\psi_1=0$ or $\psi_2=0$): $\delta=0$, as it must be.
- **Small velocities.** For $v_1,v_2\ll c$, expanding the formula gives
$$
\delta\approx\frac{1}{2}\frac{|\mathbf v_1\times\mathbf v_2|}{c^2},
$$
the familiar leading Thomas-precession angle. For two boosts of $0.01\,c$ at right angles this gives $\delta\approx5.0\times10^{-5}$ rad.
- **Large rapidities.** If $\psi_1,\psi_2\to\infty$ at fixed $\theta\in(0,\pi)$, the formula gives $\tan(\delta/2)\to\tan(\theta/2)$, hence $\delta\to\theta$. The limiting Wigner angle is the angle between the two boost directions.

The composition law of a boost $\tilde B$ and a rotation $\tilde R$ is immediate: $\tilde B\tilde R$ and $\tilde R\tilde B$ are both unit-norm biquaternions and both correspond to general Lorentz transformations, but they are generally different elements of the group, differing by the rotation $\tilde R^{-1}\tilde B^{-1}\tilde R\tilde B$; the non-commutativity of boosts and rotations is the group-level statement of the same non-closure.

## The Lie Algebra

The Lie algebra of $SL(2,\mathbb{C})$, viewed as a **real** Lie algebra, is the space of traceless $2\times2$ complex matrices,
$$
\mathrm{G}=\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}
=\{M\in M_2(\mathbb{C}):\operatorname{tr}M=0\},
$$
of real dimension $6$. In the biquaternion basis it is
$$
\mathrm{G}=\operatorname{span}_{\mathbb{R}}\{e_1,e_2,e_3\}\ \oplus\ \operatorname{span}_{\mathbb{R}}\{ie_1,ie_2,ie_3\},
$$
the first summand being the **rotation generators** (anti-Hermitian, in $\mathbb{H}_{\mathbb{B}}$) and the second the **boost generators** (Hermitian, in $\mathbb{M}_+$). Write
$$
J_k=e_k,\qquad K_k=i e_k \qquad (k=1,2,3),
$$
so that $J_k$ generate rotations and $K_k$ generate boosts. With $\varepsilon_{jkl}$ the Levi-Civita symbol ($e_1e_2=e_3$), the commutation relations, computed by direct expansion in the quaternion basis, are
$$
[J_j,J_k]=2\varepsilon_{jkl}J_l,\qquad
[J_j,K_k]=2\varepsilon_{jkl}K_l,\qquad
[K_j,K_k]=-2\varepsilon_{jkl}J_l .
$$
The first two say that the rotations form a subalgebra $\mathrm{SU}(2)\cong\mathrm{SO}(3)$ (the compact part) and that the boosts transform as a vector under it. The third is the infinitesimal statement that **the boosts do not close**: the bracket of two boost generators is a rotation generator. This is the Lie-algebraic origin of the Thomas–Wigner rotation and of the non-closure of the preceding section.

**Relation to $\mathrm{SO}(1,3)$ and to $\mathrm{SL}(2,\mathbb{C})$.** The real Lie algebra $\mathrm{G}$ is isomorphic to the Lie algebra $\mathrm{SO}(1,3)$ of the Lorentz group, the isomorphism being the infinitesimal form of $\mathrm{Ad}$. It is also, by definition, the real Lie algebra underlying the complex Lie algebra $\mathrm{SL}(2,\mathbb{C})$. The exponential map $\exp:\mathrm{G}\to SL(2,\mathbb{C})$ is neither injective nor surjective. It is not injective: an element $M$ maps to $e_0$ exactly when it is diagonalisable with eigenvalues in $2\pi i\mathbb{Z}$, so the preimage of $e_0$ is nonzero — indeed a union of conjugacy classes, not a discrete set. It is not surjective either: for example, a matrix with a nontrivial Jordan block and eigenvalue $-1$ is not the exponential of any traceless matrix. What is true is that every unit-norm biquaternion is a **product** of exponentials, because the group is connected and $\exp$ is a local diffeomorphism at the identity. The Cartan decomposition makes this explicit: a boost is the exponential of a boost generator and a rotation is the exponential of a rotation generator, so every rotor is
$$
\tilde{\Lambda}=\exp(M)\exp(N),\qquad
M\in\operatorname{span}_{\mathbb{R}}\{K_1,K_2,K_3\},\quad
Y\in\operatorname{span}_{\mathbb{R}}\{J_1,J_2,J_3\}.
$$
The exponential map and its failure of surjectivity are treated in the companion article on the biquaternion exponential.

**The Killing form.** The Lie algebra is semisimple, and its Killing form is nondegenerate. In the basis $(J_1,J_2,J_3,K_1,K_2,K_3)$ it is diagonal,
$$
B(J_j,J_k)=-16\,\delta_{jk},\qquad
B(K_j,K_k)=+16\,\delta_{jk},\qquad
B(J_j,K_k)=0,
$$
(computed from $B(M,N)=\operatorname{tr}(\operatorname{ad}M\,\operatorname{ad}N)$ in this algebra). Its signature is therefore $(3,3)$: negative definite on the compact rotation subalgebra and positive definite on the complementary boost directions. The indefiniteness is the Lie-algebraic expression of the non-compactness of $SL(2,\mathbb{C})$ and of the Lorentz group.

## The Two $\mathrm{SU}(2)$ Halves

The complexification of the real Lie algebra $\mathrm{G}$ splits. Let $\mathsf{i}$ denote the **complexification unit**, which is a formal scalar and is not the scalar imaginary $i\in\mathbb{B}$. Define
$$
N_k^{\pm}=\frac{1}{2}\bigl(J_k\pm \mathsf{i}\,K_k\bigr)
=\frac{1}{2}\bigl(e_k\pm \mathsf{i}\,(i e_k)\bigr),\qquad k=1,2,3 .
$$
A direct computation using the commutation relations above gives
$$
[N_j^+,N_k^+]=2\varepsilon_{jkl}N_l^+,\qquad
[N_j^-,N_k^-]=2\varepsilon_{jkl}N_l^-,\qquad
[N_j^+,N_k^-]=0 .
$$
Thus the complexified algebra is a direct sum of two commuting three-dimensional complex Lie algebras, each isomorphic to the complexification of $\mathrm{SU}(2)$:
$$
\mathrm{G}\otimes_{\mathbb{R}}\mathbb{C}
\;\cong\;\mathrm{SL}(2,\mathbb{C})\oplus\mathrm{SL}(2,\mathbb{C})
\;\cong\;\mathrm{SU}(2)_{\mathbb{C}}\oplus\mathrm{SU}(2)_{\mathbb{C}} .
$$
The two summands are the **self-dual** and **anti-self-dual** halves of the complexified Lorentz algebra. The rotation generators are the diagonal combination,
$$
J_k=N_k^++N_k^-,
$$
and the boost generators are the off-diagonal combination,
$$
K_k=\frac{1}{\mathsf{i}}\bigl(N_k^+-N_k^-\bigr).
$$
So a rotation is a simultaneous equal rotation in the two $\mathrm{SU}(2)$ factors, while a boost is a rotation in one factor and an opposite rotation in the other. This is the algebraic reason why the spatial rotation group is compact and the boosts are not: rotations act in the same sense in both factors, boosts in opposite senses.

Two remarks belong here.

**Complexification, not the algebra itself.** Unlike a real form such as $\mathrm{SU}(2)\oplus\mathrm{SU}(2)$, the real algebra $\mathrm{G}$ is simple: it is not itself a sum of two ideals. The splitting occurs only after complexification. Concretely, an element of $\mathrm{G}\otimes_{\mathbb{R}}\mathbb{C}$ is a formal combination of $e_k$ and $i e_k$ with complex coefficients, and the combinations $N_k^\pm$ require the formal unit $\mathsf{i}$, which must be distinguished from the scalar imaginary $i$ already present in $\mathbb{B}$ and in the boost generators $K_k=ie_k$.

**Parity.** The two factors are exchanged by parity, $N_k^+\leftrightarrow N_k^-$, which is an outer automorphism of the Lorentz group and not an element of $SO^+(1,3)$. Correspondingly, a representation labelled $(m,n)$ is sent to $(n,m)$ by parity. This is the algebraic origin of the chirality of the Weyl spinors.

## Finite-Dimensional Representations

A finite-dimensional representation of the Lorentz group is a continuous homomorphism $SO^+(1,3)\to GL(V)$, or equivalently — because every such representation lifts — a representation of the double cover $SL(2,\mathbb{C})$ that is trivial on $\{\pm e_0\}$ (see the next section). Complex representations of the compact subgroup $SU(2)$ are completely reducible, and the same holds for $SL(2,\mathbb{C})$; so it suffices to describe the irreducible ones.

**The label $(m,n)$.** Let $V_j$ denote the irreducible $\mathrm{SU}(2)$-module of dimension $2j+1$, $j\in\tfrac12\mathbb{Z}_{\geq0}$, i.e. the symmetric power $\operatorname{Sym}^{2j}(\mathbb{C}^2)$ in the matrix realisation. The finite-dimensional irreducible representations of $SL(2,\mathbb{C})$ are the outer tensor products
$$
(m,n)=V_m\boxtimes V_n,\qquad m,n\in\tfrac12\mathbb{Z}_{\geq0},
\qquad
\dim_{\mathbb{C}}(m,n)=(2m+1)(2n+1).
$$
Equivalently, writing $m=j_1$, $n=j_2$, the labels $(j_1,j_2)$ are the highest weights of the two $\mathrm{SU}(2)$ halves of the preceding section. The first index refers to the holomorphic (self-dual) half and the second to the antiholomorphic (anti-self-dual) half.

**Dictionary.** The low-lying representations have direct interpretations in the biquaternion framework.

| Representation | Dimension | Object |
|---|---|---|
| $(0,0)$ | $1$ | Lorentz scalar |
| $(\tfrac12,0)$ | $2$ | left-handed Weyl spinor |
| $(0,\tfrac12)$ | $2$ | right-handed Weyl spinor |
| $(\tfrac12,\tfrac12)$ | $4$ | four-vector (the biquaternion algebra as a module) |
| $(1,0)$ | $3$ | self-dual antisymmetric 2-form |
| $(0,1)$ | $3$ | anti-self-dual antisymmetric 2-form |
| $(1,0)\oplus(0,1)$ | $6$ | adjoint representation |
| $(1,1)$ | $9$ | symmetric traceless rank-2 tensor |

The Dirac spinor is the direct sum $(\tfrac12,0)\oplus(0,\tfrac12)$, of dimension $4$. The electromagnetic field strength, a rank-2 antisymmetric tensor, decomposes into its self-dual and anti-self-dual parts, transforming as $(1,0)$ and $(0,1)$; this is the representation-theoretic content of the complex combination $\mathbf E+i\mathbf B$. The adjoint representation of the Lorentz algebra is $(1,0)\oplus(0,1)$, of dimension $6$, matching the six generators of the Lie algebra.

**Restriction to rotations.** Under the maximal compact subgroup $SU(2)\subset SL(2,\mathbb{C})$ the representation $(m,n)$ restricts as
$$
(m,n)\big|_{SU(2)}\;\cong\;V_m\otimes V_n ,
$$
which decomposes by the Clebsch–Gordan rule into $\mathrm{SU}(2)$-irreps. For example,
$$
(\tfrac12,\tfrac12)\big|_{SU(2)}\cong V_{\tfrac12}\otimes V_{\tfrac12}\cong V_1\oplus V_0,
$$
i.e. $3\oplus1$: under spatial rotations the four-vector splits into a spatial vector (three components) and a scalar (the time component). This is the representation-theoretic statement that rotations do not mix time with space. The Clebsch–Gordan rule and the tensor products of the $(m,n)$ are developed in the companion article on biquaternion representation theory.

**Complete reducibility and tensor products.** Every finite-dimensional representation is a direct sum of irreducibles, and the tensor product of two irreducibles decomposes by the product of the two $\mathrm{SU}(2)$ Clebsch–Gordan rules:
$$
(m,n)\otimes(m',n')\;\cong\;\bigoplus_{k=0}^{2\min(m,m')}\ \bigoplus_{k'=0}^{2\min(n,n')}\bigl(m+m'-k,\,n+n'-k'\bigr),
$$
the sums running over integer steps. For instance,
$$
(\tfrac12,\tfrac12)\otimes(\tfrac12,\tfrac12)\cong(0,0)\oplus(1,0)\oplus(0,1)\oplus(1,1),
$$
of dimension $1+3+3+9=16=4\times4$.

**Polynomial representations and the unitary trick.** The finite-dimensional irreducibles of the complex group are exactly the **polynomial** (equivalently holomorphic, equivalently algebraic) ones: the matrix entries are polynomial in the entries of the group element, and such representations are the symmetric powers $V_j=\operatorname{Sym}^{2j}(\mathbb{C}^2)$ of the defining module, of highest weight $2j$ and spin $j$. Restriction to the maximal compact subgroup $SU(2)$ is an equivalence of categories, the **unitary trick**,
$$
\left\{\text{f.d. polynomial representations of }SL(2,\mathbb{C})\right\}\simeq\left\{\text{f.d. unitary representations of }SU(2)\right\},
$$
complexifying the Lie algebra and exponentiating; the two sides are parameterised by the same highest weights. What the unitary trick does not carry across is unitarity for the non-compact group itself, a point taken up in §*Unitary Representations*.

**Tensor powers of the spinor.** Iterating the Clebsch–Gordan rule decomposes the $N$-fold tensor power of the defining module,
$$
V_{1/2}^{\otimes N}\cong\bigoplus_{k=0}^{\lfloor N/2\rfloor}\left[\binom Nk-\binom N{k-1}\right]V_{N/2-k},
$$
the multiplicity of $V_{N/2-k}$ being the ballot (Catalan-triangle) number $\binom Nk-\binom N{k-1}$.

**Physical reading: addition of angular momenta.** The Clebsch–Gordan rule is the quantum rule for combining two angular momenta: $V_j\otimes V_k$ is the state space of a composite system whose parts carry spins $j$ and $k$, and the decomposition lists its total-spin sectors. The case $V_{1/2}\otimes V_{1/2}\cong V_1\oplus V_0$ is the addition of two spin-$\tfrac12$ particles into a triplet and a singlet, and $V_{1/2}^{\otimes3}\cong V_{3/2}\oplus2V_{1/2}$ is the quartet and the two doublets of three; the ballot numbers are the multiplicities with which each total spin occurs. The invariant $\varepsilon$ that produces the scalar $V_0$ is the antisymmetric two-particle state, the singlet of the framework.

**The defining representation and its two dualities.** The defining module $V_{1/2}=\mathbb{C}^2$ is **self-dual** for $SL(2,\mathbb{C})$: since the determinant is one, the alternating form $\varepsilon(u,v)=u_1v_2-u_2v_1$ is invariant and identifies $V_{1/2}^{*}$ with $V_{1/2}$. Its **conjugate** $\overline{V_{1/2}}=(0,\tfrac12)$ is a different, inequivalent representation — the other chirality — and parity exchanges the two; the direct sum is the Dirac spinor $\Delta=(\tfrac12,0)\oplus(0,\tfrac12)$ of the dictionary, and the tensor product is the four-vector representation $V_{1/2}\otimes\overline{V_{1/2}}\cong(\tfrac12,\tfrac12)$.

**Physical reading: the one-particle module and the chiral fields.** The defining module is the **one-particle module**: a state of a biquaternion field is a section of it or of its conjugate, which is why the framework carries a Dirac pair rather than a single Weyl spinor, and why the mass term, which couples the two chiralities, is a parity-respecting bilinear. The two inequivalent representations are the two chiralities of a massless spin-$\tfrac12$ field, and the non-descent of the half-integral representations to $SO^+(1,3)$ is the spinor double cover.

## Where the Biquaternion Algebra Sits

The biquaternion algebra is not merely the home of the rotors; it is itself a representation of the group it defines. Three distinct structures should be distinguished.

**As the vector representation.** Under the conjugation action
$$
\tilde{Q}\ \longmapsto\ \tilde{\Lambda}\,\tilde{Q}\,\tilde{\Lambda}^{*},
\qquad \tilde{Q}\in\mathbb{B},\quad \tilde{\Lambda}\in SL(2,\mathbb{C}),
$$
the four-complex-dimensional algebra $\mathbb{B}\cong M_2(\mathbb{C})$ carries the irreducible representation
$$
\mathbb{B}\;\cong\;M_2(\mathbb{C})\;\cong\;S\otimes\bar S\;\cong\;(\tfrac12,\tfrac12),
$$
where $S=\mathbb{C}^2$ is the defining (left-handed) module and $\bar S$ its conjugate. The material subspace $\mathbb{M}_-$ is a real form of this complex representation: complexifying it gives $\mathbb{M}_-\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{B}$, and the anti-Hermitian elements are exactly the four-vectors of the companion articles. In this sense the biquaternion algebra **is** the complexified four-vector representation, and $\mathbb{M}_-$ is its real slice.

**As the defining module, twice.** Regarded instead as a left module over itself and acted on by left multiplication, the algebra decomposes as
$$
\mathbb{B}\;\cong\;S\oplus S\;\cong\;(\tfrac12,0)\oplus(\tfrac12,0),
$$
two copies of the defining representation. This is the module structure behind the identification $\mathbb{B}\cong M_2(\mathbb{C})\cong\operatorname{End}_{\mathbb{C}}(S)$, and it is developed in the companion article on the spinor module. The point to keep in view is that the same algebra carries different representations depending on which action is used: left multiplication gives two copies of $(\tfrac12,0)$, while conjugation gives the single irreducible $(\tfrac12,\tfrac12)$.

**As the even Clifford algebra.** Finally, $\mathbb{B}\cong\mathrm{Cl}_{1,3}^{+}$ is the even subalgebra of the Clifford algebra of Minkowski space, and the spin group sits inside it,
$$
\operatorname{Spin}(1,3)\cong SL(2,\mathbb{C})\subset\mathbb{B}\subset \mathrm{Cl}_{1,3}.
$$
The spinor representation is the restriction of the Clifford module to the even subalgebra, which is why its action is one-sided; the four-vector representation is the signed inner conjugation action on the odd part, which is why it is two-sided. This correspondence is the algebraic origin of the whole structure and is treated in the companion article on the spinor module.

**The same group under other names.** The abstract group generated by the unit-norm biquaternions is the Lorentz group, and geometry knows it under three further names. In the relevant dimensions, up to the usual finite covers, it is the group of motions of hyperbolic space — the hyperboloid model of hyperbolic three-space is the orbit of a timelike vector under exactly the conjugation action above; it is the Möbius group $\mathrm{PSL}(2,\mathbb{C})$, the conformal group of the celestial sphere on which the rotors act by fractional linear transformations; and it is the Laguerre group of the plane, the stabiliser of the family of planes in the Lie sphere group of *Möbius and Lie Sphere Geometry*. The identifications are old, and the Laguerre one was pointed out by Cartan (1912) and Poincaré (1912). Naming them keeps the rotor picture of this article from being read as the only reading of the same group: rotor conjugation, the Möbius action on the celestial sphere, and the Laguerre action on oriented circles and planes are three presentations of one group, and the history of the geometry is older than the history of the physics.

## The Two-to-One Cover

The map $\mathrm{Ad}:SL(2,\mathbb{C})\to SO^+(1,3)$ has kernel $\{\pm e_0\}$. This single fact controls the representation theory.

Because $\mathrm{Ad}$ is two-to-one and surjective, the groups have the same Lie algebra but different global structure:
$$
SO^+(1,3)\cong SL(2,\mathbb{C})/\{\pm e_0\},
\qquad
\pi_1\bigl(SO^+(1,3)\bigr)\cong\mathbb{Z}/2\mathbb{Z},
$$
while $SL(2,\mathbb{C})$ is simply connected. The Lorentz group is doubly connected, and $SL(2,\mathbb{C})$ is its universal cover.

On a representation $(m,n)$, the central element $-e_0$ acts by the scalar
$$
(-1)^{2m+2n}=(-1)^{2(m+n)} .
$$
Consequently:

- If $m+n\in\mathbb{Z}$, the element $-e_0$ acts trivially, and the representation descends to a genuine representation of the Lorentz group $SO^+(1,3)$. This is the **integer-spin** (tensor) case: $(0,0)$, $(\tfrac12,\tfrac12)$, $(1,0)$, $(1,1)$, and so on.
- If $m+n\in\tfrac12+\mathbb{Z}$, the element $-e_0$ acts as $-\mathrm{id}$, and the representation does **not** descend: it is a genuine **spin representation** of the double cover $SL(2,\mathbb{C})$. This is the **half-integer-spin** case: $(\tfrac12,0)$, $(0,\tfrac12)$, $(\tfrac32,0)$, and so on.

The defining spinor $(\tfrac12,0)$ is the simplest example: $\mathsf{M}_2(-e_0)=-I_2$, so $\pm\tilde{\Lambda}$ act differently on every spinor, whereas they act identically on every four-vector. In particular a rotation by $2\pi$, which is $e_0$ in the four-vector representation, is $-e_0$ on the spinor module; a rotation by $4\pi$ is the identity on both. The spinor therefore carries a genuine two-valued representation, and the sign of a spinor is a degree of freedom invisible to any four-vector. The companion article on the spinor module develops the spinor action and the bilinear pairings in detail; the point recorded here is its representation-theoretic classification.

## Unitary Representations

A representation is **unitary** if it carries an invariant positive-definite Hermitian form. On the defining module $V_{1/2}=\mathbb{C}^2$ the standard Hermitian form is invariant under $SU(2)$, so $V_{1/2}$ is unitary for the compact form; it is **not** unitary for $SL(2,\mathbb{C})$, because the non-compact hyperbolic one-parameter subgroups — the boosts of the preceding sections — do not preserve any positive-definite form. More generally a non-compact simple group has no nontrivial finite-dimensional unitary representation, since the image would lie in a compact group. Hence the only finite-dimensional unitary representation of the Lorentz group is the trivial one, and no finite-dimensional representation carries a boost on a positive-definite state space.

**Physical reading: why the Lorentz action is not unitary.** Unitarity is what selects the representations that carry a positive-definite probability, so the statement that the finite-dimensional representations of $SL(2,\mathbb{C})$ are not unitary is the statement that a boost cannot be implemented by a finite-dimensional unitary operator: a boost is unbounded, and a finite-dimensional unitary representation of a non-compact group would have compact image. The parameter that makes a boost unbounded is the rapidity, and it is exactly the parameter that a finite multiplet cannot carry.

**The principal series.** Physics recovers unitarity by passing to infinite-dimensional representations. Let $P=MAN$ be the Borel subgroup of upper triangular matrices, with
$$
M=\{\operatorname{diag}(u,u^{-1}):|u|=1\}\cong U(1),\qquad
A=\{\operatorname{diag}(e^{t/2},e^{-t/2}):t\in\mathbb{R}\},
$$
and $N$ unipotent. For $m\in\mathbb{Z}$ and $\nu\in\mathbb{R}$ the unitary character $\chi_{m,\nu}(man)=u^me^{i\nu t}$ induces a unitary representation
$$
\pi_{m,\nu}=\operatorname{Ind}_P^G(\chi_{m,\nu}),
$$
the **principal series**: unitary by construction, irreducible for generic parameters and tempered for $\nu\in\mathbb{R}$, with $m$ a discrete parameter and $\nu$ a continuous one. Together with the **complementary series**, whose continuous parameter is purely imaginary and bounded, and the trivial representation, this is the unitary dual of $SL(2,\mathbb{C})$; the finite-dimensional polynomial representations are not in it, except for the trivial one. The compact subgroup $SU(2)$ supplies the finite-dimensional multiplets, and the passage from its discrete highest weights to the continuous parameter of the principal series is the complexification of the unitary dual.

Physically the principal series is the mode content of a field on the mass shell: the discrete parameter $m$ is the spin about the boost axis and the continuous parameter $\nu$ the rapidity of the boost, and the non-compact symmetry is realised on an infinite-dimensional space rather than on the finite multiplet of a compact group.

### The Stabilisers of a Direction and Their Series

The representations above are those of the full group $SL(2,\mathbb{C})$. A spinfoam boundary triangle uses a smaller group, and the smaller group's dual is of a different shape, so it is worth recording which subgroup and which series.

**A space-like direction.** The subgroup of $SL(2,\mathbb{C})$ fixing a **space-like** vector of the three-dimensional Lorentzian subspace $\mathbb{R}^{1,2}$ is
$$
SU(1,1)\cong SL(2,\mathbb{R})\cong Sp(2,\mathbb{R}),
$$
the double cover of $SO(1,2)$, generated in the algebra by the boost $K_k$ whose plane is space-like together with the rotation $J_k$ about the same axis. It is the non-compact rank-one real form of $SL(2,\mathbb{C})$, and it is the same group the companion article *The Harmonic Oscillator in Biquaternionic Form* meets as the dynamical group $Sp(2,\mathbb{R})$ of the oscillator's squeezings. Its unitary dual is **not** the principal series of $SL(2,\mathbb{C})$: being of rank one it consists of the trivial representation, the **discrete series** with parameters in $-\tfrac12\mathbb{N}$, the **continuous series** with a real parameter, and the complementary series. Its homogeneous spaces are the two hyperboloids of $\mathbb{R}^{1,2}$: the time-like one, whose vector stabiliser is the compact $U(1)$, and the space-like one, whose vector stabiliser is the non-compact one-parameter subgroup of boosts.

**The three spaces, and the three spinor models.** Two groups and three transitive spaces are what a spinfoam boundary uses:
$$
S^2=SU(2)/U(1),\qquad H^\pm=SU(1,1)/U(1),\qquad H^{sl}\ (\text{stabiliser }SO(1,1)),
$$
the sphere in $\mathbb{R}^3$ with $\eta^{(3)}=\mathrm{diag}(-1,-1,-1)$, and the two hyperboloids of $\mathbb{R}^{1,2}$ with $\eta^{(1,2)}=\mathrm{diag}(1,-1,-1)$ — the **two-sheeted** time-like one, $t^2-x^2-y^2=1$, whose compact stabiliser $U(1)$ is what the discrete series attaches to, and the **one-sheeted** space-like one, $t^2-x^2-y^2=-1$, whose non-compact stabiliser is what the continuous series attaches to. Each is modelled on spinors of the defining module, and the models are the ones the external paper cited below constructs. With the indefinite pairing $[u|v]=u^{\dagger}\sigma_3v$, invariant under $SU(1,1)$ and not under all of $SL(2,\mathbb{C})$, and the triple
$$
\varsigma=(\sigma_3,\,i\sigma_2,\,-i\sigma_1)=\sigma_3(1,\sigma_1,\sigma_2),
$$
satisfying $\varsigma^i\varsigma^j=\eta^{(1,2)ij}-i\varepsilon^{ijk}\eta^{(1,2)}_{kl}\varsigma^l$ (verified here, as is the Hermiticity of $\sigma_3\varsigma^i$), the vector maps are
$$
v^i=\langle z|\sigma^i|z\rangle\ \text{for }S^2,\qquad
v^i=\tfrac12\,\langle z|\sigma_3\varsigma^i|z\rangle\ \text{for }H^\pm,\qquad
v^i=\langle z_2|\sigma_3\varsigma^i|z_1\rangle\ \text{for }H^{sl},
$$
the first from one Weyl spinor with the definite pairing, the second from one Weyl spinor with the indefinite pairing, and the third from a **pair** of Majorana spinors with a real structure commuting with $SU(1,1)$ in place of the complex conjugation of the other two. The bilinears close, under a symplectic form on the spinor space, into the Poisson algebra of $\mathfrak{so}(1,2)\cong\mathfrak{su}(1,1)$, with the paper's form $\{v^i,v^j\}=-\varepsilon^{ijk}\eta_{kl}v^l$; the closure was recomputed here on generic elements.

**Physical reading: the group a boundary triangle sees.** The distinction matters because the causal character of a triangle and of its tetrahedron selects the subgroup of the local Lorentz group in which the triangle's holonomy lies. A space-like triangle of a space-like tetrahedron gives the compact $SU(2)$ and a discrete spin label; the two time-like cases give $SU(1,1)$ and a label drawn from the discrete or the continuous series. A compact group has finite-dimensional unitary multiplets and a non-compact one does not, so it is exactly the non-compact case that carries an infinite-dimensional boundary label — which is why the time-like triangle is the difficult one in the spinfoam programme.

## Summary

The group of unit-norm biquaternions is $SL(2,\mathbb{C})$, the double cover of the restricted Lorentz group $SO^+(1,3)$; rotor conjugation $\tilde{Q}\mapsto\tilde\Lambda\tilde{Q}\tilde\Lambda^{*}$ is the covering homomorphism, with kernel $\{\pm e_0\}$. The same abstract group is known in geometry as the group of motions of hyperbolic three-space, as the Möbius group $\mathrm{PSL}(2,\mathbb{C})$, and as the Laguerre group of the plane.

Within the group, the rotations form the subgroup $SU(2)\subset\mathbb{H}_{\mathbb{B}}$, while the boosts are the Hermitian unit-norm biquaternions $\mathcal{B}\subset\mathbb{M}_+$. The boosts are closed under inverse but not under multiplication: the product of two boost rotors is Hermitian exactly when the boosts are collinear, and otherwise is a boost times a rotation. The rotation angle is the Thomas–Wigner angle,
$$
\tan\frac{\delta}{2}
=\frac{\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\sin\theta}
{\cosh\frac{\psi_1}{2}\cosh\frac{\psi_2}{2}+\sinh\frac{\psi_1}{2}\sinh\frac{\psi_2}{2}\cos\theta},
$$
about the axis $\hat{\mathbf u}_1\times\hat{\mathbf u}_2$; the boost factor has the composite rapidity $\cosh\psi_{\mathrm c}=\cosh\psi_1\cosh\psi_2+\sinh\psi_1\sinh\psi_2\cos\theta$. Every unit-norm biquaternion has a unique polar decomposition $\tilde\Lambda=\tilde B\tilde R$ into a boost and a rotation.

The real Lie algebra is $\mathrm{SL}(2,\mathbb{C})_{\mathbb{R}}$, spanned by rotations $J_k=e_k$ and boosts $K_k=ie_k$, with $[K_j,K_k]=-2\varepsilon_{jkl}J_l$; its complexification splits into two commuting $\mathrm{SU}(2)$'s, the self-dual and anti-self-dual halves. The finite-dimensional irreducibles are the $(m,n)$, $m,n\in\tfrac12\mathbb{Z}_{\geq0}$, of dimension $(2m+1)(2n+1)$; the biquaternion algebra carries $(\tfrac12,\tfrac12)$ under conjugation. Representations with $m+n\in\mathbb{Z}$ descend to $SO^+(1,3)$; those with $m+n\in\tfrac12+\mathbb{Z}$ are genuine spin representations of the double cover.

The group that carries the transformations is represented as follows. The group of units is $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$, of real dimension $8$, with the unit-norm subgroup $SL(2,\mathbb{C})$, the maximal compact subgroups $U(2)$ and $SU(2)$, and the finite-dimensional algebraic representations of $GL_2(\mathbb{C})$ parameterised by the highest weight $(\lambda_1,\lambda_2)$. The defining module $V_{1/2}=\mathbb{C}^2$ is self-dual, and its conjugate is the other chirality: the two are the Weyl spinors, their sum is the Dirac spinor and their tensor product the four-vector representation $(\tfrac12,\tfrac12)$; the adjoint representation is $(1,0)\oplus(0,1)$. Tensor products obey the Clebsch–Gordan rule, with the ballot numbers counting the total-spin sectors of the tensor powers of the spinor. Unitarity is preserved by complexification only for the compact subgroup $SU(2)$; the only finite-dimensional unitary representation of $SL(2,\mathbb{C})$ is the trivial one, and the unitary representations are the infinite-dimensional principal and complementary series, the mode content of a field on the mass shell. The subgroup fixing a space-like direction is $SU(1,1)\cong SL(2,\mathbb{R})\cong Sp(2,\mathbb{R})$, the double cover of $SO(1,2)$, whose unitary dual is the discrete and continuous series rather than the principal series of the full group; it acts on the sphere $S^2=SU(2)/U(1)$ and on the two hyperboloids $H^\pm=SU(1,1)/U(1)$ and $H^{sl}$, each modelled on one or two spinors of the defining module with the definite or the indefinite pairing.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$, $e_1e_2=e_3$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (material sector), home of four-vectors |
| $\mathbb{M}_+$ | Hermitian subspace (informational sector), home of boost rotors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, home of rotation rotors |
| $N(\tilde Q) = \langle\tilde Q,\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}$ | Biquaternion norm |
| $\tilde\Lambda\in SL(2,\mathbb{C})$ | Unit-norm biquaternion (Lorentz rotor) |
| $\tilde{Q}\mapsto\tilde\Lambda\tilde{Q}\tilde\Lambda^{*}$ | Rotor conjugation (four-vector action) |
| $\mathrm{Ad}:SL(2,\mathbb{C})\to SO^+(1,3)$ | Two-to-one covering homomorphism, kernel $\{\pm e_0\}$ |
| $\tilde\Lambda=\cosh\frac\psi2+i\sinh\frac\psi2\hat{\mathbf u}$ | Boost rotor (Hermitian, in $\mathbb{M}_+$) |
| $\tilde R=\cos\frac\theta2+\sin\frac\theta2\hat{\mathbf n}$ | Rotation rotor (unit real quaternion, in $SU(2)$) |
| $\psi$ | Rapidity, $\tanh\psi=u/c$ |
| $\delta$ | Thomas–Wigner rotation angle |
| $\tilde\Lambda=\tilde B\tilde R$ | Cartan (polar) decomposition: boost times rotation |
| $J_k=e_k$, $K_k=ie_k$ | Rotation and boost generators |
| $[J_j,J_k]=2\varepsilon_{jkl}J_l$, $[J_j,K_k]=2\varepsilon_{jkl}K_l$, $[K_j,K_k]=-2\varepsilon_{jkl}J_l$ | Lie brackets |
| $N_k^\pm=\frac12(e_k\pm\mathsf{i}(ie_k))$ | Generators of the two $\mathrm{SU}(2)$ halves |
| $(m,n)=V_m\boxtimes V_n$ | Irreducible representation, $\dim=(2m+1)(2n+1)$ |
| $(\tfrac12,0)$, $(0,\tfrac12)$ | Left- and right-handed Weyl spinors |
| $(\tfrac12,\tfrac12)$ | Four-vector (biquaternion algebra as module) |
| $m+n\in\mathbb{Z}$ vs $\tfrac12+\mathbb{Z}$ | Descends to $SO^+(1,3)$ vs genuine spin representation |
| $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$ | Group of units; real dimension $8$ |
| $U(2)$ | Unitary biquaternions; maximal compact subgroup of $\mathbb{B}^{\times}$ |
| $(\lambda_1,\lambda_2)$ | Highest weight of an algebraic representation of $GL_2(\mathbb{C})$ |
| $V_j$ | Irreducible representation of spin $j$, highest weight $2j$, dimension $2j+1$ |
| $V_{1/2}^{\otimes N}$ | Ballot-number decomposition of the tensor powers of the spinor |
| $\operatorname{Ind}_P^G(\chi_{m,\nu})$ | Principal series of $SL(2,\mathbb{C})$; $P=MAN$ the Borel subgroup |
| $SU(1,1)\cong SL(2,\mathbb{R})\cong Sp(2,\mathbb{R})$ | Subgroup fixing a space-like direction; double cover of $SO(1,2)$ |
| $S^2$, $H^\pm$, $H^{sl}$ | Sphere, two-sheeted time-like hyperboloid, one-sheeted hyperboloid |
| $[u|v]=u^{\dagger}\sigma_3v$ | Indefinite $SU(1,1)$-invariant pairing |
| $\varsigma=(\sigma_3,i\sigma_2,-i\sigma_1)$ | Triple of $SU(1,1)$ generators; $\varsigma^i\varsigma^j=\eta^{ij}-i\varepsilon^{ijk}\eta_{kl}\varsigma^l$ |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |
| $\langle\tilde{P},\tilde{Q}\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{P}\tilde{Q})$ |

## Further Reading

- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the Lorentz group, its Lie algebra, and the construction of the representations from two Weyl spinors.
- Wu-Ki Tung, *Group Theory in Physics* (World Scientific, 1985), for the finite-dimensional representation theory of the Lorentz group and the $(m,n)$ labelling.
- Élie Cartan and G. Fano, "La théorie des groupes continus et la géométrie," *Encyclopédie des Sciences Mathématiques Pures et Appliquées* **3**(1) (1915; completed posthumously 1955) 39–43, for the identification of the Lorentz group with the Laguerre group; and Henri Poincaré's report on Cartan's work, *Acta Mathematica* **38** (1921) [1912], for the same identification.
- I. M. Gel'fand, R. A. Minlos, and Z. Ya. Shapiro, *Representations of the Rotation and Lorentz Groups and Their Applications* (Pergamon, 1963), for the classical treatment of the Lorentz group representations and the two $\mathrm{SU}(2)$ decomposition.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for $\mathrm{SL}(2,\mathbb{C})$ representations, the Clebsch–Gordan rule, and the highest-weight classification.
- Anthony W. Knapp, *Representation Theory of Semisimple Groups: An Overview Based on Examples* (Princeton University Press, 1986), for the principal and complementary series and the unitary dual of $SL(2,\mathbb{C})$.
- V. Bargmann, "Irreducible unitary representations of the Lorentz group," *Annals of Mathematics* **48** (1947) 568–640, for the classification of the unitary irreducible representations of $SL(2,\mathbb{C})$ and of its rank-one subgroups, including the discrete and continuous series.
- J. D. Simão, "Biquaternions, Majorana spinors and time-like spin-foams," arXiv:2401.10324 [gr-qc] (2024), for the causal-character grading of a spinfoam boundary into $SU(2)$ and $SU(1,1)$ with the discrete and continuous series, the Weyl- and Majorana-spinor models of $S^2$, $H^\pm$ and $H^{sl}$, the $\varsigma$ triple, and the $\mathfrak{su}(1,1)$ closure of the bilinears. External; cited for the boundary only.
- Companion article *The Harmonic Oscillator in Biquaternionic Form*, for the dynamical group $Sp(2,\mathbb{R})\cong SU(1,1)$ of the oscillator's squeezings and the $\mathfrak{su}(1,1)$ Lie algebra in a non-relativistic setting.
- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for the Lie-algebra structure, the Killing form, and the complexification.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Clifford-algebra origin of the spin group and the double cover of the Lorentz group.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus and the self-dual/anti-self-dual decomposition.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of boosts and rotations and the Thomas–Wigner rotation.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of the Lorentz group in the even subalgebra.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the Thomas precession in its physical setting.
