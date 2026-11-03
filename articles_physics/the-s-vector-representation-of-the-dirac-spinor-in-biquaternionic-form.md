# __The s-Vector Representation of the Dirac Spinor in Biquaternionic Form__

## Introduction

Cartan observed that the spin group $\mathrm{Spin}(8)$ has three eight-dimensional real representations — the vector $8_v$ and the two half-spinors $8_s, 8_c$ — and that they are permuted by an outer automorphism of order three, the *triality* of $D_4$. The coincidence of the three dimensions is special to eight dimensions. Only $n = 8$ puts the vector space and the two semi-spinor spaces on an equal footing, and the associated composition law is the octonion product.

In four-dimensional Minkowski space the three spaces have dimensions four, four and four: a Lorentz vector, and the two four-real-component semi-spinors that a Dirac spinor decomposes into. Liu Yu-Fen asked whether the same coincidence can be exploited there, and constructed what he calls a *ding* construction: an order-three map $J$ on $\mathbb{M}^{1+3}\times S_1\times S_2$ built from a triple of neutral elements, under which the Dirac spinor becomes a complex four-vector. The composition law it defines is that of the algebra of complexified quaternions — the biquaternion algebra — so the *vector representation of the Dirac spinor* is the same thing as a biquaternionic representation of it. This article records that construction, its bosonic rewriting of the Dirac Lagrangian, and the self-dual form the massive Dirac equation takes in it.

The construction is a companion to the corpus's spinor-module articles. There, the Dirac field lives in a minimal left ideal of $\mathbb{B}$ and the Lorentz group acts on the left; here, a *different* linear representation of the same group — on a complex four-vector $G_\mu$ — carries the same field, and the two representations are related by fixed neutral elements. What is gained is a dictionary in which every Dirac bilinear becomes a bilinear in $G$ and its conjugate; what is paid is a preferred timelike direction, the neutral element $k_\mu$, which the dictionary needs and the metric does not supply.

The conventions are those of the companion articles and of *The Dirac Equation in Biquaternionic Form*: the algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_t = 1, \vec e_x, \vec e_y, \vec e_z$, the quaternion relations $\vec e_k^2 = -e_t$ and $\vec e_x\vec e_y = \vec e_z$ cyclically, and the central scalar imaginary $i$, with $i^2=-1$. The article is written in the **cell algebra**: a generator is the cell $C_\mu=iL_{a_\mu}R_{b_\mu}$, acting by $C_\mu\Psi=i a_\mu\Psi b_\mu$, and the gamma matrices are a frame of that algebra, displayed once in §The Gamma Formulation. The source's four-vector indices $\mu = 0,1,2,3$ are ordinary Minkowski indices with metric

$$
g_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1),
$$

which is the corpus's **generator metric**, the same object the four generators of the Dirac module obey; the source writes $\eta_{\mu\nu}$ for it. It is *not* the $ict'$ metric $\eta = \mathrm{diag}(-1,+1,+1,+1)$ of $\mathbb{M}_-$, which belongs to the gradient. Dot products are $V\cdot W = \sum_{\mu,\nu}V_\mu g_{\mu\nu}W_\nu = \sum_\mu\epsilon_\mu V_\mu W_\mu$. No index is raised in this article. Where the source wrote a contraction with one index up and one down and no metric between them, the sum here carries the sign vector $\epsilon=(1,-1,-1,-1)$, written $\sum_\mu\epsilon_\mu$; where $g_{\mu\nu}$ is written, it carries the signs itself and the sum is plain. The sign vector and the Levi-Civita symbol $\varepsilon_{\mu\nu\lambda\rho}$ are different letters.

## The Trinomial Unit Basis

### The Neutral Elements

Chevalley's name for the units of a spin representation is *neutral elements*. Liu's construction needs four of them: a timelike unit vector $k_\mu$, a spacelike unit vector $j_\mu$ orthogonal to it, and two unit semi-spinors $u_\alpha$ and $v_\alpha$. They are normalized so that

$$
k_\mu g_{\mu\nu}k_\nu = 1, \qquad j_\mu g_{\mu\nu}j_\nu = -1, \qquad k_\mu g_{\mu\nu}j_\nu = 0,
$$

and

$$
\bar u u = 1, \qquad \bar v v = -1, \qquad \bar u v = 0,
$$

where $\bar u = i(u^\dagger e_t)\vec e_x = u^\dagger C_0$ is the Dirac conjugate (left unit $e_t$, right unit $\vec e_x$). Write $a_0=e_t$, $a_k=\vec e_k$ for the units a four-vector index multiplies on the left, and $b_0=\vec e_x$, $b_k=\vec e_y$ for those it multiplies on the right. The **generator cell** of index $\mu$ is
$$
C_\mu := iL_{a_\mu}R_{b_\mu},
\qquad
C_\mu\Psi = i a_\mu\Psi b_\mu ,
$$
and the contraction of the four generators with the components $w_\mu$ is
$$
\mathcal{D}(w) := \sum_\mu w_\mu C_\mu .
$$
The reconstruction below needs the same contraction one factor of $i$ lower, on the real cell:
$$
\mathcal{R}(w) := \sum_\mu w_\mu\, iC_\mu = -\sum_\mu w_\mu\, L_{a_\mu}R_{b_\mu} .
$$

The vector and spinor units are tied together by

$$
\mathcal{D}(k)u = u, \qquad \mathcal{D}(k)v = -v, \qquad \mathcal{D}(j)u = i v, \qquad \mathcal{D}(j)v = i u .
$$

The two spinors are therefore the two eigenvectors of $\mathcal{D}(k)$ with eigenvalues $+1$ and $-1$. The spacelike neutral vector gives $\mathcal{D}(j)^2 = j\cdot j = -1$, so $\mathcal{D}(j)$ is a complex structure rather than an involution: its eigenvalues are $\pm i$, and it exchanges $u$ and $v$ only up to the factor $i$. This is a second place, after the definition of the cell, where $i^2=-1$ carries the sign. In the Dirac basis and the coordinate system

$$
u = (1,0,0,0)^{\mathsf T}, \quad v = (0,0,i,0)^{\mathsf T}, \quad k_\mu = (1,0,0,0), \quad j_\mu = (0,0,0,-1),
$$

all these relations hold. With $i^2=-1$ the two null spinors are real in this frame, $r=u+iv=(1,0,-1,0)^{\mathsf T}$ and $l=u-iv=(1,0,1,0)^{\mathsf T}$, which is the explicit form of the two pure spinors. The signs are the covariant ones: the contravariant $j$ is $(0,0,0,1)$, and $g_{\mu\nu}$ supplies the minus. The source writes $\mathcal{D}(j)v=u$ with a real $v$; in the frame above $v$ is purely imaginary and the same relation appears with the factor $i$, which is the convention the source leaves implicit. The two pure spinors are null, $\bar r r = \bar l l = 0$.

### The Null Basis

It is often convenient to pass to the null basis

$$
r = u + i v, \qquad l = u - i v, \qquad k_\pm{}_\mu = \tfrac12(k_\mu \pm j_\mu),
$$

for which

$$
\bar r l = \bar l r = 2, \qquad k_\pm{}_\mu g_{\mu\nu}k_\pm{}_\nu = 0, \qquad k_\pm{}_\mu g_{\mu\nu}k_\mp{}_\nu = \tfrac12,
$$

and

$$
\mathcal{D}(k)r = l, \qquad \mathcal{D}(k_+)r = 0, \qquad \mathcal{D}(k)l = r, \qquad \mathcal{D}(k_-)l = 0 .
$$

The names are the source's: $r$ is the right-handed and $l$ the left-handed *pure spinor* of the pair. The two null vectors $k_+$ and $k_-$ are the two null directions into which $k$ and $j$ resolve.

### The Two Semi-Spinors of a Dirac Spinor

Every Dirac spinor decomposes into two semi-spinors, each carrying four independent real components,

$$
\Psi = \Psi_1 + \Psi_2, \qquad \Psi_1 = \mathcal{R}(B^\flat)v, \qquad \Psi_2 = \mathcal{R}(N^\flat)u,
$$
where $B^\flat_\nu=\sum_\mu g_{\mu\nu}B_\mu$ and $N^\flat_\nu=\sum_\mu g_{\mu\nu}N_\mu$, with

$$
B_\mu = \tfrac12\bigl(\bar v\, iC_\mu\Psi - \bar\Psi\, iC_\mu v\bigr), \qquad
N_\mu = \tfrac12\bigl(\bar\Psi\, iC_\mu u - \bar u\, iC_\mu\Psi\bigr) .
$$

The projection uses $iC_\mu=-L_{a_\mu}R_{b_\mu}$, the real cell: with $C_\mu$ alone the coefficients would come out $i$ times real, and the product $i\cdot i=-1$ is exactly what makes them real. The two coefficients $B_\mu$ and $N_\mu$ are **real four-vectors**, and the reconstruction $\Psi \mapsto (B, N) \mapsto \Psi$ is exact. This is the first half of the statement that a Dirac spinor is a pair of real four-vectors.

## The Composition Law and the Normed Condition

### The Structure Constants

Two four-index tensors are read off the four generators. A product of generators multiplies its left units into one chain and its right units into another; with $\mathrm{Sc}$ the scalar part of a biquaternion, the trace of such a product is four times the product of the scalar parts of the two chains, so

$$
{t'}_{\mu\nu\lambda\rho} = \mathrm{Sc}(a_\mu a_\nu a_\lambda a_\rho)\,\mathrm{Sc}(b_\rho b_\lambda b_\nu b_\mu)
= g_{\mu\nu}g_{\lambda\rho} + g_{\mu\rho}g_{\nu\lambda} - g_{\mu\lambda}g_{\nu\rho},
$$

$$
\varepsilon_{\mu\nu\lambda\rho} = \mathrm{Sc}(e_t\,a_\mu a_\nu a_\lambda a_\rho)\,\mathrm{Sc}(b_\rho b_\lambda b_\nu b_\mu\,\vec e_z),
\qquad \varepsilon_{0123} = 1 .
$$

The first is symmetric under the interchange of its two index pairs; the second is the totally antisymmetric symbol. From them and the neutral vectors come the structure constants

$$
c_{\mu\nu\lambda} = \bigl({t'}_{\mu\nu\lambda\rho} - i\varepsilon_{\mu\nu\lambda\rho}\bigr)k_\rho,
\qquad
\check c_{\mu\nu\lambda} = \bigl({t'}_{\mu\nu\lambda\rho} - i\varepsilon_{\mu\nu\lambda\rho}\bigr)j_\rho .
$$

The two differ only in which neutral vector contracts the four-index symbol; $c$ is built on the timelike $k$, $\check c$ on the spacelike $j$. In $c_{\mu\lambda\nu}$ and $\check c_{\mu\lambda\nu}$ the slots are, in order, the left input, the output and the right input. The metric and $c_5{}_{\mu\nu}$ are symmetric, so their slot order carries no information; the totally antisymmetric $\varepsilon$ changes sign when two of its slots are exchanged, and its slot order is part of the statement.

### The Normed Condition

The bilinear composition

$$
(G \otimes H)_\lambda = \sum_{\mu,\nu}\epsilon_\mu\epsilon_\nu\, G_\mu\, c_{\mu\lambda\nu} H_\nu,
\qquad
(G \mathbin{\check\otimes} H)_\lambda = \sum_{\mu,\nu}\epsilon_\mu\epsilon_\nu\, G_\mu\, \check c_{\mu\lambda\nu} H_\nu
$$

satisfies the identity that Hurwitz's theorem makes possible only in dimensions $1, 2, 4, 8$:

$$
\boxed{\;\begin{aligned}
(G\cdot G)(H\cdot H) &= (G\otimes H)\cdot(G\otimes H),\\
(G\cdot G)(H\cdot H) &= -(G\mathbin{\check\otimes} H)\cdot(G\mathbin{\check\otimes} H).
\end{aligned}\;}
$$

The sign on the second line is the sign difference between the timelike and the spacelike neutral vector. Both identities are the statement that the composition preserves the quadratic form up to a fixed sign — the *normed condition* of the source, and the reason the construction lands on biquaternions rather than on some arbitrary algebra.

### The Algebra

The composition is associative and non-commutative, and $k$ is its two-sided unit:

$$
(G\otimes H)\otimes K = G\otimes(H\otimes K), \qquad \sum_{\mu,\lambda}\epsilon_\mu\epsilon_\lambda\, k_\mu c_{\mu\nu\lambda} G_\lambda = G_\nu .
$$

Its matrix realisation is obtained by writing $(e_\mu)_\nu{}_\lambda = c_{\nu\sigma}{}_\mu\, g_{\sigma\lambda}$. In the coordinate system above, $e_t = I$ and, with $e_\nu = i\,\vec u_{\nu}$ for $\nu = 1,2,3$,

$$
\boxed{\;\vec u_x\vec u_x = \vec u_y\vec u_y = \vec u_z\vec u_z = \vec u_x\vec u_y\vec u_z = -I,
\qquad \vec u_x\vec u_y = -\vec u_y\vec u_x = \vec u_z \ \ (\text{cyclic})\;}.
$$

These are the relations of the **matrix realisation**, not of the biquaternion units themselves. In that realisation $e_0=I$ and $e_k=i\vec u_k$, so $e_k^2=i^2\vec u_k^2=+I$ and $e_xe_y=i^2\vec u_x\vec u_y=-\vec u_z=i e_z$; the factor $i$, through $i^2=-1$, is what flips both signs. The neutral vector $k$ is hidden inside $c$: it is the unit element, the preferred time direction of the algebra.

## The Semi-Spinors as Real Four-Vectors

The two real four-vectors $B_\mu$ and $N_\mu$ are the *vector representation* of the two semi-spinors. The quadratic form of the spinor space reads

$$
\bar\Psi\Psi = -B_\mu g_{\mu\nu}B_\nu + N_\mu g_{\mu\nu}N_\nu,
$$

so the two vectors enter with opposite signs, and $\bar\Psi\Psi = N^2 - B^2$ is the difference of two norms. Neither sign is fixed by the spinor: in the rest frame $\Psi=(1,0,0,0)$ the vector $B$ is purely spatial and $N$ vanishes, while for $\Psi=(0,0,1,0)$ the vector $B$ is timelike. The labels *timelike* and *spacelike* that the source attaches to the two semi-spinors belong to its own metric convention; what is convention-free is the opposite sign with which the two enter $\bar\Psi\Psi$.

The complex vector $G_\mu = B_\mu + iN_\mu$ is the combined object, and its real and imaginary parts are the two semi-spinors. The chiral split of the spinor is a second, independent split, by the chirality cell:
$$
\Psi_R = \tfrac12\bigl(e_t+\Gamma\bigr)\Psi, \qquad \Psi_L = \tfrac12\bigl(e_t-\Gamma\bigr)\Psi, \qquad \Psi=\Psi_R+\Psi_L ,
$$
and the corresponding projections $R_\mu, L_\mu$ of $G_\mu$ are the subject of §The Chiral Pair. The source calls $G_\mu$ an **s-vector**, because it transforms under left multiplication $S_1(q)$ by a unit biquaternion, whereas an ordinary spacetime vector $x_\mu$ transforms under the mixed left–right map $\Lambda(q)$. Two different linear representations of the same $SL(2,\mathbb{C})$ act on the same four-dimensional index.

## The Bilinear Dictionary

### The Dictionary

The reward of the s-vector representation is that every Dirac bilinear becomes a bilinear in $G$ and $G^*$ with the structure constants $c$ and $\check c$, where $\Gamma:\Psi\mapsto-i e_t\Psi\vec e_z=-iR_{\vec e_z}\Psi$ is the chirality cell:

$$
\bar\Psi\Psi = -\tfrac12\sum_\nu\epsilon_\nu\bigl(G_\nu G_\nu + G^*_\nu G^{*}_{\nu}\bigr),
\qquad
\bar\Psi\Gamma\Psi = +\tfrac12\sum_\nu\epsilon_\nu\bigl(G_\nu G_\nu - G^*_\nu G^{*}_{\nu}\bigr),
$$

$$
\bar\Psi\, C_\mu\Psi = \sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\, G_\lambda\, c_{\lambda\mu\nu}\, G^*_\nu,
\qquad
\bar\Psi\,\Gamma C_\mu\Psi = \sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\, G_\lambda\, \check c_{\lambda\mu\nu}\, G^*_\nu .
$$
Here $\Gamma=-iL_{e_t}R_{\vec e_z}$ and $C_\mu=iL_{a_\mu}R_{b_\mu}$, so $\Gamma C_\mu=(-i)(i)L_{e_t}R_{\vec e_z}L_{a_\mu}R_{b_\mu}=L_{e_t}R_{\vec e_z}L_{a_\mu}R_{b_\mu}$: the two factors of $i$ cancel by $i^2=-1$, and the axial bilinear carries no explicit imaginary unit. The slot order is the one fixed above: the first slot of $c$ belongs to the left factor, here $G_\lambda$, the middle slot to the output index $\mu$, and the last slot to the right factor, here $G^*_\nu$. Because the two factors commute as complex numbers, the sum is unchanged if the two are exchanged together with the first and last slots; it is changed if only one of the two is moved. With the opposite attachment, $\sum\epsilon_\nu\epsilon_\lambda G^*_\nu\check c_{\nu\mu\lambda}G_\lambda$, the same sum appears with the opposite sign, and the two readings must not be mixed.

The charge current is $e\,\pi_\mu = e\sum_{\rho,\sigma}\epsilon_\rho\epsilon_\sigma\, G_\rho c_{\rho\mu\sigma}G^*_\sigma$, the source's first bilinear; the vector identity above is the same statement with $\mu$ renamed. The chirality cell is the ordered product of the four generator cells up to the factor $i$,
$$
\Gamma=-iL_{e_t}R_{\vec e_z},
$$
and it anticommutes with each $C_\mu$, so it separates the two chiral halves of every spinor. Its representative on the reference frame, written in §The Gamma Formulation, is the usual fifth gamma. The source further rewrites the mass form as

$$
\bar\Psi\Psi = \sum_\mu\epsilon_\mu\, K_\mu\,\bar\Psi\, C_\mu\Psi
$$

for a unit complex vector $K_\mu$ built from $\Psi$; that interpretation — the mass as a unit vector, hence as a non-integrable phase — is recorded in *The Dirac Equation in Biquaternionic Form*, and this article takes it as the entry into the same construction.

### The Cubicity of the Interaction

The vector-space, semi-spinor-1 and semi-spinor-2 labels are permuted by the order-three map

$$
J : \ A \mapsto B \mapsto N \mapsto A,
$$

which leaves the trilinear form

$$
A_\mu\bigl(\bar\Psi_{(1)}\, C_\mu\Psi_{(2)} + \bar\Psi_{(2)}\, C_\mu\Psi_{(1)}\bigr)
= 2\sum_{\nu,\lambda,\sigma}\epsilon_\nu\epsilon_\lambda\epsilon_\sigma\, A_\mu\, \varepsilon_{\lambda\mu\nu\sigma}N_\lambda B_\nu k_\sigma
$$

invariant. This is the *ding*: the fourth-dimensional analogue of Cartan's triality, with the biquaternion algebra in place of the octonions, and the vector, the timelike unit $k$ and the two semi-spinors playing the roles the three eight-dimensional spaces play in the $\mathrm{Spin}(8)$ case. Written with the first slot of the symbol on $B$ instead, $\varepsilon_{\nu\mu\lambda\sigma}B_\nu N_\lambda$, the same sum changes sign; the identity above is the version in which each symbol carries its factors in the order of its slots.

The fuller cubic form is linear in the vector $A$ and quadratic in the two semi-spinors. Its three-index symbols are the four-index ones contracted with $k$,
$$
{t'}_{\nu\mu\lambda}:={t'}_{\nu\mu\lambda\sigma}k_\sigma,
\qquad
\varepsilon_{\mu\lambda\nu}:=\varepsilon_{\mu\lambda\nu\sigma}k_\sigma,
$$
and the form is
$$
C = \sum_\mu A_\mu\,\bar\Psi\, C_\mu\Psi
= \sum_{\mu,\nu,\lambda}\epsilon_\nu\epsilon_\lambda\, A_\mu\, G_\lambda\, c_{\lambda\mu\nu}\, G^*_\nu .
$$
For real $A$ its real part is the source's cubic form,
$$
\mathrm{Re}\,C = \sum_{\mu,\nu,\lambda}\epsilon_\nu\epsilon_\lambda\, A_\mu\Bigl[{t'}_{\nu\mu\lambda}\bigl(B_\nu B_\lambda + N_\nu N_\lambda\bigr) + 2\varepsilon_{\mu\lambda\nu}B_\lambda N_\nu\Bigr],
$$
with the symmetric $t'$ pairing each semi-spinor with itself and the antisymmetric $\varepsilon$ pairing the two; the imaginary part is a second $t'$ contraction of $B$ and $N$, which the compact form keeps inside the single complex number $C$. The two together complete the dictionary of the three quadratic forms and the one cubic form that define the algebra.

## The Bosonic Form of the Dirac Lagrangian

Passing from the spinor to the s-vector representation turns the Dirac Lagrangian into

$$
\tfrac12\sum_\mu\epsilon_\mu\bigl[\bar\Psi\, C_\mu(\partial/\partial x_\mu - ieA_\mu)\Psi - \bigl((\partial/\partial x_\mu + ieA_\mu)\bar\Psi\bigr) C_\mu\Psi\bigr] - m\bar\Psi\Psi
$$

$$
= \tfrac12\Bigl[\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\bigl(\tilde\nabla_\mu G_\nu\bigr)^* i\check c_{\nu\mu\lambda} G_\lambda - \sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda G^*_\nu\, i\check c_{\nu\mu\lambda}\, \tilde\nabla_\mu G_\lambda + m\sum_\nu\epsilon_\nu\bigl(G^{*}_\nu G^{*}_{\nu} + G_\nu G_\nu\bigr)\Bigr],
$$

with the covariant derivative

$$
\tilde\nabla_\mu G_\lambda = \partial/\partial x_\mu G_\lambda - ieA_\mu\, g_{\lambda\rho}\, c_5{}_{\rho\sigma} G_\sigma .
$$

On the chiral projections the connection collapses to an ordinary phase, because $c_5{}_{\rho\sigma}R_\sigma=+R_\rho$ and $c_5{}_{\rho\sigma}L_\sigma=-L_\rho$:

$$
\tilde\nabla_\mu R_\lambda = \bigl(\partial/\partial x_\mu - ieA_\mu\bigr)R_\lambda,
\qquad
\tilde\nabla_\mu L_\lambda = \bigl(\partial/\partial x_\mu + ieA_\mu\bigr)L_\lambda .
$$

The opposite charges of the two halves are thus the two eigenvalues of $c_5$, and the gauge field couples to them with opposite signs, as a chiral gauge field must.

Both kinetic terms carry the same combination $i\check c$, and that product is not purely imaginary, because $\check c$ already contains an $i$. Since $\check c_{\mu\nu\lambda}=({t'}_{\mu\nu\lambda\rho}-i\varepsilon_{\mu\nu\lambda\rho})j_\rho$, the combination is
$$
i\check c_{\mu\nu\lambda}=\varepsilon_{\mu\nu\lambda\rho}j_\rho+i\,{t'}_{\mu\nu\lambda\rho}j_\rho,
$$
so the operator has a real $\varepsilon$ part and an imaginary $t'$ part. The two kinetic terms are not equal and not merely conjugate: writing $T_1$ for the first and $T_2$ for the second, conjugation exchanges them with a minus,
$$
T_2=-\overline{T_1},
$$
so the combination $T_1-T_2=T_1+\overline{T_1}$ is real. The minus comes from the antisymmetry of $\varepsilon$ under the exchange of the two slots it carries.

Two features are worth naming. The kinetic operator is not symmetric in $G$ and $G^*$: the two terms differ by a sign as well as by conjugation, and that is what makes their difference real. The mass term is $m(G^*G^* + GG)$, not $mG^*G$: the mass couples $G$ to $G^*$ rather than to itself, which is the shadow of the chirality-off-diagonal mass of the spinor formulation. The kinetic operator has the block structure of a Dirac operator in a four-vector carrier. The generator cells anticommute,
$$
C_\mu C_\nu + C_\nu C_\mu = 2g_{\mu\nu},
$$
so the operator $\sum_\mu\epsilon_\mu C_\mu\,\partial/\partial x_\mu$ squares to the d'Alembertian,
$$
\Bigl(\sum_\mu\epsilon_\mu C_\mu\,\partial/\partial x_\mu\Bigr)^2
= \tfrac12\sum_{\mu,\nu}\epsilon_\mu\epsilon_\nu\{C_\mu,C_\nu\}\,\partial_\mu\partial_\nu
= \sum_\mu\epsilon_\mu\,\partial_\mu^2 ,
$$
where $i^2=-1$ is used twice, once inside each cell. A solution of the massive equation therefore obeys
$$
\bigl(\partial\!\cdot\!\partial + m^2\bigr)G_\mu = 0 ,
$$
which is the sense in which the first-order system is a square root of the Klein–Gordon equation.

The bosonization is not canonical. It depends on the choice of the neutral elements $j_\mu$ and $k_\mu$: the Lagrangian is built from $\check c$, and $\check c$ is built from $j$. Any orthogonal pair with $k\cdot k = -j\cdot j = 1$ serves, they are arbitrary but must be fixed; the remaining symbols $c_{\mu\nu\lambda}$, $c_5{}_{\rho\sigma}$ and the rest are reconstructed once $j$ and $k$ are chosen.

## The Two Equations and the Self-Dual Form

### The Chiral Pair

The massive Dirac equation in the vector representation has **two chiral halves**, and the mass couples them. In the chiral split the equation reads two equations, not one:

$$
\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\, i(\partial/\partial x_\nu-ieA_\nu)R_\lambda - m\,L^{*}_{\mu}=0,
$$
$$
\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\, i(\partial/\partial x_\nu+ieA_\nu)L_\lambda - m\,R^{*}_{\mu}=0,
$$

where

$$
R_\mu = \tfrac12\bigl(\delta_{\mu\nu} + c_5{}_{\mu\nu}\bigr)G_\nu,
\qquad
L_\mu = \tfrac12\bigl(\delta_{\mu\nu} - c_5{}_{\mu\nu}\bigr)G_\nu
$$

are the two chiral biquaternions. The single complex equation

$$
i\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\,\tilde\nabla_\nu G_\lambda - m\, G^{*}_{\mu} = 0
$$

is the compact form of the same pair: the two equations above are its two chiral projections, and the two projectors sum to the identity. This is the spinor equation's two-sided structure, carried to the four-vector carrier. In the spinor carrier the same pair reads

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
\qquad
\tilde\nabla^\natural\tilde\Psi_L=m\tilde\Psi_R,
$$

with the mass cell $mL_{e_t}R_{e_t}=m e_t$ the identity in the algebra. Nothing in the mass term flips the chirality by itself; the term is off-diagonal only in the sense that the two equations are written as a pair, and each half is carried into the other by the mass. The s-vector pair and the spinor pair are the same two equations in two carriers.

Equivalently, with $A_\mu = 0$, the pair is the self-dual system

$$
\boxed{\;G_{\mu\nu} = \tfrac{i}{2}\,\varepsilon_{\mu\nu\lambda\rho} G_{\lambda\rho},
\qquad
\sum_\mu\epsilon_\mu\bigl(\partial/\partial x_\mu G_\mu - i m j_\mu G^{*}_{\mu}\bigr) = 0\;},
$$

where

$$
G_{\mu\nu} = \bigl(\partial/\partial x_\mu G_\nu + im\,j_\mu G^*_\nu\bigr) - \bigl(\partial/\partial x_\nu G_\mu + im\,j_\nu G^*_\mu\bigr).
$$

The first equation is a self-duality condition on the field strength $G_{\mu\nu}$, the second a divergence condition. The self-dual pair and the chiral pair are two ways of writing the same first-order system: one splits by the 2-form, the other by chirality. The mass enters the two boxed equations with opposite signs, and that relative sign is fixed: the self-duality is a consequence of the equation of motion, not an independent equation, and flipping both signs at once is the change of convention $G\leftrightarrow G^*$, $m\mapsto-m$ rather than a different system.

### The Chiral Biquaternions and the 2-Form

The two chiral biquaternions $R_\mu$ and $L_\mu$ defined in §The Chiral Pair are the projections of $G_\mu$ selected by the two eigenvalues of $c_5{}_{\mu\nu}$; the equation of motion is the pair displayed there. The two-form

$$
H_{\mu\nu} := \sum_\lambda\epsilon_\lambda\, G^*_\lambda\, \check c_{\lambda\mu\nu}
$$

is not antisymmetric. Its symmetric part is proportional to the metric, $H_{(\mu\nu)}=\phi\,g_{\mu\nu}$, with $\phi=\tfrac14 g_{\mu\nu}H_{\mu\nu}$, and its antisymmetric part is **anti-self-dual**,

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

The algebra supplies the chirality cell $c_5{}_{\mu\nu}$ with the defining property

$$
c_5{}_{\mu\rho} g_{\rho\sigma} c_5{}_{\sigma\nu} = g_{\mu\nu},
\qquad\text{i.e.}\qquad (c_5)^2 = 1 .
$$

In the neutral frame $k=(1,0,0,0)$, $j=(0,0,0,-1)$ the cell is the explicit matrix

$$
c_5{}_{\mu\nu} =
\begin{pmatrix} 0 & 0 & 0 & 1\\ 0 & 0 & i & 0\\ 0 & -i & 0 & 0\\ 1 & 0 & 0 & 0\end{pmatrix},
$$

which is Hermitian and squares to the identity, so its eigenvalues are $+1$ and $-1$ and the two projections are orthogonal. It mixes $G_0$ with $G_3$ and $G_1$ with $G_2$; it does not separate time from space, and the factor $i$ in its off-diagonal entries is what makes it an involution rather than a reflection.

The $\mathrm{U}(1)$ transformation of the spinor, $\Psi \mapsto \Psi \exp(i\alpha)$, becomes in the vector representation

$$
G_\mu \mapsto \bigl(\delta_{\mu\nu}\cos\alpha - i c_5{}_{\mu\nu}\sin\alpha\bigr)G_\nu = \bigl(\exp(-i\alpha c_5)\bigr)_{\mu\nu} G_\nu .
$$

This is a *chiral-type* transformation of $G$, and because $c_5^2 = 1$ it obeys the De Moivre theorem,

$$
\bigl(\cos\alpha - i c_5\sin\alpha\bigr)^n = \cos n\alpha - i c_5\sin n\alpha .
$$

The correspondence is exact, but it is not symmetric: the *chiral* transformation of the spinor, $\Psi \mapsto \exp(-ia\Gamma)\Psi$, becomes the *ordinary* $\mathrm{U}(1)$ transformation $G_\mu \mapsto \exp(ia)G_\mu$, and $\Psi\mapsto\exp(ia\Gamma)\Psi$ becomes $G_\mu\mapsto\exp(-ia)G_\mu$. The mass term $m\bar\Psi\Psi = -\tfrac{m}{2}(G^*G^* + GG)$ is invariant under the chiral-type transformation $G_\mu\mapsto(\delta_{\mu\nu}\cos a-i c_5{}_{\mu\nu}\sin a)G_\nu$ but *not* under the ordinary $\mathrm{U}(1)$ transformation $G_\mu\mapsto e^{ia}G_\mu$, so plane-wave solutions for $\Psi$ and for $G_\mu$ are rotated into one another by this exchange and must be distinguished.

## The Dual Transformation and the Two Semi-Spinors

The map

$$
B \mapsto N, \qquad N \mapsto -B, \qquad m \mapsto -m
$$

leaves the quadratic form $m\bar\Psi\Psi = m\sum_\nu\epsilon_\nu(N_\nu N_\nu - B_\nu B_\nu)$, the cubic form $\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda V_\mu B_\nu N_\lambda\varepsilon_{\nu\mu\lambda}$ and hence the Lagrangian and the equation of motion invariant. The source reads this as the statement that the semi-spinor of the first type is *dual* to the semi-spinor of the second type, on the model of the electromagnetic duality that exchanges $\vec E$ and $\vec H$ while exchanging $e$ and a magnetic coupling. It is the first-order shadow of the parent-action duality between the Dirac Lagrangian and the second-order topologically massive gauge Lagrangian, and it is the reason the two Lagrangians can describe the same propagating modes.

## What the Construction Does and Does Not Supply

**It supplies** a genuine, verified linear equivalence between the Dirac spinor and a complex four-vector, with the whole bilinear dictionary, a bosonic form of the Lagrangian, and a self-dual form of the massive equation. The central algebraic identities quoted above — the normed condition, associativity, the unit, the four-index traces $t'$ and $\varepsilon$, the reality of the two semi-spinor four-vectors, the recovery of $k$ and $j$ from $c$ and $\check c$, the mass, chiral and vector bilinears, the anti-self-duality of $H_{[\mu\nu]}$, and the trilinear form — were recomputed on the corpus's convention and hold. Where the source's printed sign differs, the difference is the slot order of $c$ and $\varepsilon$, not the identity; the De Moivre theorem follows from $(c_5)^2=1$.

**It does not supply** a Lorentz-covariant construction. The neutral elements $j_\mu$ and $k_\mu$ are *extra structure*: they are not determined by the metric, they are the two directions the construction singles out, and the algebra's unit is $k$. The source is explicit that this is a defect of the incomplete algorithm and, in the same breath, a virtue: the structure constants *do* return the neutral vectors by contraction,
$$
g_{\mu\nu}\,c_{\mu\nu\lambda}=4k_\lambda,
\qquad
g_{\mu\nu}\,\check c_{\mu\nu\lambda}=-4j_\lambda,
$$
so the preferred frame is not put in by hand in the final form, it is the algebra's own unit. But it is still a preferred frame, and a Lorentz transformation that moves $k$ is not a symmetry of the individual dictionary, only of the equivalence class of dictionaries. The source's own warning applies: the triality map $J$ is *not* a symmetry of the theory; it maps one description of the theory to another description of the same theory.

**It does not supply** any new physics. The construction is a re-encoding of the Dirac equation in a different linear representation of the same Lorentz group, and its predictions — the mass shell, the propagator, the cross sections — are those of the Dirac equation. What it changes is the *language*: the mass is a non-integrable phase, the next-to-topological density is a total derivative, and the photon–electron relation becomes a duality between a first-order and a second-order description. The physics is the same; the bookkeeping is different, and cleaner.

## Open Questions

1. **The preferred frame.** Is the neutral vector $k_\mu$ a genuine extra structure, or is it fixed by the algebra as the source claims? The corpus's *Algebra and Element Conventions* already distinguishes the algebra from the spacetime it is applied to; the question is whether $k$ is a fact about the algebra or a fact about the embedding.

2. **The relation to the corpus's spinor module.** In the corpus the Dirac field lives in a Peirce carrier of $\mathbb{B}$, a minimal left ideal; here it is a complex four-vector. Both are four-complex-dimensional and carry the same left action of $\mathbb{B}$, so as modules they are equivalent, and the neutral elements give the explicit intertwiner. What is not settled is which basis makes the dictionary readable: the equivalence of the modules does not by itself select the trinomial unit basis.

3. **The lattice consequence.** The source suggests, as "further speculation", that because the dualized Dirac equation is second order, and second-order Lagrangians have no fermion-doubling problem, the vector representation offers a route around the Nielsen–Ninomiya obstruction. The corpus's *Fermion Doubling and the Nielsen–Ninomiya Theorem* treats that obstruction as a lattice statement; whether the s-vector representation evades its hypotheses, or merely restates them in a different field variable, is open.

4. **The interaction with a preferred frame.** If $k_\mu$ is physical, the construction singles out a preferred direction in the vacuum. Does the resulting theory violate Lorentz invariance observably, or is $k$ a gauge artifact of the description? The source does not say.

5. **Extension beyond four dimensions.** The construction uses the Lorentzian four-dimensional signature essentially — the source notes that a biquaternion description would not work if the dimension and signature were different. What happens at the next triality dimension, eight, where the algebra is the octonions and the vector, semi-spinor and semi-spinor spaces coincide, is the Cartan case the corpus records in *Triality and Spin(8) with Inner Conjugation*.

These questions are open.

## The Gamma Formulation

The four gammas are the generator cells of the body, $\gamma_\mu=C_\mu$, and together they are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z}.
$$

Here $L_{a}R_{b}$ multiplies on the left by $a$ and on the right by $b$: $L_{a}R_{b}\Psi=a\Psi b$. A single product $L_aR_b$ is a pure tensor; the pure tensors form the cone of rank at most one, and a general element is a sum of at most four of them.

$\gamma_5$ is the reference-frame representative of the chirality cell: the ordered product $i\gamma_0\gamma_1\gamma_2\gamma_3$, which is $\Gamma=-iL_{e_t}R_{\vec e_z}$ written in the frame; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module. The symbol $\Gamma$ is not a gamma matrix: $\Gamma$ is the chirality cell in the algebra, and $\gamma_5$ is its representative on the reference frame. This is why no $\gamma$ symbol appears in the body of the article.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

## Summary

A Dirac spinor in four-dimensional Minkowski space decomposes into two semi-spinors, and each semi-spinor is a **real four-vector**: $\Psi_1 = \mathcal{R}(B^\flat)v$ and $\Psi_2 = \mathcal{R}(N^\flat)u$ with real $B_\mu, N_\mu$, where $B^\flat_\nu=\sum_\mu g_{\mu\nu}B_\mu$ and $N^\flat_\nu=\sum_\mu g_{\mu\nu}N_\mu$. The combined object $G_\mu = B_\mu + iN_\mu$ is an **s-vector**, and the map $\Psi \leftrightarrow G$ is a linear equivalence. It rests on a trinomial unit basis — a timelike unit vector $k_\mu$, a spacelike unit vector $j_\mu$, and two unit semi-spinors $u, v$ — the neutral elements of Chevalley. The composition law $c_{\mu\nu\lambda} = ({t'}_{\mu\nu\lambda\rho} - i\varepsilon_{\mu\nu\lambda\rho})k_\rho$ built from the four-index traces $t'$ and $\varepsilon$ is associative, has $k$ as its unit, and satisfies the normed condition $(G\cdot G)(H\cdot H) = (G\otimes H)\cdot(G\otimes H)$; its matrix realisation is the quaternion algebra with $e_0=I$ and $e_k=i\vec u_k$, so that $e_k^2=+I$ and $e_xe_y=i e_z$. The Dirac bilinears become $G$-$G^*$ bilinears with the structure constants $c$ and $\check c$, and the order-three map $A\mapsto B\mapsto N\mapsto A$ permutes the vector and the two semi-spinors while leaving the trilinear form invariant — the *ding* construction, the four-dimensional analogue of Cartan's triality, with the biquaternion algebra in place of the octonions.

The Dirac Lagrangian becomes bosonic: a quadratic kinetic term in $G$ with the $\check c$ structure constants, and a mass term $m(G^*G^* + GG)$ that couples $G$ to $G^*$ — the chirality-off-diagonal mass in another guise. The massive equation becomes the pair of §The Chiral Pair, or equivalently the self-dual pair $G_{\mu\nu} = \tfrac{i}{2}\varepsilon_{\mu\nu\lambda\rho}G_{\lambda\rho}$, $\partial/\partial x_\mu G_\mu - imj_\mu G^{*}_{\mu} = 0$, with the antisymmetric part of the two-form $H_{\mu\nu} = G^*_\lambda\check c_{\lambda\mu\nu}$ anti-self-dual. The $\mathrm{U}(1)$ transformation of the spinor becomes the chiral-type transformation $G \mapsto (\cos\alpha - ic_5\sin\alpha)G$ with $(c_5)^2 = 1$, so the De Moivre theorem holds; the chiral transformation of the spinor becomes an ordinary $\mathrm{U}(1)$ transformation of $G$. The dual map $B \mapsto N$, $N \mapsto -B$, $m \mapsto -m$ leaves the theory invariant.

What the construction supplies is a dictionary; what it does not supply is covariance or new physics. The neutral elements $k_\mu$ and $j_\mu$ are a preferred frame. They are not determined by the metric; the contractions $g_{\mu\nu}c_{\mu\nu\lambda}=4k_\lambda$ and $g_{\mu\nu}\check c_{\mu\nu\lambda}=-4j_\lambda$ return them from the structure constants, so the frame is the algebra's own, but it is still a frame, and the corpus records the question as open. The triality map is not a symmetry; it maps one description to another description of the same theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mu, \nu, \lambda, \rho$ | Ordinary Minkowski four-vector indices, $0,1,2,3$ |
| $g_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$ | Generator metric of the frame (the source's $\eta$); not the $ict'$ metric |
| $V\cdot W = \sum_{\mu,\nu}V_\mu g_{\mu\nu}W_\nu = \sum_\mu\epsilon_\mu V_\mu W_\mu$ | Minkowski dot product |
| $k_\mu, j_\mu$ | Timelike and spacelike unit neutral vectors, $k\cdot k = -j\cdot j = 1$, $k\cdot j = 0$ |
| $u, v$ | Unit semi-spinors, $\bar u u = 1$, $\bar v v = -1$, $\bar u v = 0$ |
| $r = u+iv$, $l = u-iv$ | Pure spinors, $\bar r l = \bar l r = 2$ |
| $k_\pm{}_\mu = \tfrac12(k_\mu\pm j_\mu)$ | Null vectors formed from the neutral pair |
| $e_t, \vec e_k$ | The algebra units, $e_t = 1$, $\vec e_k^2 = -e_t$ |
| $a_\mu, b_\mu$ | Left and right units of the index: $a_0 = e_t$, $a_k = \vec e_k$, $b_0 = \vec e_x$, $b_k = \vec e_y$ |
| $C_\mu = iL_{a_\mu}R_{b_\mu}$ | The generator cell of index $\mu$; $C_\mu\Psi=i a_\mu\Psi b_\mu$ |
| $\mathcal{D}(w) = \sum_\mu w_\mu C_\mu$ | Contraction of the four generator cells, as it appears in the bilinears |
| $\mathcal{R}(w) = \sum_\mu w_\mu\,iC_\mu=-\sum_\mu w_\mu L_{a_\mu}R_{b_\mu}$ | Contraction on the real cell, as it appears in the reconstruction |
| $\delta_{\mu\nu}$ | The identity in the four-index space; no index is raised anywhere |
| $\mathrm{Sc}$ | Scalar part of a biquaternion |
| ${t'}_{\mu\nu\lambda\rho} = \mathrm{Sc}(a_\mu a_\nu a_\lambda a_\rho)\mathrm{Sc}(b_\rho b_\lambda b_\nu b_\mu)$ | Symmetric four-index trace |
| $\varepsilon_{\mu\nu\lambda\rho} = \mathrm{Sc}(e_ta_\mu a_\nu a_\lambda a_\rho)\mathrm{Sc}(b_\rho b_\lambda b_\nu b_\mu\vec e_z)$ | Totally antisymmetric symbol, $\varepsilon_{0123}=1$ |
| $c_{\mu\nu\lambda} = ({t'}_{\mu\nu\lambda\rho}-i\varepsilon_{\mu\nu\lambda\rho})k_\rho$ | Structure constants built on $k$ |
| $\check c_{\mu\nu\lambda} = ({t'}_{\mu\nu\lambda\rho}-i\varepsilon_{\mu\nu\lambda\rho})j_\rho$ | Structure constants built on $j$ |
| $c_5{}_{\mu\nu} = -g_{\mu\mu}\check c_{\mu\nu\lambda}k_\lambda$ | The algebra's chirality cell; $(c_5)^2 = 1$ |
| $\Gamma:\Psi\mapsto-i e_t\Psi\vec e_z=-iR_{\vec e_z}\Psi$ | The chirality cell (not a gamma matrix) |
| $(G\otimes H)_\lambda = G_\mu c_{\mu\lambda\nu}H_\nu$ | Composition law |
| $B_\mu, N_\mu$ | Real four-vectors of the two semi-spinors |
| $G_\mu = B_\mu + iN_\mu$ | s-Vector (the vector representation of the Dirac spinor) |
| $\Psi_R, \Psi_L$ | Right- and left-handed halves of the spinor, $\Psi_{R,L}=\tfrac12(e_t\pm\Gamma)\Psi$ (the source's $R,L$) |
| $R_\mu, L_\mu$ | Chiral projections of the s-vector, $R_\mu=\tfrac12(\delta_{\mu\nu}+c_{5\mu\nu})G_\nu$, $L_\mu=\tfrac12(\delta_{\mu\nu}-c_{5\mu\nu})G_\nu$ |
| $\Psi_1, \Psi_2$ | The two semi-spinors |
| $G_{\mu\nu}$ | Field strength of the self-dual form |
| $H_{\mu\nu} = G^*_\lambda\check c_{\lambda\mu\nu}$ | Two-form; its antisymmetric part is anti-self-dual |
| $\phi = \tfrac14 g_{\mu\nu}H_{\mu\nu}$ | Complex scalar in $H_{(\mu\nu)}=\phi\,g_{\mu\nu}$, the trace part of $H$ |
| $A_\mu$ | Electromagnetic four-potential |

## Further Reading

- Liu Yu-Fen, "Triality, Biquaternion and Vector Representation of the Dirac Equation," arXiv:math-ph/0109008 (2001), for the trinomial unit basis and the neutral elements, the composition law $c_{\mu\nu\lambda}$ and the normed condition, the semi-spinor four-vectors $B_\mu, N_\mu$, the s-vector $G_\mu = B_\mu + iN_\mu$, the bilinear dictionary, the bosonic Dirac Lagrangian, the self-dual form of the massive equation, the $\mathrm{U}(1)$ transformation and the De Moivre theorem, and the dual map $B \leftrightarrow N$. The explicit matrices $\vec u_{\nu}$ are its equations (16)–(18).
- Liu Yu-Fen, "Triality and Dual Equivalence Between Dirac Field and Topologically Massive Gauge Field," arXiv:hep-th/0602275 (2006), for the restatement of the construction with the fuller cubic form, the braid-group "Dirac's game", the chiral biquaternions $R_\mu, L_\mu$, the anti-self-dual two-form $H_{\mu\nu}$, the chiral form of the equation of motion, and the parent-action duality carried in the companion article *Dual Equivalence of the Dirac and Topologically Massive Gauge Fields*.
- E. Cartan, *Leçons sur la théorie des spineurs* I, II (Hermann, Paris, 1938); English translation by R. Streater, *The Theory of Spinors* (Hermann, Paris, 1966), for the original triality of $\mathrm{Spin}(8)$.
- C. C. Chevalley, *The Algebraic Theory of Spinors* (Columbia University Press, New York, 1954), for the neutral elements of a spin representation.
- J. F. Adams, *Lectures on Exceptional Lie Groups* (University of Chicago Press, Chicago, 1996), for the generalized notion of triality and the dimensions $1, 2, 4, 8$.
- J. C. Baez, "The Octonions," *Bulletin of the American Mathematical Society* **39** (2002) 145–205 (arXiv:math.RA/0105155), for the triality of $\mathrm{Spin}(8)$ and the octonions, and for the Hurwitz theorem.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer Academic Publishers, Dordrecht, 1997), for the algebra of complexified quaternions and the left- and right-multiplication transformations $S_1(q), S_2(q)$.
- The companion corpus articles: [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html), [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) (for the non-integrable-phase interpretation of the mass and the unit vector $K_\mu$), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) (for the covariant derivative $\tilde\nabla_\mu$ away from the neutral-element form), and [Triality and Spin(8) with Inner Conjugation](../articles_maths/triality-and-spin8-with-inner-conjugation.html) (for the eight-dimensional case the construction generalizes).
