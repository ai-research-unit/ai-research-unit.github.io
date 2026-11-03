# __Dual Equivalence of the Dirac and Topologically Massive Gauge Fields__

## Introduction

A massive spin-1 field can acquire its mass in more than one way. The **Proca** mass is second order and scalar: a term $\mu^2 A_\mu A^\mu$ in the Lagrangian and a Klein–Gordon factor in the propagator. A **topological** mass is first order: a term with one derivative, one power of the mass, and a Levi-Civita symbol, which in $2+1$ dimensions is the Chern–Simons term of Deser, Jackiw and Templeton.

Liu Yu-Fen's claim is a duality of the second kind. The **Dirac** Lagrangian in the vector representation is first order in the derivative and carries its mass as a term that couples the field to its conjugate. A single first-order **parent action** in the same variables has two reductions: eliminating the auxiliary potential gives back the Dirac Lagrangian, and eliminating the Dirac field gives a second-order Lagrangian whose mass term is first order — on the three-dimensional spin manifold, exactly the Maxwell plus Chern–Simons Lagrangian of the topologically massive gauge field. The two describe the same propagating modes, at least classically.

The article records the two parent actions and their four eliminations, and separates what is verified from what is quoted. It is the physics companion of *The s-Vector Representation of the Dirac Spinor in Biquaternionic Form* and of *Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form*: the parent action is written in the s-vector variables, and its two reductions pass through the self-dual field strength and the cubic (order-three ding) form of those articles.

**The frame.** Four-vector indices $\mu=0,1,2,3$ carry the generator metric of the Dirac module,
$$
g_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1),
$$
the corpus's *generator metric*, not the $ict'$ metric $\mathrm{diag}(-1,+1,+1,+1)$ of $\mathbb{M}_-$. Contractions are $V\cdot W=\sum_{\mu,\nu}V_\mu g_{\mu\nu}W_\nu=\sum_\mu\epsilon_\mu V_\mu W_\mu$ with the sign vector $\epsilon=(1,-1,-1,-1)$, and every index the source raises is carried by an $\epsilon$ in the sums below. The Levi-Civita symbol $\varepsilon_{\mu\nu\lambda\rho}$ is totally antisymmetric with $\varepsilon_{0123}=1$; it is a different letter from $\epsilon$. Two neutral vectors are fixed by the structure constants, the timelike $k_\mu$ of $c_{\mu\nu\lambda}=(t'_{\mu\nu\lambda\rho}-i\varepsilon_{\mu\nu\lambda\rho})k_\rho$ and the spacelike $j_\mu$ of $\check c_{\mu\nu\lambda}=(t'_{\mu\nu\lambda\rho}-i\varepsilon_{\mu\nu\lambda\rho})j_\rho$, with $k\cdot k=-j\cdot j=1$ and $k\cdot j=0$. The source's point is that they are offshoots of the algebra and not extra structure. The projectors are
$$
p^\pm_{\mu\nu}=\tfrac12\bigl(g_{\mu\nu}\pm c_3{}_{\mu\nu}\bigr),\qquad p^+_{\mu\nu}=g_{\mu\nu}+j_\mu j_\nu,\qquad p^-_{\mu\nu}=-j_\mu j_\nu,
$$
with $p^++p^-=g$, so that $G_\mu=G^\mu-j_\mu\phi$ splits any four-vector into its three-dimensional part $G^\mu=p^+_{\mu\nu}G_\nu$ and its complex scalar $\phi=G_\mu j^\mu$.

**The cells.** The article is written in the cell algebra. The generator of index $\mu$ is the cell
$$
C_\mu=L_{a_\mu}R_{b_\mu},\qquad a_0=e_t,\quad a_k=\vec e_k,\qquad b_0=\vec e_x,\quad b_k=\vec e_y,\qquad C_\mu\Psi=a_\mu\Psi b_\mu,
$$
and $\mathcal{D}(w)=\sum_\mu w_\mu\,iC_\mu$ contracts the four generators with the components $w_\mu$. The cells obey the Clifford relations $\{iC_\mu,iC_\nu\}=2g_{\mu\nu}e_t$, so the metric sits inside the generator and a cell bilinear carries no explicit $\epsilon$. The chirality cell is
$$
\Gamma=-iC_5=-iL_{e_t}R_{\vec e_z},\qquad \Gamma^2=e_t,\qquad \Gamma\,C_\mu=-C_\mu\Gamma,\qquad \Gamma=iC_0C_1C_2C_3 .
$$
The gammas are a frame of this algebra. They appear once, in §The Gamma Formulation, and nowhere in the body.

## The Parent Action

### The Fields

$G_\mu$ is the Dirac field in the vector representation, the **s-vector**: a complex four-vector with the bilinears of the companion article,
$$
\bar\Psi\Psi=-\tfrac12\sum_\nu\epsilon_\nu\bigl(G_\nu G_\nu+G^*_\nu G^*_\nu\bigr),\qquad
\bar\Psi\,iC_\mu\Psi=\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,G^*_\nu c_{\nu\mu\lambda}G_\lambda,
\qquad
\bar\Psi\,\Gamma\,iC_\mu\Psi=-\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,G^*_\nu\check c_{\nu\mu\lambda}G_\lambda,
$$
the last one by $\Gamma\,iC_\mu=-i\cdot i\,C_5C_\mu=C_5C_\mu$, one factor of $i$ spent on $i^2=-1$. $H_\mu$ is the dual potential: a complex four-vector, the auxiliary field of the four-dimensional parent action. In the three-dimensional version the auxiliary field is the complex potential $B_\mu$ in the axial gauge $B_\mu j^\mu=0$, and the complex scalar $\phi$ is a spectator carried through both reductions unchanged. $A_\mu$ is the electromagnetic potential, and it enters only through the covariant derivative
$$
\tilde\nabla_\mu G_\lambda=\partial/\partial x_\mu G_\lambda-ieA_\mu\,g_{\lambda\rho}\,c_5{}^{\rho\sigma}G_\sigma .
$$
The derivative that the auxiliary field uses is the same object with the constant $a$ added in the manner of a second coupling, $\nabla^a_\mu=\partial/\partial x_\mu+ia\,j_\mu C$ with $C$ the conjugation, so that
$$
\nabla^a_\mu B_\nu-\nabla^a_\nu B_\mu=\partial/\partial x_\mu B_\nu-\partial/\partial x_\nu B_\mu+ia\,j_\mu B^*_\nu-ia\,j_\nu B^*_\mu=F_{\mu\nu},
$$
which is the source's field strength: it reduces to the Maxwell tensor at $a=0$ and is invariant under the generalized gauge transformation $B_\mu\mapsto B_\mu+p^+_{\mu\nu}\partial/\partial x_\nu\Theta$. The constant $a$ is real and differs from $m$; it survives in the reductions as the combination $m-a$ and is set to zero in the three-dimensional case.

### The Four-Dimensional Parent Action

The parent action is linear in the auxiliary field and quadratic in the Dirac field,
$$
S_{GH}=\int\Bigl[\bigl(G_\nu+\tfrac12 H_\nu\bigr)^*i\check c_{\nu\mu\lambda}\nabla^{ea}_\mu H_\lambda+\tfrac{m-a}{2}G_\nu G_\nu-\bigl(\nabla^{ea}_\mu H_\nu\bigr)^*i\check c_{\nu\mu\lambda}\bigl(G_\lambda+\tfrac12 H_\lambda\bigr)+\tfrac{m-a}{2}G^*_\nu G^*_\nu+\partial_\mu Z_0^\mu\Bigr],
$$
with $\nabla^{ea}$ the same derivative with the electromagnetic term of $\tilde\nabla$ added to the $a$-term. The *same* $\check c$ contracts the Dirac field, the auxiliary field and the derivative in both halves: the two eliminations are two ways of inverting one linear system, and the coupling constants $e$ and $a$ sit in the derivative while the mass $m$ sits in the quadratic terms. $Z_0^\mu$ is a surface term, chosen so that the total divergence produced by the elimination vanishes.

### The Two Eliminations

**Eliminating the auxiliary field.** Varying $H_\mu$ gives
$$
\check c_{\mu\nu\lambda}\nabla^{ea}_\nu G_\lambda=-\check c_{\mu\nu\lambda}\nabla^{ea}_\nu H_\lambda ,
$$
and substituting this back leaves the **Dirac Lagrangian** in the vector representation,
$$
\boxed{\;\mathcal{L}_D=\tfrac12\Bigl[\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\Bigl(\bigl(\tilde\nabla_\mu G_\nu\bigr)^*i\check c_{\nu\mu\lambda}G_\lambda-G^*_\nu\,i\check c_{\nu\mu\lambda}\,\tilde\nabla_\mu G_\lambda\Bigr)+m\sum_\nu\epsilon_\nu\bigl(G^*_\nu G^*_\nu+G_\nu G_\nu\bigr)\Bigr]\;}
$$
up to the total divergence that $Z_0$ removes. The mass couples $G$ to $G^*$: it is chirality-off-diagonal, and that is why the s-vector is not a pair of independent complex vectors. For $G=B+iN$ one has $G^2+G^{*2}=2(B^2-N^2)$ by $i^2=-1$, so the same term is the real bilinear $m\sum_\nu\epsilon_\nu(N_\nu N_\nu-B_\nu B_\nu)$.

The source does not solve the varied equation for $H_\mu$, and says so: the equation is linear in $H$ and its conjugate, the two are coupled by the $a$-term, and the solution is non-local. What the source uses is the equation itself, which is enough to eliminate $H$ from the action and to display the Dirac Lagrangian. The elimination is therefore algebraic in form and non-local in content.

**Eliminating the Dirac field.** Varying $G_\nu$ gives the linear relation
$$
(m-a)G_\lambda=\bigl(\nabla^{ea}_\mu H_\nu\bigr)^*i\check c_{\nu\mu\lambda},
$$
and substituting it back leaves a **second-order Lagrangian** for $H_\mu$,
$$
\mathcal{L}_H=\tfrac{1}{2(m-a)}\sum_{\mu,\nu,\lambda,\rho,\delta}\epsilon_\mu\epsilon_\nu\epsilon_\lambda\epsilon_\rho\epsilon_\delta\bigl(\check c_{\nu\mu\lambda}\nabla^{ea}_\mu H_\lambda\bigr)\bigl(\check c_{\nu\rho\delta}\nabla^{ea}_\rho H_\delta\bigr)+\tfrac12\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda H^*_\nu\,i\check c_{\nu\mu\lambda}\nabla^{ea}_\mu H_\lambda+\text{c.c.}+\partial_\mu Z_0^\mu ,
$$
quadratic in the derivative. The first term is the kinetic term; the second is first order and bilinear in the mass, the **cubic form** of the companion article. At $a=e=0$ and after the rescaling $H_\mu\mapsto bH_\mu$ that restores canonical normalisation it reads
$$
\mathcal{L}_H=-\tfrac{b^2}{2m}\Bigl[\sum_{\mu,\nu}\epsilon_\mu\epsilon_\nu\,\partial_\mu H_\nu\,\partial_\mu H_\nu-m\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda H^*_\nu\,i\check c_{\nu\mu\lambda}\partial_\mu H_\lambda-\partial_\mu\bigl(H^\mu\partial H\bigr)\Bigr]+\text{c.c.},
$$
so the mass term has one derivative and one power of $m$ — the hallmark of a topological mass, and the reason the source calls the two actions dual.

### The Three-Dimensional Parent Action and the Topological Mass

The three-dimensional version separates the scalar first. The duality is taken between the pairs $(G^\mu;\phi)$ and $(B^\mu;\phi)$ with the *same* $\phi$, and the parent action is
$$
S_{G\phi B}=\int\Bigl[\tfrac12\bigl(G^*_\nu+\tfrac12 B^*_\nu\bigr)i\check c_{\nu\mu\lambda}F_{\mu\lambda}+\tfrac{i}{2}\bigl(G^\mu\partial_\mu\phi^*-\phi^*\partial_\mu G^\mu\bigr)+\tfrac{m-a}{2}G_\nu G_\nu+\tfrac{i}{2}\phi^*j^\mu\nabla^{-a}_\mu\phi+\text{c.c.}+\partial_\mu Z_1^\mu\Bigr].
$$
Varying $B_\mu$ gives
$$
\check c_{\mu\nu\lambda}\bigl(\nabla^a_\nu G_\lambda-\nabla^a_\lambda G_\nu\bigr)=-\check c_{\mu\nu\lambda}F_{\nu\lambda},
$$
and substituting back returns the Dirac Lagrangian, now with $A_\mu=0$ and $G_\mu=G^\mu-j_\mu\phi$. Varying $G_\nu$ gives
$$
(m-a)G^\mu=\tfrac{i}{2}F_{\lambda\nu}\check c^{*\nu\lambda\mu}-i\,p^{\mu\nu}_+\partial_\nu\phi^* ,
$$
and substituting this back leaves
$$
\mathcal{L}_{\phi B}=\tfrac{1}{8(m-a)}\sum_{\mu,\lambda,\rho,\delta}\epsilon_\mu\epsilon_\lambda\epsilon_\rho\epsilon_\delta\bigl(\check c_{\nu\mu\lambda}F_{\mu\lambda}\bigr)\bigl(\check c_{\nu\rho\delta}F_{\rho\delta}\bigr)+\tfrac14\sum_{\mu,\nu,\lambda}\epsilon_\mu\epsilon_\nu\epsilon_\lambda B^*_\nu\,i\check c_{\nu\mu\lambda}F_{\mu\lambda}+\text{(scalar sector)}+\text{c.c.}+\partial_\mu Z_2^\mu .
$$
On the spin manifold, where the fields depend on the three coordinates of the slice orthogonal to $j$ and $j^\nu\partial_\nu B_\mu=j^\nu\partial_\nu\phi=0$, and at $a=0$, the interaction term between $B$ and $\phi$ becomes a surface term and the Lagrangian reduces to
$$
\boxed{\;\mathcal{L}_G=-\tfrac{1}{4m}\sum_{\mu,\lambda}\epsilon_\mu\epsilon_\lambda F_{\mu\lambda}F_{\mu\lambda}+\tfrac14\sum_{\mu,\nu,\lambda}\check\varepsilon_{\nu\mu\lambda}B^*_\nu F_{\mu\lambda}+\text{(scalar sector)}+\text{c.c.},\;}
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

**Quoted, recomputed, and open.** The two parent actions, the four varied equations and the four Lagrangians are the source's, Eqs. (55)–(61), (71), (77)–(81) and (88). This pass recomputed the algebra those expressions use — the cell Clifford relations, $\Gamma\,iC_\mu=C_5C_\mu$, the split $i\check c=\varepsilon j+i\,t'j$, the anti-self-duality of $H_{[\mu\nu]}$, the proportionality $H_{(\mu\nu)}=\phi^*g_{\mu\nu}$, the reconstruction of $G$ from $H$, the total antisymmetry of $\check\varepsilon_{\nu\mu\lambda}$, the vanishing of the $t'$ part on an antisymmetric $F$, and the identities of §*The Mass as a Non-Integrable Phase* — and not the eliminations themselves, which are a variational computation on the source's field content.

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
with $\Theta$ a function on the spin manifold, and $\check c_{\nu\mu\lambda}\partial_\mu\partial_\lambda\Theta=j_\nu\,\partial\partial\Theta$ reduces the condition to the wave equation.

**There is no Bianchi identity.** The structure constants $\check c$ contain the antisymmetric (Lie) and the symmetric (Jordan) parts, so the two-form built from the potential is not the curl of anything with an automatic closure: the object the duality exchanges is the self-dual tensor of §*The Self-Dual Field Strength*, not an antisymmetric field strength. The source's reason for the construction is stated as the definition of a potential without a Bianchi identity: the second of the Maxwell-like pair satisfied by the Dirac field plays the role of the Bianchi identity only when $\phi_1+\phi_2=0$, and in that gauge the field strength can be written as $F_{\mu\nu}$ above.

**Why the $t'$ part drops out.** The mass term of the three-dimensional reduction is the contraction of $F$ with $i\check c$, and $i\check c$ has a $t'$ part and an $\varepsilon$ part. The tensor $t'_{\mu\nu\lambda\rho}=g_{\mu\nu}g_{\lambda\rho}+g_{\mu\rho}g_{\nu\lambda}-g_{\mu\lambda}g_{\nu\rho}$ is symmetric under $\mu\leftrightarrow\lambda$, so its contraction with the antisymmetric $F_{\mu\lambda}$ vanishes identically — verified — and only the Levi-Civita part survives. That is why the surviving mass term is a Chern–Simons term and not a Jordan-type coupling: the antisymmetry of the field strength selects the antisymmetric part of the algebra's structure constants.

## The Self-Dual Field Strength

The antisymmetric part of the biquaternion is the field strength of the s-vector. The two-form
$$
H_{\mu\nu}=\sum_\lambda\epsilon_\lambda\,G^*_\lambda\,\check c_{\lambda\mu\nu}
$$
is not antisymmetric. It splits into a symmetric and an antisymmetric part, $H_{\mu\nu}=H_{(\mu\nu)}+H_{[\mu\nu]}$; the symmetric part is proportional to the metric, $H_{(\mu\nu)}=\phi^*g_{\mu\nu}$, and the antisymmetric part is **anti-self-dual**,
$$
H_{[\mu\nu]}=-\tfrac{i}{2}\sum_{\lambda,\rho}\epsilon_\lambda\epsilon_\rho\,\varepsilon_{\mu\nu\lambda\rho}H_{[\lambda\rho]} .
$$
Anti-self-duality halves the six components of a two-form, so $H_{[\mu\nu]}$ carries three complex independent components, one for each complex component of the three-dimensional part of $G_\mu$. The two objects carry the same information and either reconstructs the other:
$$
G^*_\mu=-\sum_\nu\epsilon_\nu\,H_{\mu\nu}\,j_\nu .
$$
The two signs above — the one of $\phi^*g_{\mu\nu}$ and the one of the reconstruction — flip together with the orientation of $\check c$, that is, with the sign of $j$; both are a convention, and what was checked is the proportionality to the metric and the one-to-one correspondence, not the orientation.
The same construction runs backwards from the auxiliary potential: the source's
$$
H_{[\mu\nu]}=\tfrac{i}{2(m-a)}\sum_{\lambda,\rho}\epsilon_\lambda\epsilon_\rho\,c_{\mu\lambda\rho\nu}F_{\lambda\rho}
$$
is anti-self-dual for the same reason, and it is the object in which the reduced Lagrangian of the previous section is written. Because $H_{\mu\nu}$ is not antisymmetric, it has no Bianchi identity; the price of the self-duality is the loss of the closure that an antisymmetric field strength would have had.

## The Two Dirac Equations

Two equations carry the name in this corpus, and they differ in which side of the multiplication acts. The duality touches both, so they are kept apart here.

**The one-sided pair.** On the Dirac module the massive equation is the chirality-off-diagonal pair
$$
L_{\tilde\nabla}\tilde\Psi_R=m\,\tilde\Psi_L,
\qquad
L_{\tilde\nabla^{\natural}}\tilde\Psi_L=m\,\tilde\Psi_R,
$$
each line a left multiplication, with the mass as the pairing of the two chiral halves. In the s-vector carrier the same pair is the source's two chiral projections,
$$
\begin{aligned}
&\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\,i\bigl(\partial/\partial x_\nu-ieA_\nu\bigr)R_\lambda-m\,L^*_\mu=0,\\
&\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\,i\bigl(\partial/\partial x_\nu+ieA_\nu\bigr)L_\lambda-m\,R^*_\mu=0,
\end{aligned}
$$
with $R_\mu=\tfrac12(g_{\mu\nu}+c_5{}_{\mu\nu})G_\nu$ and $L_\mu=\tfrac12(g_{\mu\nu}-c_5{}_{\mu\nu})G_\nu$ the two chiral biquaternions. Two equations, one per chirality; the $\pm$ in the derivative is the sign of the chirality, not a second dynamics.

**The two-sided equation.** Read on the algebra rather than on the module, the same content is one equation whose two sides are the two multiplications,
$$
L_{\tilde\nabla^{\natural}}F=m\,\Gamma\bar F,
$$
where $F\in\mathbb{B}$ and $\bar F$ is the coefficient conjugate. The derivative acts on the left, the mass on the right, and the conjugation supplies the antilinear part. The chirality cell is a pure right multiplication, and right multiplications by orthogonal units anticommute, so $\Gamma$ anticommutes with all four generators; it is the chirality, not a fifth generator.

**Which one the parent action uses.** The first-order Dirac equation of the parent action is the single compact equation
$$
i\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\,\tilde\nabla_\nu G_\lambda-m\,G^*_\mu=0,
$$
the two-sided form in the s-vector carrier: the mass couples $G$ to $G^*$, and the two chiral lines above are its projections under $R_\mu$ and $L_\mu$. So the elimination of $H_\mu$ returns the *pair*, not one equation, and the chirality of the mass is the same chirality that the gauge reduction carries into the Chern–Simons term.

## The Mass as a Non-Integrable Phase

The mass enters as a shift of the covariant derivative, exactly as the charge does:
$$
\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\,\check c_{\mu\nu\lambda}\bigl[\partial/\partial x_\nu+i\bigl(eA_\nu+mK_\nu\bigr)\bigr]R_\lambda=0,
$$
with the conjugate equation for $L_\mu$. $K_\mu$ is a unit complex vector built from the chiral halves of the field,
$$
K_\mu=\frac{\bar\Psi_R\,iC_\mu\Psi_R}{2\bar\Psi_R\Psi_L}+\frac{\bar\Psi_L\,iC_\mu\Psi_L}{2\bar\Psi_L\Psi_R},
\qquad
K\cdot K=\sum_\mu\epsilon_\mu K_\mu K_\mu=1,
$$
and it carries the mass as a cell bilinear,
$$
\bar\Psi\Psi=\sum_\mu\epsilon_\mu K_\mu\,\bar\Psi\,iC_\mu\Psi=\bar\Psi\,\mathcal{D}(K^\flat)\Psi,
\qquad K^\flat_\mu=\sum_\nu g_{\mu\nu}K_\nu .
$$
The $\epsilon$ on the first equality is the metric contraction of $K$ with the current, and the second equality is the definition of $\mathcal{D}$: $\mathcal{D}(K^\flat)=K_t\,iC_0-K_x\,iC_1-K_y\,iC_2-K_z\,iC_3$. No $i^2$ enters there, because the metric already sits inside $iC_\mu$; the only $i$'s are the four of the four cells. The same vector converts one chirality into the other: contracted with the generators, $\mathcal{D}(K)$ takes the right-handed half of the spinor to the left-handed half and back. The source writes that pair with the gammas; the cell form of the same two lines is the statement that the $K$-contraction is the chirality-exchange operator, and it is verified on the module.

The derivative shift integrates to a phase,
$$
R_\mu=R^0_\mu\exp\Bigl(-i\!\int\bigl(eA_\nu+mK_\nu\bigr)^*dx_\nu\Bigr),
\qquad
L_\mu=L^0_\mu\exp\Bigl(i\!\int\bigl(eA_\nu+mK_\nu\bigr)dx_\nu\Bigr),
$$
which depends on the path from a fixed initial point, and $K$ is form-invariant under the map: it is the same function of the mapped fields as of the original ones, so the map is invertible and the massless and massive solutions correspond one to one. This is the source's **non-integrable phase**: the mass is not a scalar multiplying $\bar\Psi\Psi$ but a unit complex vector, a direction in the complexified tangent space, and the phase it generates is path-dependent and is not removable by a gauge transformation of the s-vector. Its real part is the vector current and its imaginary part the axial current, so the phase and the "scale" of the spinor are the two halves of one complex vector.

The topological mass of the gauge field and the phase mass of the Dirac field are then the same object read in the two reductions: in both, the mass is a first-order coupling carried by a direction that the algebra supplies and that no gauge transformation removes.

## What the Equivalence Is and Is Not

**It is** a duality of the strong–weak type. The source's reason is that a duality typically exchanges the regimes, $g\mapsto1/g$, so a weak-coupling description in one variable is a strong-coupling description in the other, and having the explicit map makes perturbation theory available on both sides. No other article in the corpus states a dual equivalence of this kind; *The Proca Equation: Massive Spin 1 in Biquaternionic Form* is the second-order counterpart, not a dual, because there the mass is a scalar term and no elimination produces it.

**It is not** a new solution of either theory. The duality relates the *descriptions*, not the dynamics: a solution of the Dirac equation maps to a solution of the gauge equation and conversely, and no new physics follows from the map itself. What the duality supplies is a dictionary — Dirac mass to topological mass, Dirac current to field strength, Dirac chirality to the gauge dual pair — and a definition of the potential that makes no reference to a Bianchi identity.

**It is** classical. Both reductions are statements about actions and their variations; the source says "at least classically" and says nothing about the quantum theory.

## Open Questions

1. **The four-dimensional mass term.** In four dimensions the reduced Lagrangian carries the cubic form, not a Chern–Simons term; the Chern–Simons term appears only after the reduction to the spin manifold. The source's route to four dimensions is the promotion by the embedding vector $j$, so the four-dimensional topological mass is $j$-dependent. Whether there is a four-dimensional topological mass that does not single out a direction is open.

2. **The spectator scalar.** The scalar $\phi$ is carried through both reductions unchanged and, at $a=0$ on the spin manifold, does not interact with $B$. In four dimensions it is not a spectator: it sources the "electric" and "magnetic" currents of the Maxwell-like pair. Whether the three-dimensional decoupling is a property of the theory or of the gauge $a=0$ is not settled.

3. **The role of the triality.** The parent action is written in the s-vector variables, and the s-vector carries the triality (order-three ding) structure. Does the dual equivalence commute with the triality map $A\mapsto B\mapsto N\mapsto A$? If it does, the equivalence is triality-covariant, which would be a strong structural statement; if not, the triality breaks at the duality.

4. **The quantised equivalence.** A classical dual equivalence need not survive quantisation. Do the two reductions give the same anomaly, the same $\beta$ function, the same $S$-matrix? *Anomalies and Anomaly Cancellation in Biquaternionic Form* is the natural place to test it.

5. **The quantisation of the phase.** The source conjectures that single-valuedness of the non-integrable phase on a closed curve quantises the combination $bm$ carried by $K$, by analogy with Dirac's monopole argument. The conjecture is stated and not proved. Whether $K$ has a geometric meaning beyond the plane-wave case is the source's own open question.

These questions are open.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

$$
\gamma_0=iL_{e_t}R_{\vec e_x},\quad \gamma_1=iL_{\vec e_x}R_{\vec e_y},\quad \gamma_2=iL_{\vec e_y}R_{\vec e_y},\quad \gamma_3=iL_{\vec e_z}R_{\vec e_y},\quad \gamma_5=-iL_{e_t}R_{\vec e_z}.
$$

The four $\gamma_\mu$ are the generators $iC_\mu$ of the body, and $\gamma_5$ is the representative of the chirality cell $\Gamma$. They satisfy $\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4$ and $\{\gamma_5,\gamma_\mu\}=0$, the second being the same anticommutation that $\Gamma$ obeys as a cell: right multiplications by orthogonal units anticommute. The product of the four is the chirality,
$$
\gamma_0\gamma_1\gamma_2\gamma_3=-i\gamma_5 ,
$$
which is the cell identity $\Gamma=iC_0C_1C_2C_3$ read on the module.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module. The symbol $\Gamma$ is not a gamma matrix: $\Gamma$ is the chirality cell in the algebra and $\gamma_5$ is its representative on the reference frame. This is why no $\gamma$ symbol appears in the body of the article.

The squares are cells, and $i^2=-1$ does the sign:
$$
\gamma_0^2=i^2R_{\vec e_x^2}=(-1)(-1)I_4=I_4,
\qquad
\gamma_5^2=(-i)^2R_{\vec e_z^2}=(-1)(-1)I_4=I_4 .
$$

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

## Summary

The Dirac Lagrangian in the vector representation and the Lagrangian of the three-dimensional topologically massive gauge field are **dual**: one first-order parent action in the s-vector variables reduces, on one elimination, to the Dirac Lagrangian — first-order kinetic term in the $\check c$ structure constants, mass term $m(G^*G^*+GG)$ coupling the field to its conjugate — and, on the other elimination, to a second-order Lagrangian for the dual potential whose mass term is first order and bilinear in $m$. On the spin manifold orthogonal to $j$, at $a=0$, the latter reads
$$
\mathcal{L}_G=-\tfrac{1}{4m}\sum_{\mu,\lambda}\epsilon_\mu\epsilon_\lambda F_{\mu\lambda}F_{\mu\lambda}+\tfrac14\sum_{\mu,\nu,\lambda}\check\varepsilon_{\nu\mu\lambda}B^*_\nu F_{\mu\lambda},
$$
Maxwell plus a Chern–Simons mass, with $\check\varepsilon_{\nu\mu\lambda}=\sum_\rho\varepsilon_{\nu\mu\lambda\rho}j_\rho$ and the gauge equation $\sum_\nu\epsilon_\nu\,\partial F_{\nu\mu}/\partial x_\nu+\tfrac m2\sum_{\nu,\lambda}\epsilon_\nu\epsilon_\lambda\check\varepsilon_{\mu\nu\lambda}F^*_{\nu\lambda}=0$. The same $m$ is, in the other reduction, the non-integrable phase of the Dirac field: $\bar\Psi\Psi=\sum_\mu\epsilon_\mu K_\mu\bar\Psi iC_\mu\Psi$ with $K\cdot K=1$.

Three facts make the mechanism work. The first-order mass term changes only by a total derivative under the gauge freedom of the dual potential, which is what "topological" means here. The structure constants $t'$ are symmetric in the pair of indices that the antisymmetric field strength contracts, so they drop out and only the Levi-Civita part survives — verified — and the mass term is a Chern–Simons term. And the self-dual two-form $H_{\mu\nu}$ carries the same information as the s-vector, with $H_{[\mu\nu]}$ anti-self-dual and $H_{(\mu\nu)}=\phi^*g_{\mu\nu}$, so the auxiliary field of the reduction is the antisymmetric part of the biquaternion.

The parent actions and the eliminations are the source's; the algebraic identities they use were recomputed for this article and hold. The eliminations themselves were not recomputed, and no quantum statement is made.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C_\mu=L_{a_\mu}R_{b_\mu}$ | Bare cell of index $\mu$; $a_0=e_t$, $a_k=\vec e_k$, $b_0=\vec e_x$, $b_k=\vec e_y$; $C_\mu\Psi=a_\mu\Psi b_\mu$ |
| $iC_\mu$ | Generator cell; $\{iC_\mu,iC_\nu\}=2g_{\mu\nu}e_t$ |
| $\mathcal{D}(w)=\sum_\mu w_\mu\,iC_\mu$ | Contraction of the four generators with the components $w_\mu$ |
| $C_5=L_{e_t}R_{\vec e_z}$, $\Gamma=-iC_5$ | Chirality cell; $\Gamma=iC_0C_1C_2C_3$, not a gamma matrix |
| $g_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$ | Generator metric; not the $ict'$ metric of $\mathbb{M}_-$ |
| $\epsilon_\mu=g_{\mu\mu}$, $\epsilon=(1,-1,-1,-1)$ | Sign vector of the metric; distinct from $\varepsilon$ |
| $G_\mu$ | s-Vector (complex four-vector), the Dirac field in the vector representation |
| $H_\mu$ | Dual (potential) field of the four-dimensional parent action, complex four-vector |
| $B_\mu$ | Complex potential of the three-dimensional version, axial gauge $B_\mu j^\mu=0$ |
| $\phi$ | Complex scalar, $\phi=G_\mu j^\mu$; $G_\mu=G^\mu-j_\mu\phi$ with $G^\mu=p^+_{\mu\nu}G_\nu$ |
| $p^\pm_{\mu\nu}$ | Projectors; $p^+=g+jj$, $p^-=-jj$, $p^++p^-=g$ |
| $A_\mu$ | Electromagnetic four-potential; it enters only the covariant derivative |
| $B_\mu, N_\mu$ | Real four-vectors of the two semi-spinors, $G=B+iN$ |
| $k_\mu$, $j_\mu$ | Timelike and spacelike neutral vectors, units of $c$ and $\check c$ |
| $c_{\mu\nu\lambda}$, $\check c_{\mu\nu\lambda}$ | Structure constants on $k$ and on $j$; $\check c=(t'-i\varepsilon)j$ |
| $\check\varepsilon_{\nu\mu\lambda}=\sum_\rho\varepsilon_{\nu\mu\lambda\rho}j_\rho$ | Levi-Civita symbol of the $j$-slice |
| $H_{\mu\nu}=\sum_\lambda\epsilon_\lambda G^*_\lambda\check c_{\lambda\mu\nu}$ | Two-form of the s-vector; $H_{[\mu\nu]}$ anti-self-dual, $H_{(\mu\nu)}=\phi^*g_{\mu\nu}$ |
| $F_{\mu\nu}=\partial_\mu B_\nu-\partial_\nu B_\mu+iaj_\mu B^*_\nu-iaj_\nu B^*_\mu$ | Field strength of the dual potential |
| $\bar\Psi\Psi=\sum_\nu\epsilon_\nu(N_\nu N_\nu-B_\nu B_\nu)$ | Dirac bilinear |
| $K_\mu$ | Unit complex vector, $K\cdot K=1$; the mass as a non-integrable phase |
| $\varepsilon_{\mu\nu\lambda\rho}$ | Totally antisymmetric symbol, $\varepsilon_{0123}=1$ |
| $m$, $a$ | Fermion mass (equated to the topological gauge mass) and the auxiliary real constant $a\ne m$ |
| $S_{GH}$, $S_{G\phi B}$ | The two parent actions, four- and three-dimensional |
| $\mathcal{L}_D$, $\mathcal{L}_H$, $\mathcal{L}_{\phi B}$, $\mathcal{L}_G$ | Dirac, dual-potential, scalar-plus-potential and spin-manifold Lagrangians |

## Further Reading

- Liu Yu-Fen, "Triality and Dual Equivalence Between Dirac Field and Topologically Massive Gauge Field," arXiv:hep-th/0602275 (2006), for the parent actions (55) and (77), their eliminations, the self-dual field strength, the topological reading of the mass, and the non-integrable phase. **The eliminations are quoted; the algebraic identities they use are recomputed.**
- Liu Yu-Fen, "Triality, Biquaternion and Vector Representation of the Dirac Equation," arXiv:math-ph/0109008 (2001), for the s-vector representation, the bosonic Dirac Lagrangian, the self-dual form of the massive equation, and the bilinear dictionary on which the parent action is built.
- S. Deser and R. Jackiw, *Physics Letters B* **139** (1984) 371, for the parent (master) action method itself.
- S. Deser, R. Jackiw and S. Templeton, "Topologically massive gauge theories," *Annals of Physics* **140** (1982) 372, for the original topologically massive gauge theory in $2+1$ dimensions and its Chern–Simons mass.
- H. Weyl, "Elektron und Gravitation," *Zeitschrift für Physik* **56** (1929) 330, and C. N. Yang, "Integral formalism for gauge fields," *Physical Review Letters* **33** (1974) 445, for the non-integrable phase factor that the mass generalises.
- The companion corpus articles: [The s-Vector Representation of the Dirac Spinor in Biquaternionic Form](the-s-vector-representation-of-the-dirac-spinor-in-biquaternionic-form.html), [Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form](triality-and-the-ding-construction-for-the-dirac-spinor-in-biquaternionic-form.html), [The Proca Equation: Massive Spin 1 in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), [Anyons and Braid Statistics in Biquaternionic Form](anyons-and-braid-statistics-in-biquaternionic-form.html), and [Anomalies and Anomaly Cancellation in Biquaternionic Form](anomalies-and-anomaly-cancellation-in-biquaternionic-form.html).
