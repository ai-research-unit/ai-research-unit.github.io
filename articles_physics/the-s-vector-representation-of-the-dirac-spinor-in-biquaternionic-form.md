# __The s-Vector Representation of the Dirac Spinor in Biquaternionic Form__

## Introduction

Cartan observed that the spin group $\mathrm{Spin}(8)$ has three eight-dimensional real representations — the vector $8_v$ and the two half-spin representations $8_s, 8_c$ — and that they are permuted by an outer automorphism of order three, the *triality* of $D_4$. Triality itself is special to dimension eight: there, and only there, the three representations have the same dimension *and* an outer automorphism of order three permutes them, and the composition law that comes with the permutation is the octonion product.

In four-dimensional Minkowski space the three spaces do have dimensions four, four and four — a Lorentz vector, and the two four-real-component parts into which the Dirac field of the older literature decomposes — but $\mathrm{Spin}(1,3)$ has no order-three outer automorphism, so the coincidence of dimensions buys nothing on its own. Liu Yu-Fen asked whether a permutation can be built anyway, from extra data, and constructed what he calls a *ding* construction: an order-three map $J$ on $\mathbb{M}^{1+3}\times S_1\times S_2$ built from a triple of neutral elements, under which the Dirac field becomes a complex four-vector. The composition law it defines is that of the algebra of complexified quaternions — the biquaternion algebra — so the *vector representation of the field* is the same thing as a biquaternionic representation of it. This article records that construction, its bosonic rewriting of the Dirac Lagrangian, and the self-dual form the massive Dirac equation takes in it.

The construction is a companion to the corpus's articles on the Dirac field. There, the field is an element of $\mathbb{B}$ and the Lorentz group acts on it by left multiplication; here, a *different* linear representation of the same group — on a complex four-vector $G_\mu$ — carries the same field, and the two representations are related by fixed neutral elements. What is gained is a dictionary in which every Dirac bilinear becomes a bilinear in $G$ and its conjugate; what is paid is a preferred timelike direction, the neutral element $u_\mu$, which the dictionary needs and the metric does not supply.

The frame is $\mathbb{B}_{\Phi}$ and the metric is $\delta_{\mu\nu}=(1,1,1,1)$; the source writes $\eta_{\mu\nu}$ for the same form read in its real coordinate, whose tuple is $-\varepsilon$. Where the source contracts with one index up and one down and no metric between them, the sum here carries the sign vector $\epsilon=(1,-1,-1,-1)$, written $\sum_\mu\epsilon_\mu$, and no index is raised in this article. The only operator that differentiates the field is the gradient $\tilde\nabla$ of *Operator and Calculus Conventions*, with its conjugate $\tilde\nabla^\natural$ and the d'Alembertian $\Box$; the source's $\partial/\partial x_\mu$ keep the source's index and metric. The four generators are the four actions of §The Neutral Elements, and their legacy arrays are printed once in §The Legacy Pauli Gamma Formulation. Because $e_t$ commutes with the spatial units, $\tilde\nabla^2$ keeps the mixed time–space derivatives and is not scalar, so the mass enters through the pair of §The Chiral Pair and not through the square of one first-order derivative operator.

## The Trinomial Unit Basis

### The Neutral Elements

Chevalley's name for the units a representation is built on is *neutral elements*. The construction needs four of them: a timelike unit vector $u_\mu$, a spacelike unit vector $j_\mu$ orthogonal to it, and two neutral elements $u$ and $v$ of $\mathbb{B}$. They are normalized so that

$$
u_\mu g_{\mu\nu}u_\nu = 1, \qquad j_\mu g_{\mu\nu}j_\nu = -1, \qquad u_\mu g_{\mu\nu}j_\nu = 0,
$$

and

$$
u^{\dagger}C_0u = 1, \qquad v^{\dagger}C_0v = -1, \qquad u^{\dagger}C_0v = 0,
$$

where $C_0$ multiplies on the right by $i\vec e_x$ and $\dagger$ is Liu's adjoint of the field, so that $u^{\dagger}C_0u$ above is his scalar bilinear of the neutral element $u$. The article keeps his letters for that bilinear, which is the object his dictionary reproduces, and it writes the same pairing for any two elements as $\tilde{Ξ}_{\mathrm{sp},1}^{\dagger}C_0\tilde{Ξ}_{\mathrm{sp},2}$. Write $a_0=e_t$, $a_k=\vec e_\eta$ for the units a four-vector index multiplies on the left, and $b_0=\vec e_x$, $b_k=\vec e_y$ for those it multiplies on the right. The **generator** of index $\mu$ is the action
$$
C_\mu:\tilde{Ξ}_{\mathrm{sp}}\longmapsto i a_\mu\tilde{Ξ}_{\mathrm{sp}} b_\mu .
$$
The first generator carries the identity on its left, $a_0=e_t$, so $C_0$ multiplies on the right alone, $\tilde{Ξ}_{\mathrm{sp}}\mapsto i\tilde{Ξ}_{\mathrm{sp}}\vec e_x$, and only the three spatial generators act on both sides. The contraction of the four generators with the components $w_\mu$ is
$$
\mathcal{D}(w) := \sum_\mu w_\mu C_\mu .
$$
The reconstruction below needs the same contraction one factor of $i$ lower, on the real map:
$$
\mathcal{R}(w):\tilde{Ξ}_{\mathrm{sp}}\longmapsto-\sum_\mu w_\mu\, a_\mu\tilde{Ξ}_{\mathrm{sp}} b_\mu = \sum_\mu w_\mu\, iC_\mu\tilde{Ξ}_{\mathrm{sp}} .
$$

The vector and the neutral elements are tied together by

$$
\mathcal{D}(k)u = u, \qquad \mathcal{D}(k)v = -v, \qquad \mathcal{D}(j)u = i v, \qquad \mathcal{D}(j)v = i u .
$$

The two neutral elements are therefore the two eigenvectors of $\mathcal{D}(k)$ with eigenvalues $+1$ and $-1$. The spacelike neutral vector gives $\mathcal{D}(j)^2 = j\cdot j = -1$, so $\mathcal{D}(j)$ is a complex structure rather than an involution: its eigenvalues are $\pm i$, and it exchanges $u$ and $v$ only up to the factor $i$. This is a second place, after the definition of the generator, where $i^2=-1$ carries the sign. In the frame of the source, $k=(1,0,0,0)$ and $j=(0,0,0,-1)$, and the relations above hold with the source's two neutral elements. With $i^2=-1$ the two null elements are real in that frame, $r=u+iv$ and $l=u-iv$. The signs are the covariant ones: the contravariant $j$ is $(0,0,0,1)$, and $g_{\mu\nu}$ supplies the minus. The source writes $\mathcal{D}(j)v=u$; in the frame above the same relation appears with the factor $i$, which is the convention the source leaves implicit. The pair is null, $r^{\dagger}C_0r = l^{\dagger}C_0l = 0$.

### The Null Basis

It is often convenient to pass to the null basis

$$
r = u + i v, \qquad l = u - i v, \qquad k_\pm{}_\mu = \tfrac12(u_\mu \pm j_\mu),
$$

for which

$$
r^{\dagger}C_0l = l^{\dagger}C_0r = 2, \qquad k_\pm{}_\mu g_{\mu\nu}k_\pm{}_\nu = 0, \qquad k_\pm{}_\mu g_{\mu\nu}k_\mp{}_\nu = \tfrac12,
$$

and

$$
\mathcal{D}(k)r = l, \qquad \mathcal{D}(k_+)r = 0, \qquad \mathcal{D}(k)l = r, \qquad \mathcal{D}(k_-)l = 0 .
$$

The names are the source's: $r$ is the right and $l$ the left element of the pair. The two null vectors $k_+$ and $k_-$ are the two null directions into which $k$ and $j$ resolve.

### The Two Real Four-Vectors of the Field

Every field of the algebra carries two real four-vectors, each with four independent real components,

$$
\tilde{Ξ}_{\mathrm{sp}} = \tilde{Ξ}_{\mathrm{sp},1} + \tilde{Ξ}_{\mathrm{sp},2}, \qquad \tilde{Ξ}_{\mathrm{sp},1} = \mathcal{R}(B^\flat)v, \qquad \tilde{Ξ}_{\mathrm{sp},2} = \mathcal{R}(N^\flat)u,
$$
where $B^\flat_\nu=\sum_\mu g_{\mu\nu}B_\mu$ and $N^\flat_\nu=\sum_\mu g_{\mu\nu}N_\mu$, with

$$
B_\mu = \tfrac12\bigl(v^{\dagger}C_0\, iC_\mu\tilde{Ξ}_{\mathrm{sp}} - \tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\, iC_\mu v\bigr), \qquad
N_\mu = \tfrac12\bigl(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\, iC_\mu u - u^{\dagger}C_0\, iC_\mu\tilde{Ξ}_{\mathrm{sp}}\bigr) .
$$

The projection uses $iC_\mu$, the real map, $\tilde{Ξ}_{\mathrm{sp}}\mapsto-a_\mu\tilde{Ξ}_{\mathrm{sp}} b_\mu$: with $C_\mu$ alone the coefficients would come out $i$ times real, and the product $i\cdot i=-1$ is exactly what makes them real. The two coefficients $B_\mu$ and $N_\mu$ are **real four-vectors**, and the reconstruction $\tilde{Ξ}_{\mathrm{sp}} \mapsto (B, N) \mapsto \tilde{Ξ}_{\mathrm{sp}}$ is exact. This is the first half of the statement that the field is a pair of real four-vectors.

## The Composition Law and the Normed Condition

### The Structure Constants

Two four-index tensors are read off the four generators. A product of generators multiplies its left units into one chain and its right units into another, so the trace of such a product is four times the product of the scalar parts of the two chains, and

$$
{r'_{t}}_{\mu\nu\lambda\rho} = \mathrm{Sc}(a_\mu a_\nu a_\lambda a_\rho)\,\mathrm{Sc}(b_\rho b_\lambda b_\nu b_\mu)
= g_{\mu\nu}g_{\lambda\rho} + g_{\mu\rho}g_{\nu\lambda} - g_{\mu\lambda}g_{\nu\rho},
$$

$$
\varepsilon_{\mu\nu\lambda\rho} = \mathrm{Sc}(e_t\,a_\mu a_\nu a_\lambda a_\rho)\,\mathrm{Sc}(b_\rho b_\lambda b_\nu b_\mu\,\vec e_z),
\qquad \varepsilon_{0123} = 1 .
$$

The first is symmetric under the interchange of its two index pairs; the second is the totally antisymmetric symbol. From them and the neutral vectors come the structure constants

$$
c_{\mu\nu\lambda} = \bigl({r'_{t}}_{\mu\nu\lambda\rho} - i\varepsilon_{\mu\nu\lambda\rho}\bigr)k_\rho,
\qquad
\check c_{\mu\nu\lambda} = \bigl({r'_{t}}_{\mu\nu\lambda\rho} - i\varepsilon_{\mu\nu\lambda\rho}\bigr)j_\rho .
$$

The two differ only in which neutral vector contracts the four-index symbol; $c$ is built on the timelike $k$, $\check c$ on the spacelike $j$. In $c_{\mu\lambda\nu}$ and $\check c_{\mu\lambda\nu}$ the slots are, in order, the left input, the output and the right input. The metric is symmetric, so its slot order carries no information; the totally antisymmetric $\varepsilon$ changes sign when two of its slots are exchanged, and its slot order is part of the statement.

### The Normed Condition

The bilinear composition

$$
(G \otimes H)_\lambda = \sum_{\mu,\nu}\epsilon_\mu\epsilon_\nu\, G_\mu\, c_{\mu\lambda\nu} H_\nu,
\qquad
(G \mathbin{\check\otimes} H)_\lambda = \sum_{\mu,\nu}\epsilon_\mu\epsilon_\nu\, G_\mu\, \check c_{\mu\lambda\nu} H_\nu
$$

satisfies the identities that Hurwitz's theorem makes possible only in dimensions $1, 2, 4, 8$:

$$
(G\cdot G)(H\cdot H) = (G\otimes H)\cdot(G\otimes H),
$$

$$
(G\cdot G)(H\cdot H) = -(G\mathbin{\check\otimes} H)\cdot(G\mathbin{\check\otimes} H).
$$

The sign of the second identity is the sign difference between the timelike and the spacelike neutral vector. Both identities are the statement that the composition preserves the quadratic form up to a fixed sign — the *normed condition* of the source, and the reason the construction lands on biquaternions rather than on some arbitrary algebra.

### The Algebra

The composition is associative and non-commutative, and $k$ is its two-sided unit:

$$
(G\otimes H)\otimes K = G\otimes(H\otimes K), \qquad \sum_{\mu,\lambda}\epsilon_\mu\epsilon_\lambda\, u_\mu c_{\mu\nu\lambda} G_\lambda = G_\nu .
$$

Its realisation is the quaternion algebra. The four directions are read with $e_0=k$ as the unit, $k$ being the algebra's identity, and $e_k=i\vec e_\eta$, so that $e_k^2=e_t$ and $e_xe_y=i e_z$ cyclically: the factor $i$, through $i^2=-1$, flips both signs of the quaternion law, and those are the relations of the realisation, not of the biquaternion units themselves. The unarrowed $e_k$ is this rescaled direction, not the quaternion unit $\vec e_\eta$, whose square is $-e_t$ and whose product is $\vec e_x\vec e_y=+\vec e_z$. The neutral vector $k$ is hidden inside $c$: it is the unit element of the composition, the preferred time direction of the algebra.

## The Two Parts as Real Four-Vectors

The two real four-vectors $B_\mu$ and $N_\mu$ are the *vector representation* of the two parts of the field. The quadratic form of the field reads

$$
\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\tilde{Ξ}_{\mathrm{sp}} = -B_\mu g_{\mu\nu}B_\nu + N_\mu g_{\mu\nu}N_\nu,
$$

so the two vectors enter with opposite signs, and $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\tilde{Ξ}_{\mathrm{sp}} = N^2 - B^2$ is the difference of two norms. Neither sign is fixed by the field: in the rest frame the vector $B$ is purely spatial and $N$ vanishes, while for a field polarised along the third direction the vector $B$ is timelike. The labels *timelike* and *spacelike* that the source attaches to the two parts belong to its own metric convention; what is convention-free is the opposite sign with which the two enter $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\tilde{Ξ}_{\mathrm{sp}}$.

The complex vector $G_\mu = B_\mu + iN_\mu$ is the combined object, and its real and imaginary parts are the two parts. The two values of the chirality are a second, independent split: the field is written $\tilde{Ξ}_{\mathrm{sp},R}$ for the $+1$ value and $\tilde{Ξ}_{\mathrm{sp},L}$ for the $-1$ value, $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},R}+\tilde{Ξ}_{\mathrm{sp},L}$, and only the zero element carries both. The corresponding two parts $G_{R\mu}$ and $G_{L\mu}$ of $G_\mu$ are the subject of §The Chiral Pair. The source calls $G_\mu$ an **s-vector**, because it transforms under left multiplication by a unit biquaternion $q$, $S_1(q):\tilde{Ξ}_{\mathrm{sp}}\mapsto q\tilde{Ξ}_{\mathrm{sp}}$, whereas an ordinary spacetime vector $x_\mu$ transforms under the mixed map $\Lambda(q):x\mapsto qxq^{*}$. Two different linear representations of the same $SL(2,\mathbb{C})$ act on the same four-dimensional index.

## The Bilinear Dictionary

### The Dictionary

The reward of the s-vector representation is that every Dirac bilinear becomes a bilinear in $G$ and $G^*$ with the structure constants $c$ and $\check c$. The chirality acts by $\tilde{Ξ}_{\mathrm{sp}}\mapsto-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z$:

$$
\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\tilde{Ξ}_{\mathrm{sp}} = -\tfrac12\sum_\nu\epsilon_\nu\bigl(G_\nu G_\nu + G^*_\nu G^{*}_{\nu}\bigr),
\qquad
\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\Gamma\tilde{Ξ}_{\mathrm{sp}} = +\tfrac12\sum_\nu\epsilon_\nu\bigl(G_\nu G_\nu - G^*_\nu G^{*}_{\nu}\bigr),
$$

$$
\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\, C_\mu\tilde{Ξ}_{\mathrm{sp}} = \sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\, G_\lambda\, c_{\lambda\mu\nu}\, G^*_\nu,
\qquad
\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\,\Gamma C_\mu\tilde{Ξ}_{\mathrm{sp}} = \sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\, G_\lambda\, \check c_{\lambda\mu\nu}\, G^*_\nu .
$$
Here $\Gamma:\tilde{Ξ}_{\mathrm{sp}}\mapsto-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z$ and $C_\mu:\tilde{Ξ}_{\mathrm{sp}}\mapsto i a_\mu\tilde{Ξ}_{\mathrm{sp}} b_\mu$, so $\Gamma C_\mu:\tilde{Ξ}_{\mathrm{sp}}\mapsto a_\mu\tilde{Ξ}_{\mathrm{sp}} b_\mu\vec e_z$: the two factors of $i$ cancel by $i^2=-1$, and the axial bilinear carries no explicit imaginary unit. The slot order is the one fixed above: the first slot of $c$ belongs to the left factor, here $G_\lambda$, the middle slot to the output index $\mu$, and the last slot to the right factor, here $G^*_\nu$. Because the two factors commute as complex numbers, the sum is unchanged if the two are exchanged together with the first and last slots; it is changed if only one of the two is moved. With the opposite attachment, $\sum\epsilon_\nu\epsilon_\lambda G^*_\nu\check c_{\nu\mu\lambda}G_\lambda$, the same sum appears with the opposite sign, and the two readings must not be mixed.

The charge current is $e\,\pi_\mu = e\sum_{\rho,\sigma}\epsilon_\rho\epsilon_\sigma\, G_\rho c_{\rho\mu\sigma}G^*_\sigma = e\,\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0C_\mu\tilde{Ξ}_{\mathrm{sp}}$, the source's first bilinear, and it is the vector identity above with the summation indices renamed $\lambda\to\rho$, $\nu\to\sigma$. The operator that carries the split is the right multiplication
$$
\Gamma:\tilde{Ξ}_{\mathrm{sp}}\longmapsto-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z,
$$
a pure right multiplier, so its side is the right slot and its two eigenspaces are the two values of every field. In the reference frame it is the ordered product of the four generators up to the factor $i$, and it anticommutes with each $C_\mu$; both are properties of the basis operator, and neither is what makes it a chirality. Its array on that frame, written in §The Legacy Pauli Gamma Formulation, is the usual fifth generator. The source further rewrites the mass form as

$$
\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\tilde{Ξ}_{\mathrm{sp}} = \sum_\mu\epsilon_\mu\, U_{\mathrm{vec},\mu}\,\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\, C_\mu\tilde{Ξ}_{\mathrm{sp}}
$$

for a unit complex vector $U_{\mathrm{vec},\mu}$ built from $\tilde{Ξ}_{\mathrm{sp}}$; that interpretation — the mass as a unit vector, hence as a non-integrable phase — is recorded in *The Dirac Equation in Biquaternionic Form*, and this article takes it as the entry into the same construction.

### The Cubicity of the Interaction

The vector, the first part and the second part are permuted by the order-three map

$$
J : \ A \mapsto B \mapsto N \mapsto A,
$$

which leaves the trilinear form

$$
A_\mu\bigl(\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0_{(1)}\, C_\mu\tilde{Ξ}_{\mathrm{sp},(2)} + \tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0_{(2)}\, C_\mu\tilde{Ξ}_{\mathrm{sp},(1)}\bigr)
= 2\sum_{\nu,\lambda,\sigma}\epsilon_\nu\epsilon_\lambda\epsilon_\sigma\, A_\mu\, \varepsilon_{\lambda\mu\nu\sigma}N_\lambda B_\nu k_\sigma
$$

invariant. This is the *ding*: the fourth-dimensional analogue of Cartan's triality, with the biquaternion algebra in place of the octonions, and the vector, the timelike unit $k$ and the two parts playing the roles the three eight-dimensional spaces play in the $\mathrm{Spin}(8)$ case. Written with the first slot of the symbol on $B$ instead, $\varepsilon_{\nu\mu\lambda\sigma}B_\nu N_\lambda$, the same sum changes sign; the identity above is the version in which each symbol carries its factors in the order of its slots.

The fuller cubic form is linear in the vector $A$ and quadratic in the two parts. Its three-index symbols are the four-index ones contracted with $k$,
$$
{r'_{t}}_{\nu\mu\lambda}:={r'_{t}}_{\nu\mu\lambda\sigma}k_\sigma,
\qquad
\varepsilon_{\mu\lambda\nu}:=\varepsilon_{\mu\lambda\nu\sigma}k_\sigma,
$$
and the form is
$$
C = \sum_\mu A_\mu\,\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\, C_\mu\tilde{Ξ}_{\mathrm{sp}}
= \sum_{\mu,\nu,\lambda}\epsilon_\nu\epsilon_\lambda\, A_\mu\, G_\lambda\, c_{\lambda\mu\nu}\, G^*_\nu .
$$
For real $A$ its real part is the source's cubic form,
$$
\mathrm{Re}\,C = \sum_{\mu,\nu,\lambda}\epsilon_\nu\epsilon_\lambda\, A_\mu\Bigl[{r'_{t}}_{\nu\mu\lambda}\bigl(B_\nu B_\lambda + N_\nu N_\lambda\bigr) + 2\varepsilon_{\mu\lambda\nu}B_\lambda N_\nu\Bigr],
$$
with the symmetric $r'_t$ pairing each part with itself and the antisymmetric $\varepsilon$ pairing the two; the imaginary part is a second $r'_t$ contraction of $B$ and $N$, which the compact form keeps inside the single complex number $C$. The two together complete the dictionary of the three quadratic forms and the one cubic form that define the algebra.

## The Bosonic Form of the Dirac Lagrangian

Passing from the field to the s-vector representation turns the Dirac Lagrangian into

$$
\tfrac12\sum_\mu\epsilon_\mu\bigl[\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\, C_\mu(\partial/\partial x_\mu - ieA_\mu)\tilde{Ξ}_{\mathrm{sp}} - \bigl((\partial/\partial x_\mu + ieA_\mu)\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\bigr) C_\mu\tilde{Ξ}_{\mathrm{sp}}\bigr] - k_m\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\tilde{Ξ}_{\mathrm{sp}}
$$

$$
= \tfrac12\Bigl[\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\bigl(\tilde\nabla_\mu G_\nu\bigr)^* i\check c_{\nu\mu\lambda} G_\lambda - \sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda G^*_\nu\, i\check c_{\nu\mu\lambda}\, \tilde\nabla_\mu G_\lambda + m\sum_\nu\epsilon_\nu\bigl(G^{*}_\nu G^{*}_{\nu} + G_\nu G_\nu\bigr)\Bigr],
$$

with the covariant derivative

$$
\tilde\nabla_\mu G_\lambda = \partial/\partial x_\mu G_\lambda - ieA_\mu\, g_{\lambda\rho}\, c_5{}_{\rho\sigma} G_\sigma .
$$

On the two parts the connection collapses to an ordinary phase, because $c_5{}_{\rho\sigma}G_{R\sigma}=+G_{R\rho}$ and $c_5{}_{\rho\sigma}G_{L\sigma}=-G_{L\rho}$:

$$
\tilde\nabla_\mu G_{R\lambda} = \bigl(\partial/\partial x_\mu - ieA_\mu\bigr)G_{R\lambda},
\qquad
\tilde\nabla_\mu G_{L\lambda} = \bigl(\partial/\partial x_\mu + ieA_\mu\bigr)G_{L\lambda} .
$$

The opposite charges of the two parts are thus the two eigenvalues of $c_5$, and the gauge field couples to them with opposite signs, as a gauge field on two values must.

Both kinetic terms carry the same combination $i\check c$, and that product is not purely imaginary, because $\check c$ already contains an $i$. Since $\check c_{\mu\nu\lambda}=({r'_{t}}_{\mu\nu\lambda\rho}-i\varepsilon_{\mu\nu\lambda\rho})j_\rho$, the combination is
$$
i\check c_{\mu\nu\lambda}=\varepsilon_{\mu\nu\lambda\rho}j_\rho+i\,{r'_{t}}_{\mu\nu\lambda\rho}j_\rho,
$$
so the operator has a real $\varepsilon$ part and an imaginary $r'_t$ part. The two kinetic terms are not equal and not merely conjugate: writing $T_1$ for the first and $T_2$ for the second, conjugation exchanges them with a minus,
$$
T_2=-\overline{T_1},
$$
so the combination $T_1-T_2=T_1+\overline{T_1}$ is real. The minus comes from the antisymmetry of $\varepsilon$ under the exchange of the two slots it carries.

Two features are worth naming. The kinetic operator is not symmetric in $G$ and $G^*$: the two terms differ by a sign as well as by conjugation, and that is what makes their difference real. The mass term is $m(G^*G^* + GG)$, not $mG^*G$: the mass couples $G$ to $G^*$ rather than to itself, which is the shadow of the mass that relates the two parts of the field. The kinetic operator separates the two values the way a Dirac operator does in a four-vector carrier.

The mass is not carried by the square of a first-order derivative operator. The derivative of the article is the gradient, and the gradient's square is not scalar, because $e_t$ commutes with the spatial units and the mixed time–space derivatives survive in $\tilde\nabla^2=\Box+2\sum_\eta\vec e_\eta\,\partial^2/\partial R_t\partial R_\eta$. Only the paired product $\tilde\nabla\tilde\nabla^\natural=\Box$ is scalar, and it conjugates one factor instead of squaring it. The free equation is therefore first order in one field, $i\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\,\tilde\nabla_\nu G_\lambda=0$ at $m=0$; the massive system is the pair of §The Chiral Pair, and the mass sits between the two values rather than inside one square.

The pair does imply the Klein–Gordon equation, and the implication runs through the paired product. On the element, from $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde\nabla^\natural\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$, applying $\tilde\nabla^\natural$ to the first equation and $\tilde\nabla$ to the second gives $\tilde\nabla^\natural\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m^{2}\tilde{Ξ}_{\mathrm{sp},R}$ and $\tilde\nabla\tilde\nabla^\natural\tilde{Ξ}_{\mathrm{sp},L}=k_m^{2}\tilde{Ξ}_{\mathrm{sp},L}$, that is

$$
\bigl(\Box-k_m^{2}\bigr)\tilde{Ξ}_{\mathrm{sp},R}=0,\qquad\bigl(\Box-k_m^{2}\bigr)\tilde{Ξ}_{\mathrm{sp},L}=0,
$$

since $\tilde\nabla^\natural\tilde\nabla=\tilde\nabla\tilde\nabla^\natural=\Box$ is scalar. Each value obeys the Klein–Gordon equation, and the first-order system is the pair, not the square root of a scalar operator. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

The bosonization is not canonical. It depends on the choice of the neutral elements $j_\mu$ and $u_\mu$: the Lagrangian is built from $\check c$, and $\check c$ is built from $j$. Any orthogonal pair with $k\cdot k = -j\cdot j = 1$ serves, they are arbitrary but must be fixed; the remaining symbols $c_{\mu\nu\lambda}$, $c_5{}_{\rho\sigma}$ and the rest are reconstructed once $j$ and $k$ are chosen.

## The Two Equations and the Self-Dual Form

### The Chiral Pair

The massive Dirac equation in the vector representation has **two values**, and the mass couples them. Split into its two values, the equation reads two equations, not one:

$$
\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\, i(\partial/\partial x_\nu-ieA_\nu)G_{R\lambda} - m\,G^{*}_{L\mu}=0,
$$
$$
\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\, i(\partial/\partial x_\nu+ieA_\nu)G_{L\lambda} - m\,G^{*}_{R\mu}=0,
$$

where $G_{R\mu}$ and $G_{L\mu}$ are the two parts of $G_\mu$: the $+1$ and the $-1$ value of $c_5$,

$$
c_5{}_{\mu\nu}G_{R\nu}=+G_{R\mu},
\qquad
c_5{}_{\mu\nu}G_{L\nu}=-G_{L\mu},
\qquad
G_\mu=G_{R\mu}+G_{L\mu}.
$$

The single complex equation

$$
i\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\,\tilde\nabla_\nu G_\lambda - m\, G^{*}_{\mu} = 0
$$

is the compact form of the same pair at $A_\mu=0$: the two equations above are its two values, and every $G_\mu$ is their sum. Both halves are quoted in the source's letters, $\partial/\partial x_\nu$ its index partial and $A_\nu$ its gauge field; the compact line writes the same equation in the corpus gradient, whose $\nu$-th leg stands in that slot. This is the two-value structure of the element's equation, carried to the four-vector carrier. On the element the same pair reads

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde\nabla^\natural\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R},
$$

with the mass $me_t$ central, $e_t$ being the identity of the algebra. Nothing in the mass term flips the value by itself; the term is off-diagonal only in the sense that the two equations are written as a pair, and each value is carried into the other by the mass. The pair on $G$ and the pair on $\tilde{Ξ}_{\mathrm{sp}}$ are the same two equations in two carriers.

Equivalently, with $A_\mu = 0$, the pair is the self-dual system

$$
G_{\mu\nu} = \tfrac{i}{2}\,\varepsilon_{\mu\nu\lambda\rho} G_{\lambda\rho},
\qquad
\sum_\mu\epsilon_\mu\bigl(\partial/\partial x_\mu G_\mu + i m j_\mu G^{*}_{\mu}\bigr) = 0,
$$

where

$$
G_{\mu\nu} = \bigl(\partial/\partial x_\mu G_\nu - im\,j_\mu G^*_\nu\bigr) - \bigl(\partial/\partial x_\nu G_\mu - im\,j_\nu G^*_\mu\bigr).
$$

The first equation is a self-duality condition on the field strength $G_{\mu\nu}$, the second a divergence condition with the same mass term, $+im\,j_\mu G^*_\mu$. The two entries together are the compact equation rewritten at $A_\mu=0$, and neither stands alone.

### The Two Parts and the 2-Form

The two parts $G_{R\mu}$ and $G_{L\mu}$ of §The Chiral Pair are the two values of $c_5{}_{\mu\nu}$ read on $G_\mu$; the equation of motion is the pair displayed there. The two-form

$$
H_{\mu\nu} := \sum_\lambda\epsilon_\lambda\, G^*_\lambda\, \check c_{\lambda\mu\nu}
$$

is not antisymmetric. Its symmetric part is proportional to the metric, $H_{(\mu\nu)}=\xi_{\mathrm{scl}}\,g_{\mu\nu}$, with $\xi_{\mathrm{scl}}=\tfrac14 g_{\mu\nu}H_{\mu\nu}$, and its antisymmetric part is **anti-self-dual**,

$$
H_{[\mu\nu]} = -\tfrac{i}{2}\sum_{\lambda,\rho}\epsilon_\lambda\epsilon_\rho\,\varepsilon_{\mu\nu\lambda\rho} H_{[\lambda\rho]},
$$

so the antisymmetric part, which has six real components, is carried by three complex ones. This is the biquaternion analogue of the electromagnetic field, whose six real components are carried by the single biquaternion $\vec E+i\vec H$: the source notes that only the three-dimensional vector part of a biquaternion has the Maxwell analogy. In these variables the uncharged Dirac equation reads

$$
\sum_\nu\epsilon_\nu\,\partial/\partial x_\nu H_{\nu\mu} - \tfrac{im}{2}\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\bigl(\check c_{\nu\mu\lambda}H_{\nu\lambda}\bigr)^* = 0.
$$

The source reads the resulting pair of equations as a Maxwell system with both "electric" and "magnetic" currents, and records the identity

$$
\tfrac14\bigl[G_{\mu\nu}\varepsilon_{\mu\nu\lambda\rho}G_{\lambda\rho} + G^*_{\mu\nu}\varepsilon_{\mu\nu\lambda\rho}G^*_{\lambda\rho}\bigr]
= 2\partial/\partial x_\mu\Bigl[\varepsilon_{\mu\nu\lambda\rho}\bigl(B_\nu\partial/\partial x_\lambda B_\rho - N_\nu\partial/\partial x_\lambda N_\rho + 2mB_\nu N_\lambda j_\rho\bigr)\Bigr],
$$

a Chern–Pontryagin-type density equal to a total derivative of a Chern–Simons-type current. The Dirac Lagrangian can therefore be modified by that total derivative, which is the entry into the topologically massive gauge field of the companion article *Dual Equivalence of the Dirac and Topologically Massive Gauge Fields*.

## The U(1) Transformation and the De Moivre Theorem

The index space carries the involution $c_5{}_{\mu\nu}$ with the defining property

$$
c_5{}_{\mu\rho} g_{\rho\sigma} c_5{}_{\sigma\nu} = g_{\mu\nu},
\qquad (c_5)^2 = 1 .
$$

In the neutral frame $k=(1,0,0,0)$, $j=(0,0,0,-1)$ it acts as

$$
c_5:k\longmapsto-j,\qquad j\longmapsto-k,\qquad \vec e_1\longmapsto i\vec e_2,\qquad \vec e_2\longmapsto-i\vec e_1,
$$

so it exchanges the two neutral vectors up to a sign and rotates the pair of spacelike directions by $i$. Its values are real on the neutral pair and imaginary on the spacelike pair; it is Hermitian, squares to the identity, and is $g$-antisymmetric,

$$
\sum_\lambda c_5{}_{\lambda\mu}g_{\lambda\nu} = -\sum_\lambda g_{\mu\lambda}c_5{}_{\lambda\nu},
$$

so its eigenvalues are $+1$ and $-1$, the two parts are orthogonal, and $e^{-i\alpha c_5}$ is an isometry of the quadratic form. It mixes $G_0$ with $G_3$ and $G_1$ with $G_2$; it does not separate time from space, and the action is basis-dependent, the values above being a representative of the chirality rather than the chirality itself.

The last two of these properties are what make the *chiral-type* rotation

$$
M(\alpha)_{\mu\nu} = \delta_{\mu\nu}\cos\alpha - i c_5{}_{\mu\nu}\sin\alpha = \bigl(\exp(-i\alpha c_5)\bigr)_{\mu\nu}
$$

an isometry of the quadratic form $q(G)=G_\mu g_{\mu\nu}G_\nu$: the $g$-antisymmetry makes the cross terms cancel, and $c_5^2=1$ makes the diagonal terms add to $g$, so $M^{\mathsf T}gM=g$. Because $c_5^2=1$ it also obeys the De Moivre theorem,

$$
\bigl(\cos\alpha - i c_5\sin\alpha\bigr)^n = \cos n\alpha - i c_5\sin n\alpha .
$$

The mass term $k_m\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\tilde{Ξ}_{\mathrm{sp}} = -\tfrac{k_m}{2}(G^*G^* + GG) = +\tfrac{k_m}{2}\bigl[q(G)+q(G^*)\bigr]$ is invariant under $M(\alpha)$ for that reason, and it is *not* invariant under the ordinary phase $G_\mu\mapsto e^{i\alpha}G_\mu$, which multiplies $q$ by $e^{2i\alpha}$.

The source identifies $M(\alpha)$ with the image of the field's vector $\mathrm{U}(1)$, $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}}\exp(i\alpha)$. The dictionary is narrower than that. The exact correspondence runs through the *chiral* transformation: $\tilde{Ξ}_{\mathrm{sp}}\mapsto\exp(-ia\Gamma)\tilde{Ξ}_{\mathrm{sp}}$ becomes the ordinary phase $G_\mu\mapsto e^{ia}G_\mu$, and $\tilde{Ξ}_{\mathrm{sp}}\mapsto\exp(ia\Gamma)\tilde{Ξ}_{\mathrm{sp}}$ becomes $G_\mu\mapsto e^{-ia}G_\mu$. The vector phase does not act diagonally on $G$ at all. Since $v^{\dagger}C_0\,iC_\mu\tilde{Ξ}_{\mathrm{sp}}$ and $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\,iC_\mu v$ are conjugate up to sign, $B_\mu$ is the real part of $X_\mu:=v^{\dagger}C_0\,iC_\mu\tilde{Ξ}_{\mathrm{sp}}$, and the phase sends

$$
B_\mu \mapsto B_\mu\cos\alpha - \mathrm{Im}(X_\mu)\sin\alpha,
$$

with $N_\mu$ treated the same way through $Z_\mu:=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\,iC_\mu u$: a mixing of the two parts, not a rotation of each. So $M(\alpha)$ is the transformation the mass form invites, and it is the one to use in the algebra, but it is not the image of a symmetry of the field.

## The Dual Transformation and the Two Parts

The map

$$
B \mapsto N, \qquad N \mapsto -B, \qquad m \mapsto -m
$$

leaves the quadratic form $k_m\tilde{Ξ}_{\mathrm{sp}}^{\dagger}C_0\tilde{Ξ}_{\mathrm{sp}} = k_m\sum_\nu\epsilon_\nu(N_\nu N_\nu - B_\nu B_\nu)$, the cubic form $\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda V_\mu B_\nu N_\lambda\varepsilon_{\nu\mu\lambda}$ and hence the Lagrangian and the equation of motion invariant. The source reads this as the statement that the part of the first type is *dual* to the part of the second type, on the model of the electromagnetic duality that exchanges $\vec E$ and $\vec H$ while exchanging $e$ and a magnetic coupling. It is the first-order shadow of the parent-action duality between the Dirac Lagrangian and the second-order topologically massive gauge Lagrangian, and it is the reason the two Lagrangians can describe the same propagating modes.

## What the Construction Does and Does Not Supply

**It supplies** a genuine, verified linear equivalence between the field and a complex four-vector, with the whole bilinear dictionary, a bosonic form of the Lagrangian, and a self-dual form of the massive equation. The central algebraic identities quoted above — the normed condition, associativity, the unit, the four-index traces $r'_t$ and $\varepsilon$, the reality of the two four-vectors, the recovery of $k$ and $j$ from $c$ and $\check c$, the mass, chiral and vector bilinears, the anti-self-duality of $H_{[\mu\nu]}$, and the trilinear form — were recomputed on the corpus's convention and hold. Where the source's printed sign differs, the difference is the slot order of $c$ and $\varepsilon$, not the identity; the De Moivre theorem follows from $(c_5)^2=1$.

**It does not supply** a Lorentz-covariant construction. The neutral elements $j_\mu$ and $u_\mu$ are *extra structure*: they are not determined by the metric, they are the two directions the construction singles out, and the algebra's unit is $k$. The source is explicit that this is a defect of the incomplete algorithm and, in the same breath, a virtue: the structure constants *do* return the neutral vectors by contraction,
$$
\sum_\mu\epsilon_\mu\,c_{\mu\mu\lambda}=4k_\lambda,
\qquad
\sum_\mu\epsilon_\mu\,\check c_{\mu\mu\lambda}=-4j_\lambda,
$$
so the preferred frame is not put in by hand in the final form, it is the algebra's own unit. But it is still a preferred frame, and a Lorentz transformation that moves $k$ is not a symmetry of the individual dictionary, only of the equivalence class of dictionaries. The source's own warning applies: the triality map $J$ is *not* a symmetry of the theory; it maps one description of the theory to another description of the same theory.

**It does not supply** any new physics. The construction is a re-encoding of the Dirac equation in a different linear representation of the same Lorentz group, and its predictions — the mass shell, the propagator, the cross sections — are those of the Dirac equation. What it changes is the *language*: the mass is a non-integrable phase, the next-to-topological density is a total derivative, and the photon–electron relation becomes a duality between a first-order and a second-order description. The physics is the same; the bookkeeping is different, and cleaner.

## Open Questions

1. **The preferred frame.** Is the neutral vector $u_\mu$ a genuine extra structure, or is it fixed by the algebra as the source claims? The corpus's *Algebra and Element Conventions* already distinguishes the algebra from the spacetime it is applied to; the question is whether $k$ is a fact about the algebra or a fact about the embedding.

2. **The relation to the corpus's carrier of the field.** In the corpus the field is an element of $\mathbb{B}$ and the Lorentz group acts on it by left multiplication; here it is a complex four-vector. Both are four-complex-dimensional and carry the same left action of $\mathbb{B}$, so as modules they are equivalent, and the neutral elements give the explicit intertwiner. What is not settled is which basis makes the dictionary readable: the equivalence of the modules does not by itself select the trinomial unit basis.

3. **The lattice consequence.** The source suggests, as "further speculation", that because the dualized Dirac equation is second order, and second-order Lagrangians have no fermion-doubling problem, the vector representation offers a route around the Nielsen–Ninomiya obstruction. The corpus's *Fermion Doubling and the Nielsen–Ninomiya Theorem* treats that obstruction as a lattice statement; whether the s-vector representation evades its hypotheses, or merely restates them in a different field variable, is open.

4. **The interaction with a preferred frame.** If $u_\mu$ is physical, the construction singles out a preferred direction in the vacuum. Does the resulting theory violate Lorentz invariance observably, or is $k$ a gauge artifact of the description? The source does not say.

5. **Extension beyond four dimensions.** The construction uses the Lorentzian four-dimensional signature essentially — the source notes that a biquaternion description would not work if the dimension and signature were different. What happens at the next triality dimension, eight, where the algebra is the octonions and the vector and the two part spaces coincide, is the Cartan case the corpus records in *Triality and Spin(8) with Inner Conjugation*.

These questions are open.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The four gammas are the generators of the body, $\gamma_\mu=C_\mu$, the four actions of §The Trinomial Unit Basis, and together they are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

$$
\gamma_0:\tilde{Ξ}_{\mathrm{sp}}\longmapsto i\tilde{Ξ}_{\mathrm{sp}}\vec e_x,\quad \gamma_1:\tilde{Ξ}_{\mathrm{sp}}\longmapsto i\vec e_x\tilde{Ξ}_{\mathrm{sp}}\vec e_y,\quad \gamma_2:\tilde{Ξ}_{\mathrm{sp}}\longmapsto i\vec e_y\tilde{Ξ}_{\mathrm{sp}}\vec e_y,\quad \gamma_3:\tilde{Ξ}_{\mathrm{sp}}\longmapsto i\vec e_z\tilde{Ξ}_{\mathrm{sp}}\vec e_y,\quad \gamma_5:\tilde{Ξ}_{\mathrm{sp}}\longmapsto-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z.
$$

Each is an action with both elements written in the arrow; $\gamma_0$ and $\gamma_5$ carry the identity on the left and act on the right alone. The arrays the literature prints are these actions in the Peirce frame, and the axis-free arrays of the corpus are the same actions in the corpus frame; a change of frame changes no product, no anticommutator, no trace and no determinant, so every identity here holds in both. Products stay in the same language: the product of two actions is one action, $(\tilde{Ξ}_{\mathrm{sp}}\mapsto a\tilde{Ξ}_{\mathrm{sp}} b)\circ(\tilde{Ξ}_{\mathrm{sp}}\mapsto c\tilde{Ξ}_{\mathrm{sp}} d)=\tilde{Ξ}_{\mathrm{sp}}\mapsto ac\tilde{Ξ}_{\mathrm{sp}} db$, so a product of the symbols here never needs a second notion of operator. An action is one product, and a sum of at most four actions is any $\mathbb{C}$-linear map of the algebra to itself.

The field of the older literature is a four-component spinor, a column of a minimal left ideal, and the arrays of this section are its matrices; the corpus writes the same field as an element of $\mathbb{B}$ and keeps the array as a display, which is why no $\gamma$ symbol and no column appears in the body of the article.

$\gamma_5$ is the reference-frame representative of the chirality: the ordered product $i\gamma_0\gamma_1\gamma_2\gamma_3$, which is the right action $\Gamma:\tilde{Ξ}_{\mathrm{sp}}\mapsto-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z$ written in the frame; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module. The symbol $\Gamma$ is not a gamma matrix: $\Gamma$ is the chirality in the algebra, and $\gamma_5$ is its representative on the reference frame.

## Summary

The field of four-dimensional Minkowski space decomposes into two parts, and each part is a **real four-vector**: $\tilde{Ξ}_{\mathrm{sp},1} = \mathcal{R}(B^\flat)v$ and $\tilde{Ξ}_{\mathrm{sp},2} = \mathcal{R}(N^\flat)u$ with real $B_\mu, N_\mu$, where $B^\flat_\nu=\sum_\mu g_{\mu\nu}B_\mu$ and $N^\flat_\nu=\sum_\mu g_{\mu\nu}N_\mu$. The combined object $G_\mu = B_\mu + iN_\mu$ is an **s-vector**, and the map $\tilde{Ξ}_{\mathrm{sp}} \leftrightarrow G$ is a linear equivalence. It rests on a trinomial unit basis — a timelike unit vector $u_\mu$, a spacelike unit vector $j_\mu$, and two neutral elements $u, v$ — the neutral elements of Chevalley. The composition law $c_{\mu\nu\lambda} = ({r'_{t}}_{\mu\nu\lambda\rho} - i\varepsilon_{\mu\nu\lambda\rho})k_\rho$ built from the four-index traces $r'_t$ and $\varepsilon$ is associative, has $k$ as its unit, and satisfies the normed condition $(G\cdot G)(H\cdot H) = (G\otimes H)\cdot(G\otimes H)$; its realisation is the quaternion algebra read with $e_0=k$ and $e_k=i\vec e_\eta$, so that $e_k^2=e_t$ and $e_xe_y=i e_z$. The Dirac bilinears become $G$-$G^*$ bilinears with the structure constants $c$ and $\check c$, and the order-three map $A\mapsto B\mapsto N\mapsto A$ permutes the vector and the two parts while leaving the trilinear form invariant — the *ding* construction, the four-dimensional analogue of Cartan's triality, with the biquaternion algebra in place of the octonions.

The Dirac Lagrangian becomes bosonic: a quadratic kinetic term in $G$ with the $\check c$ structure constants, and a mass term $m(G^*G^* + GG)$ that couples $G$ to $G^*$ — the mass that relates the two parts of the field in another guise. The massive equation becomes the pair of §The Chiral Pair, or equivalently the self-dual pair $G_{\mu\nu} = \tfrac{i}{2}\varepsilon_{\mu\nu\lambda\rho}G_{\lambda\rho}$, $\sum_\mu\epsilon_\mu\bigl(\partial/\partial x_\mu G_\mu + imj_\mu G^{*}_{\mu}\bigr) = 0$, with the antisymmetric part of the two-form $H_{\mu\nu} = G^*_\lambda\check c_{\lambda\mu\nu}$ anti-self-dual. Because $(c_5)^2=1$ and $c_5$ is $g$-antisymmetric, the chiral-type rotation $G\mapsto(\cos\alpha-ic_5\sin\alpha)G$ is an isometry of the quadratic form, obeys the De Moivre theorem, and leaves the mass term invariant; the chiral transformation of the field, by contrast, is an ordinary $\mathrm{U}(1)$ phase of $G$. The dual map $B \mapsto N$, $N \mapsto -B$, $m \mapsto -m$ leaves the theory invariant.

What the construction supplies is a dictionary; what it does not supply is covariance or new physics. The neutral elements $u_\mu$ and $j_\mu$ are a preferred frame. They are not determined by the metric; the contractions $\sum_\mu\epsilon_\mu c_{\mu\mu\lambda}=4k_\lambda$ and $\sum_\mu\epsilon_\mu\check c_{\mu\mu\lambda}=-4j_\lambda$ return them from the structure constants, so the frame is the algebra's own, but it is still a frame, and the corpus records the question as open. The triality map is not a symmetry; it maps one description to another description of the same theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mu, \nu, \lambda, \rho$ | Ordinary Minkowski four-vector indices, $0,1,2,3$ |
| $\delta_{\mu\nu}=(1,1,1,1)$ | The metric, the identity in the four-index space; no index is raised anywhere. The source's $\eta$ is the same form in the real coordinate, tuple $-\varepsilon$ |
| $V\cdot W$ | Minkowski pairing of two four-vectors, the sign vector $\epsilon$ supplying the signs |
| $u_\mu, j_\mu$ | Timelike and spacelike unit neutral vectors, $k\cdot k = -j\cdot j = 1$, $k\cdot j = 0$ |
| $u, v$ | The two neutral elements of $\mathbb{B}$, $u^{\dagger}C_0u = 1$, $v^{\dagger}C_0v = -1$, $u^{\dagger}C_0v = 0$ |
| $r = u+iv$, $l = u-iv$ | The two null elements, $r^{\dagger}C_0l = l^{\dagger}C_0r = 2$ |
| $k_\pm{}_\mu = \tfrac12(u_\mu\pm j_\mu)$ | Null vectors formed from the neutral pair |
| $e_t, \vec e_\eta$ | The four units of $\mathbb{B}$ |
| $a\tilde{Ξ}_{\mathrm{sp}} b$ | An action of the algebra on itself, $a$ on the left and $b$ on the right (see *Operator and Calculus Conventions*) |
| $\tilde\nabla$, $\tilde\nabla^\natural$, $\Box$ | The gradient, its conjugate and the d'Alembertian of *Operator and Calculus Conventions*, with $\varepsilon=(1,-1,-1,-1)$ |
| $a_\mu, b_\mu$ | Left and right units of the index: $a_0 = e_t$, $a_k = \vec e_\eta$, $b_0 = \vec e_x$, $b_k = \vec e_y$ |
| $C_\mu:\tilde{Ξ}_{\mathrm{sp}}\mapsto i a_\mu\tilde{Ξ}_{\mathrm{sp}} b_\mu$ | The generator of index $\mu$: two-sided on the three spatial indices, the single right action $\tilde{Ξ}_{\mathrm{sp}}\mapsto i\tilde{Ξ}_{\mathrm{sp}}\vec e_x$ on the time index |
| $\mathcal{D}(w) = \sum_\mu w_\mu C_\mu$ | The four generators contracted, a sum of four actions, as it appears in the bilinears |
| $\mathcal{R}(w):\tilde{Ξ}_{\mathrm{sp}}\mapsto-\sum_\mu w_\mu\,a_\mu\tilde{Ξ}_{\mathrm{sp}} b_\mu$ | The same sum one factor of $i$ lower, the real map of the reconstruction |
| $\tilde{Ξ}_{\mathrm{sp},1}^{\dagger}C_0\tilde{Ξ}_{\mathrm{sp},2}$ | Liu's bilinear of two elements, the object the dictionary reproduces |
| $\mathrm{Sc}$ | Scalar part of a biquaternion |
| ${r'_{t}}_{\mu\nu\lambda\rho} = \mathrm{Sc}(a_\mu a_\nu a_\lambda a_\rho)\mathrm{Sc}(b_\rho b_\lambda b_\nu b_\mu)$ | Symmetric four-index trace |
| $\varepsilon_{\mu\nu\lambda\rho}$ | The totally antisymmetric symbol, $\varepsilon_{0123}=1$; a different letter from the sign vector $\epsilon$ |
| $c_{\mu\nu\lambda} = ({r'_{t}}_{\mu\nu\lambda\rho}-i\varepsilon_{\mu\nu\lambda\rho})k_\rho$ | Structure constants built on $k$ |
| $\check c_{\mu\nu\lambda} = ({r'_{t}}_{\mu\nu\lambda\rho}-i\varepsilon_{\mu\nu\lambda\rho})j_\rho$ | Structure constants built on $j$ |
| $c_5{}_{\mu\nu}$ | The $g$-antisymmetric involution of the index space, $(c_5)^2 = 1$; it carries the value $+1$ on $G_{R}$ and $-1$ on $G_{L}$ |
| $\Gamma:\tilde{Ξ}_{\mathrm{sp}}\mapsto-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z$ | The chirality, a right action of the algebra |
| $(G\otimes H)_\lambda = \sum_{\mu,\nu}\epsilon_\mu\epsilon_\nu\,G_\mu c_{\mu\lambda\nu}H_\nu$ | Composition law |
| $B_\mu, N_\mu$ | Real four-vectors of the two parts of the field |
| $G_\mu = B_\mu + iN_\mu$ | s-Vector (the vector representation of the field) |
| $\tilde{Ξ}_{\mathrm{sp},R}, \tilde{Ξ}_{\mathrm{sp},L}$ | The two parts of the field, one per letter of the pair |
| $G_{R\mu}, G_{L\mu}$ | The two parts of the s-vector, the two values of $c_5$ |
| $\tilde{Ξ}_{\mathrm{sp},1}, \tilde{Ξ}_{\mathrm{sp},2}$ | The two parts of the field |
| $G_{\mu\nu}$ | Field strength of the self-dual form |
| $H_{\mu\nu} = G^*_\lambda\check c_{\lambda\mu\nu}$ | Two-form; its antisymmetric part is anti-self-dual |
| $\xi_{\mathrm{scl}} = \tfrac14 g_{\mu\nu}H_{\mu\nu}$ | Complex scalar in $H_{(\mu\nu)}=\xi_{\mathrm{scl}}\,g_{\mu\nu}$, the trace part of $H$ |
| $A_\mu$ | Electromagnetic four-potential |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Liu Yu-Fen, "Triality, Biquaternion and Vector Representation of the Dirac Equation," arXiv:math-ph/0109008 (2001), for the trinomial unit basis and the neutral elements, the composition law $c_{\mu\nu\lambda}$ and the normed condition, the four-vectors $B_\mu, N_\mu$, the s-vector $G_\mu = B_\mu + iN_\mu$, the bilinear dictionary, the bosonic Dirac Lagrangian, the self-dual form of the massive equation, the $\mathrm{U}(1)$ transformation and the De Moivre theorem, and the dual map $B \leftrightarrow N$. The explicit matrices $\vec u_{\nu}$ are its equations (16)–(18).
- Liu Yu-Fen, "Triality and Dual Equivalence Between Dirac Field and Topologically Massive Gauge Field," arXiv:hep-th/0602275 (2006), for the restatement of the construction with the fuller cubic form, the braid-group "Dirac's game", the two parts $G_{R\mu}, G_{L\mu}$, the anti-self-dual two-form $H_{\mu\nu}$, the chiral form of the equation of motion, and the parent-action duality carried in the companion article *Dual Equivalence of the Dirac and Topologically Massive Gauge Fields*.
- E. Cartan, *Leçons sur la théorie des spineurs* I, II (Hermann, Paris, 1938); English translation by R. Streater, *The Theory of Spinors* (Hermann, Paris, 1966), for the original triality of $\mathrm{Spin}(8)$.
- C. C. Chevalley, *The Algebraic Theory of Spinors* (Columbia University Press, New York, 1954), for the neutral elements of a spin representation.
- J. F. Adams, *Lectures on Exceptional Lie Groups* (University of Chicago Press, Chicago, 1996), for the generalized notion of triality and the dimensions $1, 2, 4, 8$.
- J. C. Baez, "The Octonions," *Bulletin of the American Mathematical Society* **39** (2002) 145–205 (arXiv:math.RA/0105155), for the triality of $\mathrm{Spin}(8)$ and the octonions, and for the Hurwitz theorem.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer Academic Publishers, Dordrecht, 1997), for the algebra of complexified quaternions and the left- and right-multiplication transformations $S_1(q), S_2(q)$.
- The companion corpus articles: [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html), [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) (for the non-integrable-phase interpretation of the mass and the unit vector $U_{\mathrm{vec},\mu}$), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) (for the covariant derivative $\tilde\nabla_\mu$ away from the neutral-element form), and [Triality and Spin(8) with Inner Conjugation](../articles_maths/triality-and-spin8-with-inner-conjugation.html) (for the eight-dimensional case the construction generalizes).
