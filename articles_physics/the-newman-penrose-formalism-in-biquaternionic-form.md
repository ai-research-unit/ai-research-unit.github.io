# __The Newman–Penrose Formalism in Biquaternionic Form__

## Introduction

The Newman–Penrose formalism rewrites the local geometry of four-dimensional spacetime in a basis adapted to the light cone. In place of an orthonormal frame it uses a **null tetrad** $(l, n, m, \bar m)$: two real null vectors $l$ and $n$, and a complex-conjugate pair $m, \bar m$ that are also null. The ten independent components of the Weyl tensor become five complex scalars $\Psi_0, \dots, \Psi_4$; the connection becomes twelve complex **spin coefficients**; and the Petrov classification of the curvature is read off from which of the five scalars vanish. The formalism is the standard language of the algebraically special solutions of general relativity.

This article places that formalism in the biquaternion framework of the read-list articles, and the placement is not an analogy. The primitive object of the Newman–Penrose construction is a null vector, and the primitive algebraic object of the framework is the **zero divisor**: in the material sector $\mathbb{M}_-$ the light cone *is* the zero-divisor cone, a nonzero null vector is a zero divisor of $\mathbb{B}$, and under the matrix realization $\Phi : \mathbb{B} \to M_2(\mathbb{C})$ it is a rank-one matrix (*The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*; *Biquaternion Null Quadric and Projective Geometry*). Every leg of a Newman–Penrose tetrad is therefore a zero divisor of the algebra, and the tetrad itself is the image of a normalized spinor dyad under the framework's spinor bilinear. That identification is the centre of this article, and it is verified below rather than asserted.

Three claims organise the discussion.

**First, the null tetrad is algebraic and native.** The four legs are elements of $\mathbb{B}$ — $l$ and $n$ in the real material sector $\mathbb{M}_-$, with $m$ and $\bar m$ complex — and each is a zero divisor. Their inner products $l\cdot n = -1$ and $m\cdot\bar m = +1$, and their vanishing self-products, follow from the normalization of the spinor dyad and from the framework's norm form; the metric is recovered from the tetrad by the completeness relation. All of this is recomputed, and the tetrad construction is checked on a dyad chosen for the check rather than on the basis dyad that suggested it.

**Second, the spin coefficients and the Weyl scalars are hosted but not generated.** The twelve spin coefficients are the components in the null basis of a connection valued in $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$ — the six-dimensional bivector subspace of $\mathbb{B}$ that the parent article identifies — and the five Weyl scalars are the components of the self-dual Weyl spinor $\Psi_{ABCD} \in \mathrm{Sym}^4 S$, where $S$ is the framework's spinor module. The algebra supplies the tetrad, the dyad, and the home of both objects; it supplies neither the connection nor the Weyl tensor.

**Third, the weights and the classification are representation-theoretic.** Under the boost–spin subgroup of the tetrad rotations the scalars scale with definite **boost weights**, $\Psi_k \mapsto A^{2-k} e^{\,i(2-k)\theta}\,\Psi_k$; the Petrov types are the multiplicity patterns of the principal null directions, equivalently the multiplicity patterns of the roots of the binary quartic $\Psi_{ABCD}k^Ak^Bk^Ck^D$. Both are recomputed on the algebra's own objects.

The article closes by separating what the framework contains from what remains an agenda. The separation is sharp: the null structure of the tetrad is native, and the curvature that the tetrad is used to describe is not.

The conventions are inherited from the read-list articles and none is redefined. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0 = 1, e_1, e_2, e_3$ satisfying $e_k^2 = -e_0$ and $e_1e_2 = e_3$, and scalar imaginary $i$ commuting with the quaternion units. The anti-Hermitian and Hermitian subspaces are $\mathbb{M}_-$ and $\mathbb{M}_+$, the real-quaternion subspace is $\mathbb{H}_{\mathbb{B}}$, and the norm form is $N(\tilde Q) = \tilde Q\bar{\tilde Q}$. The material sector is $\mathbb{M}_- = \{iq_0e_0 + q_1e_1 + q_2e_2 + q_3e_3 : q_\mu \in \mathbb{R}\}$, with four-vector coordinates $(q_0,q_1,q_2,q_3)$, and the bilinear (polar) form on it is

$$
\langle \tilde Q, \tilde P\rangle \;=\; \mathrm{Sc}\big(\tilde Q\bar{\tilde P}\big) \;=\; -q_0p_0 + q_1p_1 + q_2p_2 + q_3p_3 ,
$$

of signature $(3,1)$ in the read list's counting — three positive directions and one negative. The matrix realization is the $\mathbb{C}$-algebra isomorphism

$$
\Phi : \mathbb{B} \longrightarrow M_2(\mathbb{C}), \qquad
\Phi(e_0) = I_2, \quad \Phi(e_k) = -i\sigma_k, \quad \Phi(i) = iI_2,
$$

so that $N(\tilde Q) = \det\Phi(\tilde Q)$, Hermitian conjugation corresponds to the conjugate transpose, and $\mathbb{M}_-$ corresponds to the anti-Hermitian matrices. The spinor module is $S = \mathbb{C}^2$, the unique simple module of $\mathbb{B}$, on which the algebra acts by left multiplication; the Weyl spinor modules are $S = (\tfrac12,0)$ and its conjugate $\bar S = (0,\tfrac12)$. The rotor group is $\{\tilde\Lambda : \tilde\Lambda\bar{\tilde\Lambda} = e_0\} \cong SL(2,\mathbb{C})$, acting on $\mathbb{M}_-$ by rotor conjugation $\tilde X \mapsto \tilde\Lambda\tilde X\tilde\Lambda^\dagger$, with covering homomorphism $\Pi$ onto $SO^+(1,3)$ and kernel $\{\pm e_0\}$. The trace formula of the informational sector is $\mathrm{Tr}(\tilde P\tilde H) = 2\,\mathrm{Sc}(\tilde P\tilde H)$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum speed.

## Conventions: Signature and the Tetrad Normalization

A null tetrad is defined only up to a six-parameter local Lorentz transformation, and the inner products of its legs are fixed by a convention that must be stated before anything is computed from it. Two conventions are in common use and they differ by signs. This article fixes

$$
l\cdot l = n\cdot n = m\cdot m = \bar m\cdot\bar m = 0, \qquad
l\cdot n = -1, \qquad m\cdot\bar m = +1, \qquad
l\cdot m = l\cdot\bar m = n\cdot m = n\cdot\bar m = 0,
\tag{1}
$$

where $\cdot$ is the bilinear form $\langle\cdot,\cdot\rangle$ of the material sector, extended $\mathbb{C}$-bilinearly to $\mathbb{C}\otimes_\mathbb{R}\mathbb{M}_-$. This is the normalization appropriate to the signature $(3,1)$ with $g = \mathrm{diag}(-1,+1,+1,+1)$ that the read list uses; with the opposite metrical convention one takes $l\cdot n = +1$ and $m\cdot\bar m = -1$. Fixed once here, the convention (1) is held throughout.

Two features of (1) are worth naming because they are the source of most sign errors in this subject. First, the tetrad is **not** an orthonormal frame: its legs are null, so the metric in tetrad components is off-diagonal, and the completeness relation that inverts (1) carries the off-diagonal signs. Second, $l$ and $n$ are real four-vectors while $m$ and $\bar m$ are complex conjugates; the tetrad is a basis of the complexified material sector, of complex dimension four, not of the real $\mathbb{M}_-$.

The tetrad legs are labelled in the order $(e_1, e_2, e_3, e_4) = (l, n, m, \bar m)$ when a tetrad index is needed. Greek letters $\mu,\nu,\dots$ run over the coordinate directions of the material sector, and tetrad indices $a,b,\dots$ over the four legs.

## The Null Tetrad as a Frame of Zero Divisors

The framework's criterion for a zero divisor is a statement about the norm form. A nonzero biquaternion $\tilde Q$ is a zero divisor if and only if $N(\tilde Q)=0$, and under the isomorphism $\Phi$ the nonzero zero divisors are exactly the rank-one matrices (*Biquaternion Zero Divisors*). Restricted to the material sector, $N(\tilde Q) = -q_0^2+q_1^2+q_2^2+q_3^2$, so a nonzero element of $\mathbb{M}_-$ is a zero divisor exactly when its four-vector is null. The Newman–Penrose construction asks for four null vectors; the framework has a name for them already.

Take the tetrad

$$
l = \frac{i}{\sqrt2}e_0 - \frac{1}{\sqrt2}e_3, \qquad
n = \frac{i}{\sqrt2}e_0 + \frac{1}{\sqrt2}e_3, \qquad
m = -\frac{1}{\sqrt2}e_1 - \frac{i}{\sqrt2}e_2, \qquad
\bar m = -\frac{1}{\sqrt2}e_1 + \frac{i}{\sqrt2}e_2 .
\tag{2}
$$

In four-vector coordinates $(q_0,q_1,q_2,q_3)$ the four legs read

$$
l = \big(\tfrac{1}{\sqrt2},0,0,-\tfrac{1}{\sqrt2}\big), \quad
n = \big(\tfrac{1}{\sqrt2},0,0,\tfrac{1}{\sqrt2}\big), \quad
m = \big(0,-\tfrac{1}{\sqrt2},-\tfrac{i}{\sqrt2},0\big), \quad
\bar m = \big(0,-\tfrac{1}{\sqrt2},\tfrac{i}{\sqrt2},0\big),
$$

so $l$ and $n$ are real four-vectors — elements of the real material sector $\mathbb{M}_-$ — while $m$ and $\bar m$ are exchanged by complex conjugation. The norm form vanishes on each leg,

$$
N(l)=N(n)=N(m)=N(\bar m)=0,
$$

and no leg is zero, so **every leg of the null tetrad is a zero divisor of $\mathbb{B}$**. Under $\Phi$ the legs are the matrix units:

$$
\Phi(l)=\sqrt2\,i\,E_{11}, \quad \Phi(n)=\sqrt2\,i\,E_{22}, \quad \Phi(m)=\sqrt2\,i\,E_{12}, \quad \Phi(\bar m)=\sqrt2\,i\,E_{21},
\tag{3}
$$

where $E_{ij}$ has $1$ in position $(i,j)$ and $0$ elsewhere. Each image has rank one, so the zero-divisor property is visible by rank as well as by norm.

Equation (3) is the precise sense in which the null tetrad is native to the algebra. Up to the common factor $\sqrt2\,i$, the Newman–Penrose tetrad **is** the matrix-unit basis of $\mathbb{B}\cong M_2(\mathbb{C})$. The spinor-module article already names that basis:

$$
p = \tfrac12(e_0+ie_3), \quad q = \tfrac12(e_0-ie_3), \quad x = \tfrac12(ie_1-e_2), \quad y = \tfrac12(ie_1+e_2),
$$

with $\Phi(p)=E_{11}$, $\Phi(q)=E_{22}$, $\Phi(x)=E_{12}$, $\Phi(y)=E_{21}$, and with $p,q$ the primitive orthogonal idempotents: $p^2=p$, $q^2=q$, $pq=qp=0$. Therefore

$$
l = \sqrt2\,i\,p, \qquad n = \sqrt2\,i\,q, \qquad m = \sqrt2\,i\,x, \qquad \bar m = \sqrt2\,i\,y .
\tag{4}
$$

The two real null directions are the two primitive idempotents, and the complex pair is the off-diagonal pair. The tetrad is the Peirce decomposition of the algebra read as a null frame: the "physical" content of the tetrad — two real null directions — is exactly the idempotent content of $\mathbb{B}$.

The inner products (1) now follow from (4) and the trace formula $\langle \tilde Q,\tilde P\rangle = \mathrm{Sc}(\tilde Q\bar{\tilde P})$. Because $\bar q = p$ and $p^2=p$,

$$
\langle l,n\rangle = (\sqrt2\,i)^2\,\mathrm{Sc}(p\,\bar q) = -2\,\mathrm{Sc}(p^2) = -1 ,
$$

and because $\bar y = -y$ and $xy = p$ in the matrix-unit relations,

$$
\langle m,\bar m\rangle = (\sqrt2\,i)^2\,\mathrm{Sc}(x\,\bar y) = 2\,\mathrm{Sc}(xy) = 2\,\mathrm{Sc}(p) = +1 .
$$

The mixed products vanish because the off-diagonal units have vanishing scalar part, $\mathrm{Sc}(x)=\mathrm{Sc}(y)=0$, and the relevant products are off-diagonal matrix units. All ten inner products were recomputed from (4); the result is the off-diagonal tetrad metric

$$
\eta_{ab} = \begin{pmatrix} 0 & -1 & 0 & 0\\ -1 & 0 & 0 & 0\\ 0 & 0 & 0 & 1\\ 0 & 0 & 1 & 0\end{pmatrix}, \qquad (e_1,e_2,e_3,e_4)=(l,n,m,\bar m).
\tag{5}
$$

The metric is off-diagonal because the basis is null; there is no orthonormal frame hidden in (2). The four diagonal zeros are the null conditions, and the two $\pm1$ entries are the normalizations fixed in (1) and held.

## The Metric Recovered from the Tetrad

The tetrad is a complex basis of $\mathbb{B}$ as a four-dimensional complex vector space, and the coordinate metric is recovered from it by the completeness relation. Since the matrix $\eta$ in (5) squares to the identity, the expansion of an arbitrary element $\tilde X\in\mathbb{B}$ in the tetrad is

$$
\tilde X = -\langle \tilde X,l\rangle\,n - \langle \tilde X,n\rangle\,l + \langle \tilde X,m\rangle\,\bar m + \langle \tilde X,\bar m\rangle\,m ,
\tag{6}
$$

and, writing $l_\mu,n_\mu,m_\mu,\bar m_\mu$ for the components of the legs in the orthonormal coordinate basis of the material sector, the metric is

$$
g_{\mu\nu} = -l_\mu n_\nu - n_\mu l_\nu + m_\mu\bar m_\nu + \bar m_\mu m_\nu .
\tag{7}
$$

Substituting (2), the right-hand side of (7) evaluates to $\mathrm{diag}(-1,+1,+1,+1)$: the four zero divisors reproduce the material-sector metric, with the correct signature, and no other input is used. Both (6) and (7) were recomputed symbolically; (6) was checked on a general element $\tilde X$ with all four coefficients arbitrary, and (7) on the explicit legs.

Equation (7) is the null-tetrad counterpart of the frame relation $g_{\mu\nu} = \langle\tilde E_\mu,\tilde E_\nu\rangle$ of the parent article. There the frame was orthonormal and its legs lay in $\mathbb{M}_-$; here the frame is null and complex, and its legs are zero divisors. At each point the two are related by the local Lorentz transformation that carries one basis to the other, so the parent's remark — that the algebra supplies the local Lorentz group and the home of the frame, but not the frame itself — applies here verbatim.

## The Spinor Dyad Behind the Tetrad

Equation (3) also exhibits the tetrad's spinorial origin. Writing the two column spinors

$$
o = \begin{pmatrix}1\\0\end{pmatrix}, \qquad \iota = \begin{pmatrix}0\\1\end{pmatrix} \in S,
$$

the matrix units factorize as $E_{11} = o\,o^\dagger$, $E_{22} = \iota\,\iota^\dagger$, $E_{12} = o\,\iota^\dagger$, $E_{21} = \iota\,o^\dagger$. Hence

$$
l = \sqrt2\,i\,o\,o^\dagger, \quad n = \sqrt2\,i\,\iota\,\iota^\dagger, \quad m = \sqrt2\,i\,o\,\iota^\dagger, \quad \bar m = \sqrt2\,i\,\iota\,o^\dagger .
\tag{8}
$$

This is the Newman–Penrose **spinor dyad** $\{o,\iota\}$ in the framework's notation, and (8) is the sense in which the tetrad is the image of the dyad under the bilinear map $S\times\bar S\to\mathbb{B}$, $(u,v)\mapsto i\,uv^\dagger$, the framework's form of the algebra-level outer product $u\,v^\dagger$, whose Hermitian part the spinor-module article identifies with the vector representation. The dyad is normalized by the invariant symplectic pairing of the spinor module,

$$
\varepsilon(o,\iota) = o_1\iota_2 - o_2\iota_1 = 1, \qquad \varepsilon(g o, g \iota) = \varepsilon(o,\iota) \ \text{ for } g\in SL(2,\mathbb{C}),
$$

the form $g^{T}\epsilon\,g = \epsilon$ of the read list; it is exactly this normalization, and not the choice of basis, that produces $l\cdot n = -1$ and $m\cdot\bar m = +1$.

The construction is not tied to the basis dyad. For any dyad with $\varepsilon(o,\iota)=1$ the four legs defined by (8) are null, satisfy $l\cdot n=-1$ and $m\cdot\bar m=+1$, and have all mixed products zero; this was checked symbolically for a general complex dyad, and independently on the explicit real dyad $o=(2,1)$, $\iota=(3,2)$, whose symplectic product is $2\cdot2-1\cdot3=1$. That second dyad was chosen for the check rather than being the one that suggested the construction, and the inner products came out as in (1) on it. For the physical tetrad (2), in which the dyad is real, $\bar m$ is the complex conjugate of $m$; a complex dyad (a spin-boost of the frame) complexifies the legs while leaving the inner products (1) unchanged.


## Spin Coefficients

The tetrad is a frame, and a connection is expressed in a frame through its coefficients. Suppose a linear connection $\nabla$ on the material sector is given, metric-compatible with $\langle\cdot,\cdot\rangle$; the parent article records that the algebra carries such a connection but does not select one. For tetrad legs $e_a,e_b,e_c$ define

$$
\Gamma_{abc} := (\nabla_a e_b)\cdot e_c, \qquad \nabla_a := \nabla_{e_a}.
$$

Metric compatibility, $\nabla_a(e_b\cdot e_c)=0$, gives $\Gamma_{abc}+\Gamma_{acb}=0$, so the coefficients are antisymmetric in the last two tetrad indices. For each $a$ this is a $4\times4$ antisymmetric matrix with six independent entries, the connection being real, so $\Gamma_{abc}$ has $4\times6=24$ real independent components — that is, **twelve complex** ones. These twelve complex numbers, written in the standard names, are the **spin coefficients**:

$$
\kappa,\ \sigma,\ \rho,\ \tau; \qquad \pi,\ \lambda,\ \mu,\ \nu; \qquad \varepsilon,\ \gamma,\ \beta,\ \alpha .
$$

The first four are the contractions of $\nabla l$ with the tetrad legs,

$$
\kappa = m^a D l_a, \qquad \sigma = m^a \delta l_a, \qquad \rho = m^a \bar\delta l_a, \qquad \tau = m^a \Delta l_a,
$$

where $D=l^a\nabla_a$, $\Delta=n^a\nabla_a$, $\delta=m^a\nabla_a$ and $\bar\delta=\bar m^a\nabla_a$ are the directional derivatives along the tetrad. The second four are the analogous contractions of $\nabla n$, and the last four complete the components of $\nabla l$ and $\nabla n$ along $l$ and $n$ themselves. The overall signs are convention-dependent — the literature does not agree on them, and the definitions are stated here only to fix the pattern — but the count and the identification of the twelve as components of one connection are not.

In the framework the connection is valued in the bivector subspace. The parent article identifies the Lorentz Lie algebra $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$ with the six-dimensional subspace $\{\tilde G : \mathrm{Sc}(\tilde G)=0\}$ — equivalently, under $\Phi$, the traceless $2\times2$ matrices — spanned by $e_1,e_2,e_3$ and $ie_1,ie_2,ie_3$, which is the complex-pure-vector subspace of $\mathbb{B}$. A connection 1-form takes values in that subspace and has one component per tetrad direction, giving

$$
\underbrace{6}_{\text{real dim } \mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}} \ \times\ \underbrace{4}_{\text{tetrad directions}} \ =\ 24 \ \text{real}\ =\ 12 \ \text{complex},
$$

the same count as the antisymmetry of $\Gamma_{abc}$ gave. The biquaternionic statement of the spin coefficients is therefore: **they are the components, in the null tetrad, of an $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$-valued 1-form** — a $\mathbb{B}$-valued connection, since the bivectors sit inside $\mathbb{B}$. In flat spacetime with the constant tetrad (2), every $\nabla e_a$ vanishes and all twelve coefficients are zero; in general they measure the failure of the tetrad to be covariantly constant.

The framework's contribution here is a home, not a construction. It supplies the six-dimensional traceless subspace in which the connection values live, and it supplies the tetrad in which they are resolved; it does not supply the connection itself, exactly as the parent article found for the frame.

## The Weyl Scalars

The Weyl tensor $C_{abcd}$ is the trace-free part of the Riemann tensor, the part left after the Ricci tensor and the curvature scalar are removed. It inherits the algebraic symmetries of the Riemann tensor, $C_{abcd}=-C_{bacd}=-C_{abdc}=C_{cdab}$ with $C_{a[bcd]}=0$, and it is trace-free, $g^{ac}C_{abcd}=0$; in four dimensions this leaves ten independent real components. Contracting it with the null tetrad produces the five complex **Weyl scalars**:

$$
\begin{aligned}
\Psi_0 &= C_{abcd}\,l^a m^b l^c m^d, &\qquad
\Psi_1 &= C_{abcd}\,l^a n^b l^c m^d, &\qquad
\Psi_2 &= C_{abcd}\,l^a m^b \bar m^c n^d, \\
\Psi_3 &= C_{abcd}\,l^a n^b \bar m^c n^d, &\qquad
\Psi_4 &= C_{abcd}\,\bar m^a n^b \bar m^c n^d,
\end{aligned}
\tag{9}
$$

with an overall sign that is convention-dependent. The index structure of (9) fixes the boost weights computed in the next section, and the pattern of which legs appear in which scalar is the part of the convention that matters.

The counting works, and the decomposition $10 = 5$ complex is a real isomorphism rather than a coincidence. To verify it, parametrise a general tensor with the Weyl symmetries $C_{abcd}=-C_{bacd}=-C_{abdc}=C_{cdab}$, $C_{a[bcd]}=0$ and $g^{ac}C_{abcd}=0$. With the antisymmetries and pair symmetry there are $21$ independent pair-components; the first Bianchi identity imposes one independent condition and trace-freeness imposes ten, leaving a $21-11=10$ dimensional space. The map that sends such a tensor to the five complex contractions (9) was computed on that ten-dimensional space and found to have rank ten over $\mathbb{R}$ — equivalently rank five over $\mathbb{C}$ — so the five complex scalars are exactly the ten real components reorganised, and no information is lost. Both the dimension and the rank were recomputed.

The scalars have a spinorial form that names them in the framework's own objects. The self-dual part of the Weyl tensor is the totally symmetric fourth-rank spinor
$$
\Psi_{ABCD} \in \mathrm{Sym}^4 S,
$$
whose five independent components are the five scalars,
$$
\Psi_0 = \Psi_{0000}, \quad \Psi_1 = \Psi_{0001}, \quad \Psi_2 = \Psi_{0011}, \quad \Psi_3 = \Psi_{0111}, \quad \Psi_4 = \Psi_{1111},
\tag{10}
$$
where the index $0$ refers to the dyad element $o$ and $1$ to $\iota$. Since $S$ is two-dimensional, $\mathrm{Sym}^4 S$ has dimension $\binom{2+4-1}{4}=5$, matching (9); the anti-self-dual part is the complex conjugate spinor $\bar\Psi_{A'B'C'D'} \in \mathrm{Sym}^4\bar S$, and the reality of the Weyl tensor identifies the two, so the ten real components are the real and imaginary parts of the five complex scalars. This is the biquaternionic form of the Weyl scalars: **they are the five components of an element of $\mathrm{Sym}^4 S$, the fourth symmetric power of the framework's spinor module.**

A qualification is required, and it is the main gap of this article. The framework hosts $\mathrm{Sym}^4 S$, because it hosts the spinor module $S$; but the Weyl tensor is an external rank-four object, and nothing in $\mathbb{B}$ determines it. The five scalars are $\mathrm{Sym}^4 S$-valued, and the algebra says what that means, but which element of $\mathrm{Sym}^4 S$ a given spacetime produces is not a question the algebra answers. The next two sections use only the representation theory of $\mathrm{Sym}^4 S$, and are therefore independent of this gap; the classification of a specific spacetime is not.


## Boost Weights and the Rotations of the Tetrad

The tetrad is defined up to the six-parameter local Lorentz group, and the five scalars transform by the index structure of (9). It is useful to split that group into the two-parameter boost–spin subgroup and the two null rotations.

A boost–spin transformation rescales the legs as

$$
l \mapsto A\,l, \qquad n \mapsto A^{-1}n, \qquad m \mapsto e^{i\theta}m, \qquad \bar m \mapsto e^{-i\theta}\bar m, \qquad A>0,\ \theta\in\mathbb{R},
\tag{11}
$$

which preserves every entry of (1). In spinor terms it is $o\mapsto A^{1/2}e^{i\theta/2}o$, $\iota\mapsto A^{-1/2}e^{-i\theta/2}\iota$. Substituting (11) into (9), each scalar picks up a monomial:

$$
\Psi_k \;\longmapsto\; A^{\,2-k}\,e^{\,i(2-k)\theta}\,\Psi_k, \qquad k=0,\dots,4 .
\tag{12}
$$

The exponent $2-k$ is the **boost weight** of $\Psi_k$; it is also its spin weight, so the two coincide for the Weyl scalars. The five weights are $2,1,0,-1,-2$ as $k$ runs from $0$ to $4$.

The weight (12) was recomputed for all five scalars, not only for the extremes. Taking a general Weyl tensor and the explicit tetrad (2), the ratio $\Psi_k'/\Psi_k$ came out equal to $A^{2-k}e^{i(2-k)\theta}$ for every $k$ from $0$ to $4$; the check is multilinear in the Weyl tensor and therefore does not depend on the particular tensor chosen. The same weights are visible directly in the spinor form (10): $\Psi_k$ carries $4-k$ dyad indices of type $o$ and $k$ of type $\iota$, while $o$ and $\iota$ carry boost weights $+\tfrac12$ and $-\tfrac12$, so the weight of $\Psi_k$ is $(4-k)\tfrac12 + k(-\tfrac12) = 2-k$.

The weights make the word "definite" precise: the group acts on the five scalars diagonally in the boost direction, and the weight is the exponent of that diagonal action. They also explain why a statement that a scalar vanishes is frame-independent while a statement about the relative size of two scalars is graded: the vanishing of $\Psi_k$ is preserved by every boost–spin because $A^{2-k}\neq0$, and the five scalars sit in five distinct weight spaces.

The null rotations complete the group. A null rotation about $l$ fixes $l$ and shifts the other three legs,

$$
l \mapsto l, \qquad m \mapsto m + \bar z\,l, \qquad \bar m \mapsto \bar m + z\,l, \qquad n \mapsto n + z\,m + \bar z\,\bar m + |z|^2 l, \qquad z\in\mathbb{C},
\tag{13}
$$

which again preserves all the inner products (1). Under (13) the scalar $\Psi_0$ is invariant. This is forced by the index structure: $\Psi_0$ contains $l$ twice, and the terms generated by $m\mapsto m+\bar z l$ involve the contractions $C_{abcd}l^al^bl^cm^d$ and $C_{abcd}l^am^bl^cl^d$, each of which has a repeated leg in a pair of antisymmetric slots and therefore vanishes for any tensor with the Riemann antisymmetries. A null rotation about $n$ leaves $\Psi_4$ invariant by the same argument with $l\leftrightarrow n$. Both invariances were recomputed on several independent curvature tensors.

The invariance of the two extreme scalars is what makes the principal-null-direction conditions meaningful. The condition $\Psi_0=0$ is unchanged by a null rotation about $l$, so it is a property of the null direction $l$ rather than of the particular tetrad containing it: it says that $l$ is a principal null direction. The same holds for $\Psi_4=0$ and $n$. The remaining scalars shift under (13) by polynomial combinations of their partners, with the shifts graded by the boost weights; this is the mechanism by which a null rotation can align $l$ with a repeated principal null direction, as used in the classification below.

## Petrov Types and the Vanishing Pattern

The Petrov type of a Weyl tensor is the multiplicity pattern of its four principal null directions, and in the spinor form (10) this is a statement about a binary quartic. With $k^A = o^A + x\,\iota^A$,

$$
q(x) \;=\; \Psi_{ABCD}\,k^Ak^Bk^Ck^D \;=\; \Psi_0 + 4x\,\Psi_1 + 6x^2\,\Psi_2 + 4x^3\,\Psi_3 + x^4\,\Psi_4 .
\tag{14}
$$

The root $x=0$ represents the null direction $l$ (more precisely the spinor $o$), and the vanishing of $q$ and its derivatives at $x=0$ is the statement that $l$ is a repeated principal null direction. Explicitly,

$$
\begin{array}{ll}
\Psi_0 = 0 & l \text{ is a principal null direction (PND)},\\
\Psi_0 = \Psi_1 = 0 & l \text{ is a double PND},\\
\Psi_0 = \Psi_1 = \Psi_2 = 0 & l \text{ is a triple PND},\\
\Psi_0 = \Psi_1 = \Psi_2 = \Psi_3 = 0 & l \text{ is a quadruple PND}.
\end{array}
\tag{15}
$$

The four roots of the quartic (14) are the four principal null directions, counted with multiplicity, and the Petrov type is their multiplicity pattern. A quartic has five nontrivial multiplicity patterns — the partitions of $4$ — together with the identically zero case, and these are the six Petrov types:

| Type | Multiplicities | Principal null directions | Canonical form with $l$ repeated |
|------|----------------|----------------------------|----------------------------------|
| I | $1+1+1+1$ | four distinct | $\Psi_0=0$; with $n$ also a PND, $\Psi_0=\Psi_4=0$ |
| II | $2+1+1$ | one double, two simple | $\Psi_0=\Psi_1=0$ |
| D | $2+2$ | two double | $\Psi_0=\Psi_1=\Psi_3=\Psi_4=0$, $\Psi_2\neq0$ |
| III | $3+1$ | one triple, one simple | $\Psi_0=\Psi_1=\Psi_2=0$ |
| N | $4$ | one quadruple | $\Psi_0=\Psi_1=\Psi_2=\Psi_3=0$, $\Psi_4\neq0$ |
| O | — | none (conformally flat) | all $\Psi_k=0$ |

Two conventions are at work in such a table, and they must be separated. The **type** — the multiplicity pattern — is invariant. The **canonical vanishing list** is not: it depends on which principal null direction is aligned with $l$, and the table above aligns $l$ with the repeated direction. If instead $n$ is the repeated direction, the roles of the scalars are exchanged by $\Psi_k\leftrightarrow\Psi_{4-k}$, consistent with the weights $2-k$ and $-2+k$. The pattern in the table is stable under the residual boost–spin and null-rotation freedoms that preserve the alignment, which is why "the type" is well defined even though the individual scalars are not.

The framework does not derive the classification, and it does not need to: the classification is the multiplicity theory of the quartic (14), which lives in $\mathrm{Sym}^4 S$, and $\mathrm{Sym}^4 S$ is hosted by the algebra. What the algebra cannot do is produce the quartic for a given spacetime. That is the gap recorded above, and it is not closed here.

## What the Algebra Supplies and What It Does Not

The construction separates cleanly into what is native to $\mathbb{B}$ and what is transcribed.

**Native to the algebra.** The four null legs, as zero divisors and as rank-one matrices; the identity (4) that the tetrad is $\sqrt2\,i$ times the matrix-unit basis, with the two real null directions equal to the two primitive idempotents $p,q$; the spinor dyad and its symplectic normalization; the inner products (1) and the metric (7); the bivector subspace $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$ in which a connection takes its values; the spinor module $S$ and its symmetric power $\mathrm{Sym}^4 S$ in which the Weyl scalars take their values; and the boost weights (12), which follow from the weights of $\mathrm{Sym}^4 S$. The mapping of the null tetrad onto the zero divisors is exact, with no residual mismatch: every leg is a zero divisor, every leg is rank one, and the four together span $\mathbb{B}$. In particular, the null structure of the Newman–Penrose tetrad maps onto the framework's zero-divisor structure cleanly, and no gap is reported here.

**Not native to the algebra.** Three items, in increasing order of severity. First, the **connection**: the spin coefficients exist once a metric-compatible connection is chosen, but the algebra does not select one. The parent article records the same for the frame, and it is the reason the spin coefficients are described here as components of a $\mathbb{B}$-valued 1-form rather than as objects the algebra produces. Second, the **curvature**: the Weyl tensor is a rank-four object outside $\mathbb{B}$, and the five scalars are its components in $\mathrm{Sym}^4 S$. The algebra says what an element of $\mathrm{Sym}^4 S$ is, but nothing in the algebra determines which element a spacetime produces. The gravity articles already record this as open, and it remains open; this article has made the statement of the gap precise by naming the object that is missing. Third, the **dynamics and the global structure**: there are no field equations here, so the algebra cannot say which Petrov types occur, and the construction is pointwise and linear, so it carries no topological or asymptotic information. The peeling behaviour of the scalars along a null direction, for instance, is a statement about a limit and lies outside the algebra.

**On the two-sector decomposition.** The gravity articles raise the question whether the decomposition $\mathbb{M}_+\oplus\mathbb{M}_-$ organises the Weyl bivectors and the five scalars. The construction here answers it partially, and mostly negatively. The bivectors on which the self-dual Weyl tensor acts do have a native home: the algebra's bivector subspace is the six-real-dimensional traceless subspace of $\mathbb{B}$ that the parent identifies with $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$, and the three-complex-dimensional self-dual bivector space sits inside its complexification. But the Weyl tensor is not a bivector; its self-dual part is a symmetric traceless map on the three-dimensional self-dual bivector space, equivalently the spin-two object $\Psi_{ABCD}\in\mathrm{Sym}^4 S$, which is five complex dimensional. Since $\mathbb{B}$ itself is four complex dimensional, $\mathrm{Sym}^4 S$ is not a subspace of $\mathbb{B}$, and the decomposition of $\mathbb{B}$ into $\mathbb{M}_+$ and $\mathbb{M}_-$ cannot organise $\mathrm{Sym}^4 S$ as a decomposition into subspaces. The two-sector split does not, by itself, organise the Weyl scalars. Whether some finer correspondence exists — for instance between the self-dual/anti-self-dual split of the curvature and the complex structure that the algebra carries — is not settled here, and is left as an open question rather than forced.

## Summary

The Newman–Penrose formalism and the biquaternion framework meet at the null vector. This article has shown that the meeting is exact at the level of the tetrad: the four legs of a null tetrad are the four zero divisors that the algebra already distinguishes, and up to the common factor $\sqrt2\,i$ they are the matrix-unit basis of $\mathbb{B}\cong M_2(\mathbb{C})$, with the two real null directions equal to the two primitive idempotents. The inner products $l\cdot n=-1$ and $m\cdot\bar m=+1$, the off-diagonal tetrad metric, and the reconstruction of $\mathrm{diag}(-1,+1,+1,+1)$ from the tetrad were all recomputed, and the construction was checked on a dyad chosen for the check rather than on the basis dyad that suggested it.

The two objects the tetrad is used to express are hosted but not generated. The twelve spin coefficients are the components in the null basis of an $\mathfrak{sl}(2,\mathbb{C})_{\mathbb{R}}$-valued — hence $\mathbb{B}$-valued — connection; the count $4\times6=24$ real $=12$ complex was derived twice, once from the antisymmetry of the connection coefficients and once from the dimension of the traceless subspace. The five Weyl scalars are the components of the self-dual Weyl spinor $\Psi_{ABCD}\in\mathrm{Sym}^4 S$; the count $10=5$ complex was verified by exhibiting the ten-dimensional space of Weyl tensors and computing the rank of the map to the five scalars to be ten over $\mathbb{R}$. The boost weights $\Psi_k\mapsto A^{2-k}e^{i(2-k)\theta}\Psi_k$ were recomputed for all five scalars, and the Petrov classification was exhibited as the multiplicity pattern of the roots of the binary quartic in $\mathrm{Sym}^4 S$, with the canonical vanishing patterns stated together with the convention on which they depend.

The gap is the curvature itself. The algebra supplies the tetrad, the dyad, the connection's home, and the spinor module that carries the Weyl spinor; it does not supply the connection, the Weyl tensor, or the dynamics that would select one. The two-sector decomposition does not organise the Weyl scalars, because $\mathrm{Sym}^4 S$ is five complex dimensional and $\mathbb{B}$ is four. That is a negative structural finding, reported as such rather than closed.

## Summary of Notation

| Symbol | Meaning |
|--------|---------|
| $\mathbb{B}$ | biquaternion algebra $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, basis $e_0,e_1,e_2,e_3$, scalar imaginary $i$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | anti-Hermitian and Hermitian subspaces of $\mathbb{B}$; material and informational sectors |
| $\mathbb{H}_{\mathbb{B}}$ | real-quaternion subspace |
| $N(\tilde Q)=\tilde Q\bar{\tilde Q}$ | norm form; $N(\tilde Q)=\det\Phi(\tilde Q)$ |
| $\mathrm{Sc}$, $\mathrm{Tr}$ | scalar part and trace |
| $\langle\tilde Q,\tilde P\rangle=\mathrm{Sc}(\tilde Q\bar{\tilde P})$ | bilinear form on $\mathbb{M}_-$, signature $(3,1)$ |
| $\Phi$ | matrix realization $\mathbb{B}\to M_2(\mathbb{C})$, $\Phi(e_k)=-i\sigma_k$ |
| $S$, $\bar S$ | spinor module and its conjugate, $S\cong\mathbb{C}^2$ |
| $\mathrm{Sym}^4 S$ | self-dual Weyl spinors, complex dimension $5$ |
| $o,\iota$ | normalized spinor dyad, $\varepsilon(o,\iota)=1$ |
| $p,q,x,y$ | matrix units $E_{11},E_{22},E_{12},E_{21}$ in $\mathbb{B}$ |
| $E_{ij}$ | matrix with $1$ in position $(i,j)$ |
| $l,n,m,\bar m$ | null tetrad legs; $l,n$ real, $m,\bar m$ complex |
| $\eta_{ab}$ | tetrad metric, off-diagonal, (5) |
| $\varepsilon(o,\iota)$ | symplectic pairing of the spinor module |
| $\Gamma_{abc}=(\nabla_a e_b)\cdot e_c$ | connection coefficients in the tetrad |
| $\kappa,\sigma,\rho,\tau,\pi,\lambda,\mu,\nu,\varepsilon,\gamma,\beta,\alpha$ | the twelve spin coefficients |
| $D,\Delta,\delta,\bar\delta$ | directional derivatives along $l,n,m,\bar m$ |
| $C_{abcd}$ | Weyl tensor |
| $\Psi_0,\dots,\Psi_4$ | Weyl scalars, (9) |
| $\Psi_{ABCD}$ | self-dual Weyl spinor in $\mathrm{Sym}^4 S$ |
| $A,\theta$ | boost and spin parameters of the tetrad rotation |
| $z$ | complex parameter of a null rotation |

## Further Reading

- *Curved Spacetime and the Biquaternion Framework*, for the frame field and the curvature bivector.
- *Linearized Gravity in Biquaternionic Form*, for the Weyl tensor and the self-dual and anti-self-dual bivectors recorded there as an open problem.
- *Gravitational Waves in Biquaternionic Form*, for the null wave vector and the component count $10\to6\to2$ that the null tetrad is used to organise.
- *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the spinor module $S$, the matrix units $p,q,x,y$, the symplectic form, and the left and right actions on which the dyad construction rests.
- *Biquaternion Null Quadric and Projective Geometry*, for the null cone as the zero-divisor cone, the rank-one description, and the factorization of null biquaternions into mixed spinors.
- *Biquaternion Zero Divisors*, for the norm-form criterion and the classification of zero divisors used throughout.
- *The Spinor-Helicity Formalism and Biquaternions*, for the factorization of a null momentum into a spinor bilinear, of which the null tetrad is the four-legged version.
- *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material sector, its norm form, and the identification of its null cone with the zero divisors.
- *Spinors*, for the two-component spinor conventions.

