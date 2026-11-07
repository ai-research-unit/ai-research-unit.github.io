# __Dual Equivalence of the Dirac and Topologically Massive Gauge Fields__

## Introduction

A massive spin-1 field can acquire its mass in more than one way. The **Proca** mass is second order and scalar: a term $\mu^2 A_\mu A^\mu$ in the Lagrangian and a Klein–Gordon factor in the propagator. A **topological** mass is first order: a term with one derivative, one power of the mass, and a Levi-Civita symbol, which in $2+1$ dimensions is the Chern–Simons term of Deser, Jackiw and Templeton.

Liu Yu-Fen's claim is a duality of the second kind. The **Dirac** Lagrangian in the vector representation is first order in the derivative and carries its mass as a term that couples the field to its conjugate. A first-order **parent action** in the same variables has two reductions: eliminating the auxiliary potential gives back the Dirac Lagrangian, and eliminating the Dirac field gives a second-order Lagrangian whose mass term is first order, one derivative and one power of $m$. In four dimensions that mass term is the cubic form; on the three-dimensional spin manifold, once the embedding vector $j$ is used to slice the space, it is exactly the Maxwell plus Chern–Simons Lagrangian of the topologically massive gauge field. The two reductions describe the same propagating modes, at least classically.

The article records the two parent actions and their four eliminations, and separates what is verified from what is quoted. It is the physics companion of *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form* and of *Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form*: the parent action is written in the s-vector variables, and its two reductions pass through the self-dual field strength and the cubic (order-three ding) form of those articles.

**The display.** No array is printed in this article. Every operator is written as an action on an element, $\tilde{Ξ}_{\mathrm{sp}}\mapsto a\tilde{Ξ}_{\mathrm{sp}} b$, and the one object the source prints as a $4\times4$ array, the chirality on the four-vector carrier, is written as the contraction of structure constants that carries it. The reason is the one argued in *Why AXF Matrices instead of Pauli and Gamma Matrices*: an array is one representative of an operator in one basis, it writes that basis into the page without naming it, and the product, the trace, the determinant and the spectrum are those of the action and survive the change of representative. The field is an element of $\mathbb{B}$, its two parts are labelled by the two values of its subscript, $L$ and $R$, and the index space below carries the source's four-vectors with the sign vector it declares. The third pass of that article keeps the axis-free array where an array is the object of the sentence; no sentence here is about an array, so nothing is kept.

**The frame.** Four-vector indices $\mu=0,1,2,3$ carry the generators of the Dirac module, and the index space carries the unit metric
$$
\delta_{\mu\nu}=(1,1,1,1).
$$
Every contraction carries the plain weight, $V\cdot W=\sum_\mu\epsilon_\mu V_\mu W_\mu$, with the sign vector $\epsilon=(1,-1,-1,-1)$ used in every sum below. The weight is read from the multiplication, $\mathrm{Sc}(e_\mu e_\nu)=\epsilon_\mu\delta_{\mu\nu}$: its three minuses are the squares of the spatial units, $\vec e_k^2=-e_t$, and its one plus is the square of $e_t$. The four generators of the next paragraph obey $\{iC_\mu,iC_\nu\}=2\epsilon_\mu\delta_{\mu\nu}$ with no sum on $\mu$, so the weight sits inside the generator. The one minus of $\Box$ on the material coordinate has a different origin, the square of the $i$ in $Q_t=i r'_t$. Every index the source raises is carried by an $\epsilon$ in the sums below. The Levi-Civita symbol $\varepsilon_{\mu\nu\lambda\rho}$ is totally antisymmetric with $\varepsilon_{0123}=1$; it is a different letter from $\epsilon$. Two neutral vectors are fixed by the structure constants, the timelike $k_\mu$ of $c_{\mu\nu\lambda}=(t'_{\mu\nu\lambda\rho}-i\varepsilon_{\mu\nu\lambda\rho})k_\rho$ and the spacelike $j_\mu$ of $\check c_{\mu\nu\lambda}=(t'_{\mu\nu\lambda\rho}-i\varepsilon_{\mu\nu\lambda\rho})j_\rho$, with $k\cdot k=-j\cdot j=1$ and $k\cdot j=0$. The source's point is that they are offshoots of the algebra and not extra structure. The projectors are
$$
p^+_{\mu\nu}=\epsilon_\mu\delta_{\mu\nu}+j_\mu j_\nu,\qquad p^-_{\mu\nu}=-j_\mu j_\nu,\qquad p^+_{\mu\nu}+p^-_{\mu\nu}=\epsilon_\mu\delta_{\mu\nu},
$$
with no sum on $\mu$, the two projecting onto the slice orthogonal to $j$ and onto $j$ itself, since $j\cdot j=-1$. Any four-vector splits as $G_\mu=G^\mu-j_\mu\xi$, with three-dimensional part $G^\mu=p^+_{\mu\nu}G_\nu$ and complex scalar $\xi=G_\mu j^\mu$. The superscript on $G^\mu$ is a **label for the transverse part**, not a raised index: every index in this article is a lower index, and a sum over it carries its $\epsilon$.

**The generators.** Every operator below is a map of the algebra to itself, and each is written as an action with its side in the display. The generator of index $\mu$ is the map
$$
C_\mu:\;\tilde{Ξ}_{\mathrm{sp}}\longmapsto a_\mu\tilde{Ξ}_{\mathrm{sp}} b_\mu,\qquad a_0=e_t,\quad a_k=\vec e_k,\qquad b_0=\vec e_x,\quad b_k=\vec e_y ,
$$
so that $C_0:\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}}\vec e_x$ acts on the right alone — its left factor is $e_t$, the identity of the algebra — while $C_1,C_2,C_3$ act on both sides. The four obey $\{iC_\mu,iC_\nu\}=2\epsilon_\mu\delta_{\mu\nu}$ as operators, with no sum on $\mu$: the weight sits inside the generator, and it is what the sums below carry. The operator that carries the split is $-iR_{\vec e_z}$, a pure right multiplier and therefore an example of the right slot, and it acts by right multiplication,
$$
\Gamma:\;\tilde{Ξ}_{\mathrm{sp}}\longmapsto-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z=\tilde{Ξ}_{\mathrm{sp}}\,(i\omega),\qquad \omega=-\vec e_z,\qquad \Gamma^2=\mathrm{id},\qquad \Gamma\,iC_\mu=-iC_\mu\,\Gamma,\qquad \Gamma=i\,(C_0C_1C_2C_3) .
$$
The product is the phase $i$ times a product of four generators, and it collapses to that one right action: $C_0$ is a right action already, and the left factors of $C_1C_2C_3$ cancel in pairs, so $C_1C_2C_3:\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}}\vec e_y$ and $C_0C_1C_2C_3:\tilde{Ξ}_{\mathrm{sp}}\mapsto-\tilde{Ξ}_{\mathrm{sp}}\vec e_z$, which is the chirality up to that phase. The letter $i$ of the source's chirality displays is the pseudoscalar $\omega=-\vec e_z$, with $\omega^2=-e_t$: it does not commute with the spatial units, and the source applies it on the right, $\tilde{Ξ}_{\mathrm{sp}}\mapsto-\tilde{Ξ}_{\mathrm{sp}}\vec e_z$. The corpus keeps $\omega$ for that element and the central $i$ free, and writes the chirality multiplier as $i\omega=-i\vec e_z$. The left multiplication $\tilde{Ξ}_{\mathrm{sp}}\mapsto-\vec e_z\tilde{Ξ}_{\mathrm{sp}}$ is a different map, and it is not the one meant: the two do not agree, so the side belongs to the definition.

**The gradient.** The derivative is the biquaternionic gradient of *Operator and Calculus Conventions*:
$$
\tilde\nabla=e_t\frac{\partial}{\partial R_t}+\vec e_x\frac{\partial}{\partial R_x}+\vec e_y\frac{\partial}{\partial R_y}+\vec e_z\frac{\partial}{\partial R_z},
\qquad
\tilde\nabla^{\natural}=e_t\frac{\partial}{\partial R_t}-\vec e_x\frac{\partial}{\partial R_x}-\vec e_y\frac{\partial}{\partial R_y}-\vec e_z\frac{\partial}{\partial R_z},
$$
On the material sector the substitution is $Q_t=i r'_t$ and $Q_k=x_k$, so $\partial/\partial R_t=\partial/\partial i r'_t$. Its norm is the d'Alembertian $\Box$ of that article,
$$
\Box=\Delta-\frac{\partial^2}{\partial {r'_{t}}^2},
$$
with the one minus the square of the $i$.
The gradient acts on the left. The free equation is first order in one field, $\tilde\nabla\tilde F=0$. The massive equation is not a one-field equation, because $\tilde\nabla^2$ is not scalar: the time unit $e_t$ is central and commutes with the three spatial units, so the time–space cross terms add instead of cancelling,
$$
\tilde\nabla^2=e_t\Bigl(\frac{\partial^2}{\partial R_t^2}-\Delta_Q\Bigr)+2\sum_k\vec e_k\frac{\partial^2}{\partial R_t\partial R_k},
$$
and the mixed term is a vector. The operator $\Box$ has no such term because $\tilde\nabla^{\natural}$ carries the spatial signs reversed, and that is why the d'Alembertian is the norm and not the square. The massive equation is the chiral pair of §*The Two Dirac Equations*, $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$, and this article writes no other first-order massive equation of one field. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

## The Parent Action

### The Fields

$G_\mu$ is the Dirac field in the vector representation, the **s-vector**: a complex four-vector with the bilinears of the companion article,
$$
\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iC_0\tilde{Ξ}_{\mathrm{sp}}=-\tfrac12\sum_\nu\epsilon_\nu\bigl(G_\nu G_\nu+G^*_\nu G^*_\nu\bigr),\qquad
\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iC_0\,iC_\mu\tilde{Ξ}_{\mathrm{sp}}=\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,G_\lambda\,c_{\lambda\mu\nu}\,G^*_\nu,
\qquad
\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iC_0\,\Gamma\,iC_\mu\tilde{Ξ}_{\mathrm{sp}}=\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,G_\lambda\,\check c_{\lambda\mu\nu}\,G^*_\nu,
$$
with $\tilde{Ξ}_{\mathrm{sp}}$ the Dirac field, an element of $\mathbb{B}$, $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$ its conjugation and $iC_0$ the timelike generator, so that $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iC_0$ is the Dirac adjoint. The three identities sit in the companion's slot order — $G$ in the first slot, $G^*$ in the last — and the axial one because $\Gamma\,iC_\mu$ is $C_\mu$ followed by right multiplication by $\vec e_z$: the $-i$ of the chirality cancels the $i$ of the generator, one factor of $i$ spent on $i^2=-1$.

The opposite attachment, $\sum\epsilon\epsilon\,G^*_\nu\check c_{\nu\mu\lambda}G_\lambda$, is a different sum, and the difference is exact — verified:
$$
\check c_{\nu\mu\lambda}-\check c_{\lambda\mu\nu}=-2i\,\varepsilon_{\nu\mu\lambda\rho}\,j_\rho ,
$$
because $r'_t$ is symmetric under the exchange of the first and third slots while $\varepsilon$ is antisymmetric. The two readings must not be mixed, and the exchange isolates precisely the antisymmetric part of the structure constants — the part that survives against the field strength in §*Why the Mass Is Topological*. The Dirac Lagrangian quoted below keeps the source's own order, $\check c_{\nu\mu\lambda}$ with the starred derivative in the first slot, which is also the order of the companion's Lagrangian.

$H_\mu$ is the dual potential: a complex four-vector, the auxiliary field of the four-dimensional parent action. In the three-dimensional version the auxiliary field is the complex potential $B_\mu$ in the axial gauge $B_\mu j^\mu=0$, and the complex scalar $\xi$ is a spectator carried through both reductions unchanged.

$A_\mu$ is the electromagnetic potential, and it enters only through the covariant derivative
$$
\tilde\nabla_\mu G_\lambda=\frac{\partial G_\lambda}{\partial x_\mu}+ieA_\mu\,\epsilon_\lambda\sum_{\sigma,\nu}\epsilon_\sigma\,\check c_{\lambda\sigma\nu}k_\nu G_\sigma .
$$
The second term is the chirality of the four-vector carrier, and it is written as the contraction of structure constants on the neutral vector $k$ that it is. The source prints the same object as a $4\times4$ array $c_5{}_{\mu\nu}$, one representative of the chirality, with $c_5{}_{\mu\nu}=-\epsilon_\mu\check c_{\mu\nu\lambda}k_\lambda$ and no sum on $\mu$; the array obeys $(c_5)^2=1$ and is $\epsilon$-antisymmetric, so the chirality of the carrier takes its two values on the two chiral parts of $G$. The contraction puts $k$ on the page, where the representative had absorbed it. The derivative that the auxiliary field uses is the same object with the constant $a$ added in the manner of a second coupling, $\tilde\nabla^{a}_\mu B_\nu=\partial/\partial x_\mu B_\nu+ia\,j_\mu B^*_\nu$, the second term conjugating the field, so that
$$
\tilde\nabla^{a}_\mu B_\nu-\tilde\nabla^{a}_\nu B_\mu=\partial/\partial x_\mu B_\nu-\partial/\partial x_\nu B_\mu+ia\,j_\mu B^*_\nu-ia\,j_\nu B^*_\mu=F_{\mu\nu},
$$
which is the source's field strength: it reduces to the Maxwell tensor at $a=0$ and is invariant under the generalized gauge transformation $B_\mu\mapsto B_\mu+p^+_{\mu\nu}\partial/\partial x_\nu\Theta$. The constant $a$ is real and differs from $m$; it survives in the reductions as the combination $m-a$ and is set to zero in the three-dimensional case.

### The Four-Dimensional Parent Action

The parent action is linear in the auxiliary field and quadratic in the Dirac field,
$$
S_{GH}=\int\Bigl[\bigl(G_\nu+\tfrac12 H_\nu\bigr)^*i\check c_{\nu\mu\lambda}\tilde\nabla^{ea}_\mu H_\lambda-\bigl(\tilde\nabla^{ea}_\mu H_\nu\bigr)^*i\check c_{\nu\mu\lambda}\bigl(G_\lambda+\tfrac12 H_\lambda\bigr)+\tfrac{m-a}{2}\bigl(G\cdot G+G^*\cdot G^*\bigr)+\partial Z_0^\mu/\partial x_\mu\Bigr],
$$
with $\tilde\nabla^{ea}$ the derivative above carrying both insertions, the electromagnetic and the $a$-term. The *same* $\check c$ contracts the Dirac field, the auxiliary field and the derivative in both halves: the two eliminations are two ways of inverting one linear system, and the coupling constants $e$ and $a$ sit in the derivative while the mass $m$ sits in the quadratic terms. $Z_0^\mu$ is a surface term, chosen so that the total divergence produced by the elimination vanishes.

### The Two Eliminations

**Eliminating the auxiliary field.** Varying $H_\mu$ gives
$$
\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\tilde\nabla^{ea}_\nu G_\lambda=-\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\tilde\nabla^{ea}_\nu H_\lambda ,
$$
and substituting this back leaves the **Dirac Lagrangian** in the vector representation,
$$
\boxed{\;\mathcal{L}_D=\tfrac12\Bigl[\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\Bigl(\bigl(\tilde\nabla_\mu G_\nu\bigr)^*i\check c_{\nu\mu\lambda}G_\lambda-G^*_\nu\,i\check c_{\nu\mu\lambda}\,\tilde\nabla_\mu G_\lambda\Bigr)+m\sum_\nu\epsilon_\nu\bigl(G^*_\nu G^*_\nu+G_\nu G_\nu\bigr)\Bigr]\;}
$$
up to the total divergence that $Z_0$ removes. The mass couples $G$ to $G^*$: it couples the two chiral parts of the field, and that is why the s-vector is not a pair of independent complex vectors. For $G=B+iN$ one has $G^2+G^{*2}=2(B^2-N^2)$ by $i^2=-1$, so the same term is the real bilinear $m\sum_\nu\epsilon_\nu(N_\nu N_\nu-B_\nu B_\nu)$.

The source does not solve the varied equation for $H_\mu$, and says so: the equation couples $H$ to its conjugate through the $a$-term, and the source calls the solution non-trivial and does not attempt it. What the source uses is the equation itself, which is enough to eliminate $H$ from the action and to display the Dirac Lagrangian. The elimination is therefore explicit in form and unperformed in practice, and the Dirac Lagrangian that comes out is the source's Eq. (57).

**Eliminating the Dirac field.** Varying $G_\nu$ gives the linear relation
$$
(m-a)G_\lambda=\sum_{\mu,\nu}\epsilon_\mu\epsilon_\nu\bigl(\tilde\nabla^{ea}_\mu H_\nu\bigr)^*i\check c_{\nu\mu\lambda},
$$
and substituting it back leaves a **second-order Lagrangian** for $H_\mu$ (sums over repeated indices, one $\epsilon$ per index),
$$
\mathcal{L}_H=\tfrac{1}{2(m-a)}\sum_{\mu,\nu,\lambda,\rho,\delta}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\epsilon_\rho\epsilon_\delta\bigl(\check c_{\nu\mu\lambda}\tilde\nabla^{ea}_\mu H_\lambda\bigr)\bigl(\check c_{\nu\rho\delta}\tilde\nabla^{ea}_\rho H_\delta\bigr)+\tfrac12\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda H^*_\nu\,i\check c_{\nu\mu\lambda}\tilde\nabla^{ea}_\mu H_\lambda+\text{c.c.}+\partial Z_0^\mu/\partial x_\mu ,
$$
The first term is quadratic in the derivative and is the kinetic term; the second carries one derivative and no mass, and it is the **cubic (order-three) form** of the companion article. At $a=e=0$, and after the rescaling $H_\mu\mapsto bH_\mu$ that restores canonical normalisation, it reads
$$
\mathcal{L}_H=-\frac{b^{2}}{2\,m}\Bigl[\sum_{\mu,\nu}\epsilon_\mu\epsilon_\nu\,\partial  H_\nu/\partial x_\mu\,\partial H_\nu/\partial x_\mu-m\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\,H^*_\nu\,i\check c_{\nu\mu\lambda}\,\partial  H_\lambda/\partial x_\mu\Bigr]+\text{c.c.}+\partial\text{-terms},
$$
so the mass term has one derivative and one power of $m$ — the hallmark of a topological mass, and the reason the source calls the two actions dual.

### The Three-Dimensional Parent Action and the Topological Mass

The three-dimensional version separates the scalar first. The duality is taken between the pairs $(G^\mu;\xi)$ and $(B^\mu;\xi)$ with the *same* $\xi$, and the parent action is
$$
S_{G\xi B}=\int\Bigl[\tfrac12\bigl(G^*_\nu+\tfrac12 B^*_\nu\bigr)i\check c_{\nu\mu\lambda}F_{\mu\lambda}+\tfrac{i}{2}\sum_\mu\epsilon_\mu\Bigl(G_\mu\frac{\partial\xi^*}{\partial x_\mu}-\xi^*\frac{\partial G_\mu}{\partial x_\mu}\Bigr)+\tfrac{m-a}{2}G\cdot G+\tfrac{i}{2}\xi^*j\cdot\tilde\nabla^{-a}\xi+\text{c.c.}+\partial Z_1^\mu/\partial x_\mu\Bigr].
$$
Varying $B_\mu$ gives
$$
\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\bigl(\tilde\nabla^{a}_\nu G_\lambda-\tilde\nabla^{a}_\lambda G_\nu\bigr)=-\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}F_{\nu\lambda},
$$
and substituting back returns the Dirac Lagrangian, now with $A_\mu=0$ and $G_\mu=G^\mu-j_\mu\xi$. Varying $G_\nu$ gives
$$
(m-a)G^\mu=\tfrac{i}{2}F_{\lambda\nu}\check c^{*\nu\lambda\mu}-i\,p^{\mu\nu}_+\partial\xi^*/\partial x_\nu ,
$$
and substituting this back leaves
$$
\begin{aligned}
\mathcal{L}_{\xi B}=\;&\tfrac{1}{8(m-a)}\sum_{\nu,\mu,\lambda,\rho,\delta}\epsilon_\nu\epsilon_\mu\epsilon_\lambda\epsilon_\rho\epsilon_\delta\bigl(\check c_{\nu\mu\lambda}F_{\mu\lambda}\bigr)\bigl(\check c_{\nu\rho\delta}F_{\rho\delta}\bigr)+\tfrac14\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda B^*_\nu\,i\check c_{\nu\mu\lambda}F_{\mu\lambda}\\
&-\tfrac{1}{2(m-a)}\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\bigl(\partial\xi/\partial x_\mu\bigr)\check c_{\mu\nu\lambda}F_{\nu\lambda}+\text{(scalar sector)}+\text{c.c.}+\partial Z_2^\mu/\partial x_\mu .
\end{aligned}
$$
The abbreviation *scalar sector* stands for the source's two terms in $\xi$ alone, $\tfrac{1}{2(m-a)}\partial\xi/\partial x_\mu\,p^{\mu\nu}_+\partial\xi^*/\partial x_\nu$ and $\tfrac i2\xi^*j^\mu\tilde\nabla^{-a}_\mu\xi$, which the elimination carries through unchanged; the potential $B$ is in the axial gauge $B_\nu j^\nu=0$. On the spin manifold, where the fields depend on the three coordinates of the slice orthogonal to $j$ and $j^\nu\partial B_\mu/\partial x_\nu=j^\nu\partial\xi/\partial x_\nu=0$, and at $a=0$, the two mixing terms — the $B^*\check cF$ term at the end of the first line and the $(\partial\xi)\check cF$ term that opens the second — combine into a surface term, and the Lagrangian reduces to
$$
\boxed{\;\mathcal{L}_G=-\tfrac{1}{4m}\sum_{\mu,\lambda}\epsilon_\mu\epsilon_\lambda F_{\mu\lambda}F_{\mu\lambda}+\tfrac14\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\,\check\varepsilon_{\nu\mu\lambda}\,B^*_\nu F_{\mu\lambda}+\text{(scalar sector)}+\text{c.c.}\;}
$$
with
$$
\check\varepsilon_{\nu\mu\lambda}=\sum_\rho\varepsilon_{\nu\mu\lambda\rho}\,j_\rho
$$
the Levi-Civita symbol of the slice, nonzero only when all three indices lie on it. This is Maxwell plus a **Chern–Simons mass**: first order in the derivative, one power of the mass, one Levi-Civita symbol. The gauge equation is the topologically massive one,
$$
\sum_\nu\epsilon_\nu\,\partial/\partial x_\nu F_{\nu\mu}+\tfrac m2\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check\varepsilon_{\mu\nu\lambda}F^*_{\nu\lambda}=0,
$$
and the scalar obeys its own massive equation, decoupled from $B$.

The overall normalisation is the source's: the kinetic term carries $1/m$, so the mass appears in the denominator of the Maxwell term and in the numerator of the Chern–Simons term. Rescaling $F$ or $B$ moves the $m$ to one side or the other, and the invariant statement is the ratio.

**Quoted, recomputed, and open.** The two parent actions, the four varied equations and the four Lagrangians are the source's, Eqs. (55)–(61), (71), (77)–(81) and (88). This pass recomputed the algebra those expressions use — the anticommutation relations of the four generators, the cancellation of the two factors of $i$ in $\Gamma\,iC_\mu$, the split $i\check c=\varepsilon j+i\,t'j$, the anti-self-duality of $H_{[\mu\nu]}$ and its complex rank three, the trace $H_{(\mu\nu)}=-\xi^*\epsilon_\mu\delta_{\mu\nu}$ with no sum on $\mu$, the reconstruction $G^*_\mu=\sum_\nu\epsilon_\nu H_{\mu\nu}j_\nu$, the total antisymmetry of $\check\varepsilon_{\nu\mu\lambda}$, the symmetries of $r'_t$ and the exact condition under which it vanishes against an antisymmetric pair, the exchange identity $\check c_{\nu\mu\lambda}-\check c_{\lambda\mu\nu}=-2i\varepsilon_{\nu\mu\lambda\rho}j_\rho$ — and not the eliminations themselves, which are a variational computation on the source's field content. One claim was tested and did not reproduce: the normalisation $U_{\\mathrm{vec}}\\cdot U_{\\mathrm{vec}}=1$ of Eq. (93), with the corpus's weights, so it is carried as the source's own.

## Why the Mass Is Topological

Two properties make the first-order mass term topological rather than a mass put in by hand.

**The Lagrangian is not invariant, but the equations are.** The dual potential carries the gauge freedom
$$
\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\nu\mu\lambda}\partial/\partial x_\nu\bigl(\delta H_\lambda\bigr)=0 ,
$$
for which the equations of motion are unchanged while the mass term changes by a total derivative only. The mass term is therefore not invariant under the gauge transformation, and the theory is nonetheless gauge covariant: the invariance sits in the equations and not in the Lagrangian, which is the definition of a topological term. In the three-dimensional case the transformation is the explicit one,
$$
B_\mu\mapsto B_\mu+p^+_{\mu\nu}\,\partial/\partial x_\nu\Theta ,
$$
with $\Theta$ a function on the spin manifold; the Levi-Civita part of $\check c$ dies against the symmetric second derivative and the $r'_t$ part gives $j_\nu$ times the $\epsilon$-contracted one,
$$
\check c_{\nu\mu\lambda}\frac{\partial^2\Theta}{\partial x_\mu\partial x_\lambda}=\epsilon_\nu j_\nu\sum_\mu\epsilon_\mu\frac{\partial^2\Theta}{\partial x_\mu^2},
$$
so the only component that survives is the one along $j$, and the condition is the wave equation.

**There is no Bianchi identity.** The structure constants $\check c$ contain the antisymmetric (Lie) and the symmetric (Jordan) parts, so the two-form built from the potential is not the curl of anything with an automatic closure: the object the duality exchanges is the self-dual tensor of §*The Self-Dual Field Strength*, not an antisymmetric field strength. The source's reason for the construction is stated as the definition of a potential without a Bianchi identity: of the Maxwell-like pair that the Dirac current satisfies, the second plays the role of a Bianchi identity only for one choice of the two phase parameters $\xi_1,\xi_2$ the source introduces, namely $\xi_1+\xi_2=0$, and it is precisely that choice which the dual potential is meant to avoid.

**Which part of $\check c$ survives.** The tensor in $\check c$ is
$$
t'_{\lambda\mu\nu\rho}=\epsilon_\lambda\epsilon_\nu\,\delta_{\lambda\mu}\delta_{\nu\rho}+\epsilon_\lambda\epsilon_\mu\,\delta_{\lambda\rho}\delta_{\mu\nu}-\epsilon_\lambda\epsilon_\mu\,\delta_{\lambda\nu}\delta_{\mu\rho},
$$
where each term pairs two slots with $\delta$ and carries the weight of one slot from each pair. Its symmetries are not the naive ones. It is symmetric under $\lambda\leftrightarrow\nu$ — the first and third slots — and under $\mu\leftrightarrow\rho$, the second and fourth, and under the exchange of the two pairs $(\lambda\mu)\leftrightarrow(\nu\rho)$; it is **not** symmetric under $\lambda\leftrightarrow\mu$ or under $\mu\leftrightarrow\nu$, so a contraction with an antisymmetric tensor kills it only when the antisymmetric pair is the first and the third slot — verified, and verified to fail for every other pair.

This matters for reading the reduction correctly. A sum $\sum_{\lambda,\nu}t'_{\lambda\mu\nu\rho}X_{\lambda\nu}$ with $X$ antisymmetric vanishes, so the $r'_t$ part is invisible to a field strength contracted on the first and third slots; but the source's reduced mass term, Eq. (88), contracts the second and third slots, $\check c_{\nu\mu\lambda}F_{\mu\lambda}$, where $r'_t$ does **not** drop out — checked. The source's spin-manifold Lagrangian nonetheless carries only the Levi-Civita term $\tfrac14\check\varepsilon_{\nu\mu\lambda}B^*_\nu F_{\mu\lambda}$: there the $r'_t$ pieces of the two terms of Eq. (81) cancel against each other once the slice conditions are imposed at $a=0$. That cancellation is part of the variational reduction and is quoted here, not recomputed; what is recomputed is the symmetry of $r'_t$ and the resulting exact vanishing condition.

## The Self-Dual Field Strength

The antisymmetric part of the biquaternion is the field strength of the s-vector. The two-form
$$
H_{\mu\nu}=\sum_\lambda\epsilon_\lambda\,G^*_\lambda\,\check c_{\lambda\mu\nu}
$$
is not antisymmetric. It splits into a symmetric and an antisymmetric part, $H_{\mu\nu}=H_{(\mu\nu)}+H_{[\mu\nu]}$, and the two parts have different characters:
$$
H_{(\mu\nu)}=-\xi^*\epsilon_\mu\delta_{\mu\nu},\qquad
H_{[\mu\nu]}=-\tfrac{i}{2}\sum_{\lambda,\rho}\varepsilon_{\mu\nu}{}^{\lambda\rho}\,H_{[\lambda\rho]},
\qquad \xi^*=G^*\cdot j .
$$
The symmetric part is pure trace: it is the signed scalar $\xi^*$ times the diagonal weight, $\epsilon_\mu\delta_{\mu\nu}$ with no sum on $\mu$, and nothing else. The weight enters there with no other tensor. The antisymmetric part is **anti-self-dual**. The symbol carries two lower and two upper indices, because $\varepsilon_{\mu\nu\lambda\rho}H_{[\lambda\rho]}$ with all four indices down is not the Hodge dual under the weighted pairing; with the split the identity is closed on $H_{[\mu\nu]}$ itself.

Because the dual returns the same object, half of the six entries are dependent: the linear map $G^*\mapsto H_{[\mu\nu]}$ has complex rank three — verified — so $H_{[\mu\nu]}$ carries three complex components. Together with the single complex number $\xi^*$ in the trace, $H_{\mu\nu}$ has exactly the four complex components of $G^*_\mu$, and either object reconstructs the other:
$$
G^*_\mu=+\sum_\nu\epsilon_\nu\,H_{\mu\nu}\,j_\nu .
$$
These signs are fixed and not conventional. With $\check c=(r'_t-i\varepsilon)j$ and $j=(0,0,0,-1)$ as the corpus has them, the three identities of this paragraph hold exactly on random $G$; and the map $j\mapsto-j$ flips $\check c$, $H$ and $\xi^*$ together, so all three are invariant under the only freedom the neutral vector leaves.
The same construction runs backwards from the auxiliary potential. The source's
$$
H_{[\mu\nu]}=\tfrac{i}{2(m-a)}\sum_{\lambda,\rho}\epsilon_\lambda\epsilon_\rho\,C_{\mu\lambda\rho\nu}F_{\lambda\rho},
\qquad
C_{\mu\nu\lambda\rho}:=t'_{\mu\nu\lambda\rho}-i\varepsilon_{\mu\nu\lambda\rho},
$$
is anti-self-dual for the same reason, and it is the object in which the reduced Lagrangian of the previous section is written. The four-index symbol $C_{\mu\nu\lambda\rho}$ — a tensor, not the generator $C_\mu$ — is the source's $c$ with no neutral vector contracted into it, and $\check c_{\mu\nu\lambda}=C_{\mu\nu\lambda\rho}j_\rho$ with $c_{\mu\nu\lambda}=C_{\mu\nu\lambda\rho}k_\rho$; the $\varepsilon$ part of $C$ is what carries the anti-self-duality, and the $r'_t$ part is what keeps a symmetric component alive. That symmetric component is the price of the construction: because $H_{\mu\nu}$ is not antisymmetric, it has no Bianchi identity, and the duality has to define its potential by hand instead of reading it off a closure.

## The Two Dirac Equations

Two equations carry the name in this corpus, and they differ in which side of the multiplication acts. The duality touches both, so they are kept apart here.

**The one-sided pair.** On the Dirac module the massive equation is the pair whose mass couples the two chiral parts,
$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\,\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\,\tilde{Ξ}_{\mathrm{sp},R},
$$
both lines acting on the left, with the mass as the pairing of the two chiral parts and $\tilde\nabla^2$ not scalar. In the s-vector carrier the same pair is the source's two chiral parts,
$$
\begin{aligned}
&\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\,i\bigl(\partial/\partial x_\nu-ieA_\nu\bigr)G^{\mathrm R}_\lambda-m\,G^{\mathrm L*}_\mu=0,\\
&\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\,i\bigl(\partial/\partial x_\nu+ieA_\nu\bigr)G^{\mathrm L}_\lambda-m\,G^{\mathrm R*}_\mu=0,
\end{aligned}
$$
where $G^{\mathrm R}_\mu$ and $G^{\mathrm L}_\mu$ are the two chiral parts of $G_\mu$, the parts on which the chirality takes the values plus one and minus one,
$$
G^{\mathrm R}_\mu=\tfrac12\Bigl(G_\mu-\epsilon_\mu\sum_{\nu,\lambda}\check c_{\mu\nu\lambda}k_\lambda G_\nu\Bigr),\qquad
G^{\mathrm L}_\mu=\tfrac12\Bigl(G_\mu+\epsilon_\mu\sum_{\nu,\lambda}\check c_{\mu\nu\lambda}k_\lambda G_\nu\Bigr),
$$
with no sum on $\mu$ in $\epsilon_\mu$. Two equations, one per value; the opposite charges of the two lines are those two values, not a second dynamics.

**The two-sided equation.** Read on the algebra rather than on the module, the same content is one equation whose two sides are the two multiplications. In the observer frame it is
$$
\Bigl(-\tilde\nabla^{\natural}-k_m\,i\,\overline{\;\cdot\;}\,\vec e_z\Bigr)F=0,
$$
with $F\in\mathbb{B}$: the gradient acts from the left, the mass from the right, and the componentwise conjugation $\overline{\;\cdot\;}$ supplies the antilinear part. This is the source's equation: in the units of the check the time part of $-\tilde\nabla^{\natural}$ is $-e_t\,\partial/\partial R_t=i\,e_t\,\partial/\partial r'_t$ and its space part is $\vec e_x\partial/\partial R_x+\vec e_y\partial/\partial R_y+\vec e_z\partial/\partial R_z$. Since $\Gamma$ is the right multiplication by $-i\vec e_z$, the mass term is $m\,\Gamma\overline F$, and the equation can be moved to one side:
$$
-k_m\,i\,\overline F\,\vec e_z=m\,(-i\overline F\,\vec e_z)=m\,\Gamma\,\overline F
\qquad\Longrightarrow\qquad
\tilde\nabla^{\natural}F=m\,\Gamma\,\overline F ,
$$
one factor of $i$ spent on $i^2=-1$. Read back, $\tilde{Ξ}_{\mathrm{sp},L}=F$ and $\tilde{Ξ}_{\mathrm{sp},R}=-i\overline F\,\vec e_z$ are the two chiral fields, so the display is the pair above in another variable and not a second dynamics. The mass therefore acts by right multiplication by the **chirality**, on the conjugate field, and it is the same $\Gamma$ that appears in $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iC_0\,\Gamma\,iC_\mu\tilde{Ξ}_{\mathrm{sp}}$ above. $\Gamma$ is a right multiplication alone, and right multiplications by orthogonal units anticommute, so it anticommutes with all four generators: it is the chirality, not a fifth generator.

**Which one the parent action uses.** The first-order Dirac equation of the parent action is the single compact equation of the s-vector carrier,
$$
i\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\,\tilde\nabla_\nu G_\lambda-m\,G^*_\mu=0,
$$
whose mass couples $G$ to $G^*$ and whose two chiral lines above are its two parts, $G^{\mathrm R}_\mu$ and $G^{\mathrm L}_\mu$. It is the equation whose mass relates the two parts: one line, one mass, two parts. So the elimination of $H_\mu$ returns the *pair*, not one equation, and the chirality of the mass is the same chirality that the gauge reduction carries into the Chern–Simons term.

## The Mass as a Non-Integrable Phase

The mass enters as a shift of the covariant derivative, exactly as the charge does. The two chiral equations are the source's Eq. (94), and the star sits on the $G^{\mathrm R}$ line:
$$
\begin{aligned}
&\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\Bigl[\frac{\partial}{\partial x_\nu}+i\bigl(eA_\nu+mK_\nu\bigr)\Bigr]^{*}G^{\mathrm R}_\lambda=0,\\
&\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\Bigl[\frac{\partial}{\partial x_\nu}+i\bigl(eA_\nu+mK_\nu\bigr)\Bigr]G^{\mathrm L}_\lambda=0 .
\end{aligned}
$$
The conjugation on the first line is what makes the mass phase of $G^{\mathrm R}$ the conjugate of the mass phase of $G^{\mathrm L}$, and it is the reason the two parts carry opposite phases below.

$U_{\mathrm{vec},\mu}$ is built from the two chiral parts, as in the source's Eq. (100):
$$
U_{\mathrm{vec},\mu}=\frac{\tilde{Ξ}_{\mathrm{sp},R}^{\dagger}iC_0\,iC_\mu\tilde{Ξ}_{\mathrm{sp},R}}{2\tilde{Ξ}_{\mathrm{sp},R}^{\dagger}iC_0\tilde{Ξ}_{\mathrm{sp},L}}+\frac{\tilde{Ξ}_{\mathrm{sp},L}^{\dagger}iC_0\,iC_\mu\tilde{Ξ}_{\mathrm{sp},L}}{2\tilde{Ξ}_{\mathrm{sp},L}^{\dagger}iC_0\tilde{Ξ}_{\mathrm{sp},R}},
$$
two currents weighted by the two chiral cross-norms. The source's normalisation is $U_{\\mathrm{vec}}\\cdot U_{\\mathrm{vec}}=\sum_\mu\epsilon_\mu U_{\mathrm{vec},\mu} U_{\mathrm{vec},\mu}=1$ (Eq. 93), and its ground is the algebra's normed condition (Eq. 90), which equates the norm of the field to the norm of its current; a unit $U_{\\mathrm{vec}}$ exists because the two are the same number. That normalisation is quoted here and not recomputed: the corpus's weights on the bilinears fix the direction of $U_{\\mathrm{vec}}$ through the two terms of Eq. (100), and a numerical check of the normalisation in those weights did not reproduce the value one, so the statement is recorded as the source's.

The structural role of $U_{\\mathrm{vec}}$ is what the article uses: the *same* vector appears in the derivative shift, Eq. (94), and in the reconstruction of the field from the two-form, Eq. (92), so the mass is a direction in the complexified tangent space rather than a scalar, and the two chiral parts see it with conjugate signs.

The derivative shift integrates to a phase,
$$
G^{\mathrm R}_\mu=G^{0\mathrm R}_\mu\exp\Bigl(-i\!\int\bigl(eA_\nu+mK_\nu\bigr)^*dx_\nu\Bigr),
\qquad
G^{\mathrm L}_\mu=G^{0\mathrm L}_\mu\exp\Bigl(i\!\int\bigl(eA_\nu+mK_\nu\bigr)dx_\nu\Bigr),
$$
which depends on the path from a fixed initial point, and $U_{\\mathrm{vec}}$ is form-invariant under the map: it is the same function of the mapped fields as of the original ones, so the map is invertible and the massless and massive solutions correspond one to one. This is the source's **non-integrable phase**: the mass is not a scalar multiplying $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iC_0\tilde{Ξ}_{\mathrm{sp}}$ but a unit complex vector, a direction in the complexified tangent space, and the phase it generates is path-dependent and is not removable by a gauge transformation of the s-vector. Its real part is the vector current and its imaginary part the axial current, so the phase and the "scale" of the field are the two halves of one complex vector.

The topological mass of the gauge field and the phase mass of the Dirac field are then the same object read in the two reductions: in both, the mass is a first-order coupling carried by a direction that the algebra supplies and that no gauge transformation removes. In the gauge reduction that direction is the neutral spacelike $j$, on which the Chern–Simons symbol is built; in the Dirac reduction it is the complex unit vector $U_{\\mathrm{vec}}$, on which the phase is built. Both are directions the algebra fixes, not parameters put in by hand.

## What the Equivalence Is and Is Not

**It is** a duality of the strong–weak type. The source's reason is that a duality typically exchanges the regimes, $g\mapsto1/g$, so a weak-coupling description in one variable is a strong-coupling description in the other, and having the explicit map makes perturbation theory available on both sides. No other article in the corpus states a dual equivalence of this kind; *The Proca Equation: Massive Spin 1 in Biquaternionic Form* is the second-order counterpart, not a dual, because there the mass is a scalar term and no elimination produces it.

**It is not** a new solution of either theory. The duality relates the *descriptions*, not the dynamics: a solution of the Dirac equation maps to a solution of the gauge equation and conversely, and no new physics follows from the map itself. What the duality supplies is a dictionary — Dirac mass to topological mass, Dirac current to field strength, Dirac chirality to the gauge dual pair — and a definition of the potential that makes no reference to a Bianchi identity.

**It is** classical. Both reductions are statements about actions and their variations; the source says "at least classically" and says nothing about the quantum theory.

## Open Questions

1. **The four-dimensional mass term.** In four dimensions the reduced Lagrangian carries the cubic form, not a Chern–Simons term; the Chern–Simons term appears only after the reduction to the spin manifold. The source's route to four dimensions is the promotion by the embedding vector $j$, so the four-dimensional topological mass is $j$-dependent. Whether there is a four-dimensional topological mass that does not single out a direction is open.

2. **The spectator scalar.** The scalar $\xi$ is carried through both reductions unchanged and, at $a=0$ on the spin manifold, does not interact with $B$. In four dimensions it is not a spectator: it sources the "electric" and "magnetic" currents of the Maxwell-like pair. Whether the three-dimensional decoupling is a property of the theory or of the gauge $a=0$ is not settled.

3. **The role of the triality.** The parent action is written in the s-vector variables, and the s-vector carries the triality (order-three ding) structure. Does the dual equivalence commute with the triality map $A\mapsto B\mapsto N\mapsto A$? If it does, the equivalence is triality-covariant, which would be a strong structural statement; if not, the triality breaks at the duality.

4. **The quantised equivalence.** A classical dual equivalence need not survive quantisation. Do the two reductions give the same anomaly, the same $\beta$ function, the same $S$-matrix? *Anomalies and Anomaly Cancellation in Biquaternionic Form* is the natural place to test it.

5. **The quantisation of the phase.** The source conjectures that single-valuedness of the non-integrable phase on a closed curve quantises the phase integral that $U_{\\mathrm{vec}}$ accumulates, by analogy with Dirac's monopole argument. The conjecture is stated and not proved. Whether $U_{\\mathrm{vec}}$ has a geometric meaning beyond the plane-wave case is the source's own open question.

These questions are open.

## Summary

The Dirac Lagrangian in the vector representation and the Lagrangian of the three-dimensional topologically massive gauge field are **dual**: one first-order parent action in the s-vector variables reduces, on one elimination, to the Dirac Lagrangian — first-order kinetic term in the $\check c$ structure constants, mass term $m(G^*G^*+GG)$ coupling the field to its conjugate — and, on the other elimination, to a second-order Lagrangian for the dual potential whose mass term is first order, one derivative and one power of $m$. On the spin manifold orthogonal to $j$, at $a=0$, the latter reads
$$
\mathcal{L}_G=-\tfrac{1}{4m}\sum_{\mu,\lambda}\epsilon_\mu\epsilon_\lambda F_{\mu\lambda}F_{\mu\lambda}+\tfrac14\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\,\check\varepsilon_{\nu\mu\lambda}\,B^*_\nu F_{\mu\lambda},
$$
Maxwell plus a Chern–Simons mass, with $\check\varepsilon_{\nu\mu\lambda}=\sum_\rho\varepsilon_{\nu\mu\lambda\rho}j_\rho$ and the gauge equation $\sum_\nu\epsilon_\nu\,\partial F_{\nu\mu}/\partial x_\nu+\tfrac m2\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\check\varepsilon_{\mu\nu\lambda}F^*_{\nu\lambda}=0$. The same $m$ is, in the other reduction, the non-integrable phase of the Dirac field: a shift $mK_\mu$ of the covariant derivative, with $U_{\\mathrm{vec}}$ the source's unit complex vector, integrated along a path.

Three facts make the mechanism work. The first-order mass term changes only by a total derivative under the gauge freedom of the dual potential, which is what "topological" means here. Of the two parts of $\check c$, only the Levi-Civita one appears in the reduced Lagrangian of Eq. (88) — the $r'_t$ part cancels in the reduction — and a Levi-Civita contraction is a Chern–Simons term. And the two-form $H_{\mu\nu}$ carries the same information as the s-vector — three complex components in the anti-self-dual $H_{[\mu\nu]}$ and one in the trace $H_{(\mu\nu)}=-\xi^*\epsilon_\mu\delta_{\mu\nu}$, with no sum on $\mu$, which is four — so the auxiliary field of the reduction is the antisymmetric part of the biquaternion.

The parent actions and the eliminations are the source's; the algebraic identities they use were recomputed for this article and hold. The eliminations themselves were not recomputed, and no quantum statement is made.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C_\mu:\tilde{Ξ}_{\mathrm{sp}}\mapsto a_\mu\tilde{Ξ}_{\mathrm{sp}} b_\mu$ | Generator of index $\mu$; $a_0=e_t$, $a_k=\vec e_k$, $b_0=\vec e_x$, $b_k=\vec e_y$. Two-sided for $\mu=1,2,3$, a right action alone for $\mu=0$, whose left factor is the identity |
| $iC_\mu$ | The central $i$ times that generator; the same sides; $\{iC_\mu,iC_\nu\}=2\epsilon_\mu\delta_{\mu\nu}$, with no sum on $\mu$ |
| $\Gamma:\tilde{Ξ}_{\mathrm{sp}}\mapsto-i\tilde{Ξ}_{\mathrm{sp}}\vec e_z=\tilde{Ξ}_{\mathrm{sp}}(i\omega)$ | Chirality, a right action alone; $\Gamma^2=\mathrm{id}$; $\Gamma=i\,(C_0C_1C_2C_3)$, whose left factors cancel in pairs |
| $\omega=-\vec e_z$ | Pseudoscalar, $\omega^2=-e_t$; the source's $i$, kept distinct from the central unit |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$ | Biquaternionic gradient and its quaternion conjugate, elements acting on the left |
| $\tilde\nabla^{ea}_\mu$, $\tilde\nabla^{a}_\mu$ | The same derivative with the electromagnetic and $a$ insertions; superscripts name insertions, not a second operator |
| $\Box$ | The d'Alembertian, the norm of $\tilde\nabla$; on $Q_t=i r'_t$ it is $\Delta-\partial^2/\partial {r'_t}^2$ |
| $c_5{}_{\mu\nu}$ | The source's array of the chirality on the four-vector carrier, written here as $-\epsilon_\mu\check c_{\mu\nu\lambda}k_\lambda$ with no sum on $\mu$; $(c_5)^2=1$, $\epsilon$-antisymmetric |
| $\delta_{\mu\nu}=(1,1,1,1)$ | The unit metric of the index space; it pairs two slots as $\epsilon_\mu\delta_{\mu\nu}$, with no sum on $\mu$ |
| $\epsilon=(1,-1,-1,-1)$ | The plain weight, read from the multiplication $\mathrm{Sc}(e_\mu e_\nu)=\epsilon_\mu\delta_{\mu\nu}$; the diagonal of the generator pairing; distinct from $\varepsilon$ |
| $G^{\mathrm R}_\mu$, $G^{\mathrm L}_\mu$ | The two chiral parts of the s-vector, of value plus one and minus one: elements, not a right and a left multiplication |
| $G_\mu$ | s-Vector (complex four-vector), the Dirac field in the vector representation |
| $H_\mu$ | Dual (potential) field of the four-dimensional parent action, complex four-vector |
| $B_\mu$ | Complex potential of the three-dimensional version, axial gauge $B_\mu j^\mu=0$ |
| $\xi$ | Complex scalar, $\xi=G_\mu j^\mu$; $G_\mu=G^\mu-j_\mu\xi$ with $G^\mu=p^+_{\mu\nu}G_\nu$ |
| $p^\pm_{\mu\nu}$ | Projectors; $p^+_{\mu\nu}=\epsilon_\mu\delta_{\mu\nu}+j_\mu j_\nu$, $p^-_{\mu\nu}=-j_\mu j_\nu$, $p^+_{\mu\nu}+p^-_{\mu\nu}=\epsilon_\mu\delta_{\mu\nu}$, with no sum on $\mu$ |
| $A_\mu$ | Electromagnetic four-potential; it enters only the covariant derivative |
| $B_\mu, N_\mu$ | Real and imaginary four-vectors of the field, $G=B+iN$ |
| $k_\mu$, $j_\mu$ | Timelike and spacelike neutral vectors, units of $c$ and $\check c$ |
| $c_{\mu\nu\lambda}$, $\check c_{\mu\nu\lambda}$ | Structure constants on $k$ and on $j$; $\check c=(r'_t-i\varepsilon)j$ |
| $\check\varepsilon_{\nu\mu\lambda}=\sum_\rho\varepsilon_{\nu\mu\lambda\rho}j_\rho$ | Levi-Civita symbol of the $j$-slice |
| $H_{\mu\nu}=\sum_\lambda\epsilon_\lambda G^*_\lambda\check c_{\lambda\mu\nu}$ | Two-form of the s-vector; $H_{(\mu\nu)}=-\xi^*\epsilon_\mu\delta_{\mu\nu}$ with no sum on $\mu$, and $H_{[\mu\nu]}$ anti-self-dual |
| $\xi^*=G^*\cdot j$ | Trace of the two-form, $\xi^*=\sum_\mu\epsilon_\mu G^*_\mu j_\mu$; the complex scalar $\xi=G\cdot j$ with a star |
| $F_{\mu\nu}=\partial B_\nu/\partial x_\mu-\partial B_\mu/\partial x_\nu+iaj_\mu B^*_\nu-iaj_\nu B^*_\mu$ | Field strength of the dual potential |
| $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}iC_0\tilde{Ξ}_{\mathrm{sp}}=\sum_\nu\epsilon_\nu(N_\nu N_\nu-B_\nu B_\nu)$ | Dirac bilinear |
| $U_{\mathrm{vec},\mu}$ | Complex vector of Eq. (100) carrying the mass as a non-integrable phase; normalised to $U_{\\mathrm{vec}}\\cdot U_{\\mathrm{vec}}=1$ in the source |
| $\varepsilon_{\mu\nu\lambda\rho}$ | Totally antisymmetric symbol, $\varepsilon_{0123}=1$ |
| $m$, $a$ | Fermion mass (equated to the topological gauge mass) and the auxiliary real constant $a\ne m$ |
| $S_{GH}$, $S_{G\xi B}$ | The two parent actions, four- and three-dimensional |
| $\mathcal{L}_D$, $\mathcal{L}_H$, $\mathcal{L}_{\xi B}$, $\mathcal{L}_G$ | Dirac, dual-potential, scalar-plus-potential and spin-manifold Lagrangians |

## Further Reading

- Liu Yu-Fen, "Triality and Dual Equivalence Between Dirac Field and Topologically Massive Gauge Field," arXiv:hep-th/0602275 (2006), for the parent actions (55) and (77), their eliminations, the self-dual field strength, the topological reading of the mass, and the non-integrable phase. **The eliminations are quoted; the algebraic identities they use are recomputed.**
- Liu Yu-Fen, "Triality, Biquaternion and Vector Representation of the Dirac Equation," arXiv:math-ph/0109008 (2001), for the s-vector representation, the bosonic Dirac Lagrangian, the self-dual form of the massive equation, and the bilinear dictionary on which the parent action is built.
- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the rule this article follows in printing no array, and for what a display built on a declared axis costs.
- S. Deser and R. Jackiw, *Physics Letters B* **139** (1984) 371, for the parent (master) action method itself.
- S. Deser, R. Jackiw and S. Templeton, "Topologically massive gauge theories," *Annals of Physics* **140** (1982) 372, for the original topologically massive gauge theory in $2+1$ dimensions and its Chern–Simons mass.
- H. Weyl, "Elektron und Gravitation," *Zeitschrift für Physik* **56** (1929) 330, and C. N. Yang, "Integral formalism for gauge fields," *Physical Review Letters* **33** (1974) 445, for the non-integrable phase factor that the mass generalises.
- The companion corpus articles: [The s-Vector Representation of the Dirac Spinor in Biquaternionic Form](the-s-vector-representation-of-the-dirac-spinor-in-biquaternionic-form.html), [Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form](triality-and-the-ding-construction-for-the-dirac-spinor-in-biquaternionic-form.html), [The Proca Equation: Massive Spin 1 in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), [Anyons and Braid Statistics in Biquaternionic Form](anyons-and-braid-statistics-in-biquaternionic-form.html), and [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html).
