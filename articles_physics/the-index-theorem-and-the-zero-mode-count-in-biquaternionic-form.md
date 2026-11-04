# __The Index Theorem and the Zero-Mode Count in Biquaternionic Form__

## Introduction

The Hopf fibration of the companion article *The Hopf Fibration and the Biquaternion Gauge Bundle* supplied the geometric home of the gauge field and two integers: the winding of a map from the three-sphere, which is the instanton number, and the Chern number of a circle bundle over the two-sphere, which is the magnetic charge. This article supplies the tool that turns those integers into a *count*. The Atiyah–Singer index theorem states that the difference between the number of positive-chirality and negative-chirality zero modes of a Dirac operator is a topological integral, and in the gauge-theoretic setting that integral is the same density whose integral gave the instanton charge in *Instantons and Solitons in Biquaternionic Form*. The charge that classifies the field and the number of fermion zero modes that the field supports are therefore the same number up to the Dynkin index of the representation: the index is $2T(R)$ times the charge, and for the defining representation of $\mathrm{SU}(2)$, where $2T=1$, the two coincide.

The framework enters through three points, two of which are its own and one of which is not.

- **The operator is the framework's.** The Dirac operator in biquaternionic form is built from the biquaternionic gradient $\tilde\nabla=e_t\partial/\partial Q_t+\vec e_x\partial/\partial Q_x+\vec e_y\partial/\partial Q_y+\vec e_z\partial/\partial Q_z$ and its coupling to the connection, and its square returns the d'Alembertian: the framework's spinor module carries it, and *The Dirac Equation in Biquaternionic Form* and *The Spinor Module in Biquaternionic Form and Its Lorentz Action* fix it. The index is a property of that operator.
- **The counting is by the topological density, which the framework already has.** The index density is a total derivative whose integral is the instanton number, and the abelian form of the density is the framework's invariant $I_2=\vec E\cdot\vec B$. This was established in *Instantons and Solitons in Biquaternionic Form* and is not repeated here.
- **The trace is the matrix trace, and the framework's biquaternion norm does not supply it.** The non-abelian index density is $\mathrm{Tr}(F\wedge F)$ with the matrix trace on the gauge factor. The framework's quadratic invariant, the biquaternion norm $\langle\tilde F\rangle_{\natural}=\tilde F\tilde F^{\natural}$, is a rank-two bilinear of a *single* algebra element and has no second slot in which to trace two gauge-algebra-valued objects. This is the same rank-two limitation recorded for the topological density, and it controls what the framework can and cannot express about the index.

The article states the theorem as the standard result it is, derives the specialisations that the framework uses, and keeps the framework's own content apart from the standard content.

- Companion article *The Dirac Equation in Biquaternionic Form*, for the operator whose index is taken.
- Companion article *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, for the module and its chirality.
- Companion article *Instantons and Solitons in Biquaternionic Form*, for the topological background and its charge.
- Companion article *The Hopf Fibration and the Biquaternion Gauge Bundle*, for the abelian bundle and its charge.
- Companion article *The ADHM Construction and Biquaternion Instanton Data*, for the moduli whose dimension the adjoint index counts.
- Companion article *Clifford Modules and the Twisted Cauchy–Riemann Operator*, for the theorem in its mathematical form.

## The Dirac Operator and Its Index

**Notation, once.** The imaginary unit has $i^2=-1$, and it is the only imaginary unit in the article. Where two of them meet in a product they are reduced before the formula is read. A two-sided cell acts by $L_aR_b\psi=a\psi b$, and cells compose by $L_aR_bL_cR_d=L_{ac}R_{db}$, so

$$
(iL_aR_b)^2=i^2L_{a^2}R_{b^2}=-L_{a^2}R_{b^2},
$$

and with $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$ the two signs of the frame below follow from that one line. A product of four such cells carries $i^4=+1$ and no residual $i$. The representation label is $R$, written on $\mathcal D_R$, $T(R)$ and $\mathrm{Tr}_R$; the same letter with an element subscript, $R_b$, is the right multiplication, and the subscript is what distinguishes the two.

**Frame.** Displays are read in the $\mathbb{B}$ frame: the four coordinates $Q_\mu$ are complex, and the sign vector of the cells is $g_{\mu\nu}=\delta_{\mu\nu}$, the positive-definite one. The index is a property of an elliptic operator on a Riemannian manifold, and this is the frame whose flat slice is Euclidean.

**The four frame cells.** Write

$$
G_t:=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\qquad
G_x:=-L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
G_y:=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
G_z:=-L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}.
$$

On a field $\psi$ they act as $\psi\mapsto G_\mu\psi$: the time cell multiplies on the right by $i\,\vec e_x$, and each spatial cell multiplies on the left by $-\vec e_k$ and on the right by $\vec e_y$. Their squares and anticommutators are

$$
G_\mu^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad
\{G_\mu,G_\nu\}=2\delta_{\mu\nu}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

the first from $i^2=-1$ together with $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$, the second from $\vec e_j\vec e_k+\vec e_k\vec e_j=-2\delta_{jk}e_t$.

**The operator.** The twisted Dirac operator in the representation $R$ is

$$
\mathcal D_R=\sum_{\mu}G_\mu D_\mu,\qquad
D_\mu=\frac{\partial}{\partial Q_\mu}+i\kappa\,\mathcal A_\mu,
$$

with the sum over $\mu\in\{t,x,y,z\}$ and the connection $\mathcal A_\mu$ valued in the gauge algebra, multiplying the field from the left; and

$$
[D_\mu,D_\nu]=i\kappa\,F_{\mu\nu},\qquad
F_{\mu\nu}=\frac{\partial\mathcal A_\nu}{\partial Q_\mu}-\frac{\partial\mathcal A_\mu}{\partial Q_\nu}+i\kappa[\mathcal A_\mu,\mathcal A_\nu].
$$

The principal symbol at a covector $\xi$ is $\sum_\mu G_\mu\xi_\mu$, whose square is $\lvert\xi\rvert^2L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$; it is invertible for $\xi\neq0$, so the operator is elliptic, and on a closed manifold its kernel and cokernel are finite-dimensional. Its square is

$$
\mathcal D_R^2=\sum_\mu D_\mu^2+\frac{i\kappa}{2}\sum_{\mu,\nu}G_\mu G_\nu F_{\mu\nu},
$$

so where the field strength vanishes the second term is absent, and for the pure-gauge connection $\mathcal A_\mu=(i\kappa)^{-1}u^{-1}\partial u/\partial x_\mu$ the covariant derivative acts as $D_\mu\psi=u^{-1}\partial/\partial x_\mu(u\psi)$, so the operator is a conjugation of the free one: $\mathcal D_R=u^{-1}\bigl(\sum_\mu G_\mu\partial/\partial x_\mu\bigr)u$, whence

$$
\mathcal D_R^2=u^{-1}\,\Box\,u,\qquad
\Box=\frac{\partial^2}{\partial Q_t^2}+\Delta,\qquad
\Delta=\frac{\partial^2}{\partial Q_x^2}+\frac{\partial^2}{\partial Q_y^2}+\frac{\partial^2}{\partial Q_z^2}.
$$

The algebra element $\tilde\nabla=e_t\partial/\partial Q_t+\sum_k\vec e_k\partial/\partial Q_k$ satisfies $\tilde\nabla\tilde\nabla^{\natural}=\Box$ as well; the frame cells are chosen so that the operator has the same square, and the operator is the square root of the framework's d'Alembertian.

**The chirality.** The grading is the cell

$$
\chi:=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
$$

acting as $\psi\mapsto-i\psi\vec e_z$. The two signs in its square cancel — $i^2=-1$ and $\vec e_z^2=-e_t$ — and it is odd for the operator:

$$
\chi^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad
\{\chi,G_\mu\}=0,\qquad
[\chi,D_\mu]=0,\qquad
\chi\,\mathcal D_R=-\mathcal D_R\,\chi .
$$

The first three statements give the last: the grading carries only a right multiplication, so it commutes with every left multiplication, hence with the connection, while it anticommutes with each cell. Because $\chi$ is an involution the module splits, $M=M_+\oplus M_-$, and an odd operator has no diagonal blocks,

$$
\mathcal D_R=\begin{pmatrix}0&A\\ B&0\end{pmatrix},
\qquad
A:M_+\to M_-,
\qquad
B:M_-\to M_+,
\qquad
n_+=\dim\ker A,\quad n_-=\dim\ker B .
$$

For an elliptic operator $A$ the cokernel is the kernel of the formal adjoint, so the pair is the kernel count of a map and of its adjoint, and nothing forces the two dimensions to agree: that asymmetry is what the index measures.

**The two Dirac equations.** The framework's Dirac equation is not a single line, and the two lines are different operators. The first is the one-sided chiral pair, which is the definition,

$$
\begin{aligned}
\tilde\nabla\tilde\Psi_R&=m\tilde\Psi_L,\\
\tilde\nabla^{\natural}\tilde\Psi_L&=m\tilde\Psi_R,
\end{aligned}
$$

each member acting from the left, the mass coupling the two chiral halves. At $m=0$ the pair decouples into $\tilde\nabla\tilde\Psi_R=0$ and $\tilde\nabla^{\natural}\tilde\Psi_L=0$, one equation for each chirality.

The second is the two-sided form, in which the derivative acts from the left and the mass from the right through the chirality cell,

$$
\tilde\nabla^{\natural}F=m\,\bigl(-i\,\overline F\,\vec e_z\bigr),
$$

where $\overline\cdot$ is the coefficient conjugation. It is the same pair with the second field read as $-i\overline F\vec e_z$; it is antilinear in the mass term, and it is the form in which a right multiplication, not an off-diagonal pairing, carries the chirality coupling.

The third reading is the pair operator on the module, $\mathbb{D}$ in the notation of *Conventions of the Operators and the Calculus*,

$$
\mathbb{D}\Psi=\bigl(\tilde\nabla\Psi_R,\ \tilde\nabla^{\natural}\Psi_L\bigr),
\qquad
(\mathbb{D}-m)\Psi=0 .
$$

The mass is the off-diagonal pairing of the two halves, and it does not move the index: it is a zeroth-order term, and the index of an elliptic first-order operator is fixed by its symbol, which the mass leaves untouched. The index computed below is therefore the index of $\mathbb{D}$, and the four cells of the section above are that operator read in the frame, with the same four derivatives at the same order and the same square $\Box$.

**The index.** The index is the difference

$$
\mathrm{ind}\,\mathcal D_R=n_+-n_- ,
$$

an integer, and locally constant in the connection and in the metric; the two facts together make it a topological invariant, unchanged by any continuous deformation. It is the property of the operator that the rest of the article computes.

## The Atiyah–Singer Theorem

For a closed even-dimensional spin manifold $M$ and a twisted Dirac operator, the index is the integral of a characteristic class,

$$
\boxed{\;\mathrm{ind}\,\mathcal D_R \;=\; \int_M \hat A(TM)\wedge \mathrm{ch}(E_R)\;},
$$

where $\hat A(TM)$ is the $\hat A$-genus, the A-roof genus, of the tangent bundle and $\mathrm{ch}(E_R)$ is the Chern character of the twisting bundle. This is the Atiyah–Singer theorem; it is standard and is transcribed here, not derived. Its power in the gauge-theoretic setting is that the right-hand side is purely topological: it depends on the bundle data and not on the shape of the connection.

On the flat four-dimensional slice that the framework uses, the tangent bundle is trivial and the $\hat A$-genus reduces to $1$: $\hat A=1-\frac{p_1}{24}+\cdots$, and the Pontryagin class $p_1$ vanishes when the metric is flat. The index is therefore the degree-four part of the Chern character alone. With the trace in $R$ and the standard normalisation, that part is proportional to $\mathrm{Tr}_R(F\wedge F)$, with constant $\frac{1}{8\pi^2}$; the overall sign is carried by the orientation of $M$ together with the naming of the positive chirality, and both are fixed once here, so that

$$
\boxed{\;\mathrm{ind}\,\mathcal D_R \;=\; \frac{1}{8\pi^2}\int_{\mathbb R^4}\mathrm{Tr}_R\bigl(F\wedge F\bigr)
\;=\; 2\,T(R)\,Ϙ\;},
$$

where $T(R)$ is the Dynkin index of the representation, normalised so that the defining representation of $\mathrm{SU}(2)$ has $T=\tfrac12$, equivalently $\mathrm{Tr}(T_aT_b)=\tfrac12\delta_{ab}$ there, and $Ϙ$ is the integer topological charge of the companion article, defined with the trace in the defining representation. The two statements to read from this formula are that the index is proportional to the topological charge, and that its constant of proportionality is a representation-theoretic number.

**The Dynkin index.** For $\mathrm{SU}(2)$ the two representations that occur inside the framework are the defining module of dimension two and the adjoint representation of dimension three, and their indices are fixed by the Casimir relation $T(R)=\dim R\,C_2(R)/\dim G$, with $C_2(\text{defining})=\tfrac34$, $C_2(\text{adjoint})=2$ and $\dim G=3$:

$$
T(\text{defining})=\frac{2\cdot\tfrac34}{3}=\frac12 ,
\qquad
T(\text{adjoint})=\frac{3\cdot 2}{3}=2 .
$$

Both are computed from the same commutation relations $[T_a,T_b]=\varepsilon_{abc}T_c$ that define $\mathfrak{su}(2)\subset\mathbb M_-$ in *Non-Abelian Gauge Fields in Biquaternionic Form*, with $T_a=\tfrac12 \vec e_a$, so the group theory here is the framework's group theory. The index formula then reads

$$
\begin{aligned}
\mathrm{ind}\,\mathcal D_{\text{defining}}&=Ϙ,\\
\mathrm{ind}\,\mathcal D_{\text{adjoint}}&=4Ϙ.
\end{aligned}
$$

For a self-dual configuration of charge $Ϙ=k>0$ — the convention of the companion article, in which the self-dual unit instanton has $Ϙ=+1$ — all zero modes carry one chirality (the positive one in the convention fixed above): $n_+=k$, $n_-=0$ in the defining representation, and $n_+=4k$, $n_-=0$ in the adjoint. A single BPST instanton therefore supports one fermion zero mode in the doublet and four in the triplet.

**The abelian specialisation.** For the Hopf bundle over the two-sphere, the same theorem reduces to the two-dimensional statement

$$
\mathrm{ind}\,\mathcal D_n \;=\; \frac{1}{2\pi}\int_{S^2}F \;=\; n ,
$$

the Chern number of the bundle, which is $1$ for the Hopf bundle. Because the curvature of a $\mathrm{U}(1)$ bundle is a definite multiple of the area form, one of the two kernels is empty and the index is the total number of zero modes: the count is $\lvert n\rvert$, with the sign of $n$ naming the chirality that carries them. The two-sphere case is the simplest instance of the same counting: index equals topological charge, and the charge is a winding number of the algebra's group.

**Boundary corrections.** On a manifold with boundary the index acquires a boundary contribution, and the theorem is replaced by the Atiyah–Patodi–Singer form

$$
\mathrm{ind}\,\mathcal D_R \;=\; \int_M \hat A(TM)\wedge\mathrm{ch}(E_R) - \frac{h+\eta(0)}{2},
$$

where $h$ is the dimension of the space of boundary zero modes and $\eta(0)$ is the eta invariant of the boundary Dirac operator. The correction is a boundary term, and it is the reason a background with a nontrivial boundary can support zero modes whose count is not given by the bulk integral alone. The framework's instanton boundary is the three-sphere of *The Hopf Fibration and the Biquaternion Gauge Bundle*, and the eta invariant is a spectral invariant of the operator restricted to that boundary; its evaluation is a standard analytic computation and is not an algebraic statement about $\mathbb B$.

## The Density, the Charge, and the Total Derivative

The index is computed by the density $\mathrm{Tr}(F\wedge F)$, and the reason it is topological is that this density is a total derivative. The companion article established the chain

$$
\mathrm{Tr}\bigl(F\wedge F\bigr)=d\,\Omega_{\mathrm{CS}} ,
$$

with the Chern–Simons three-form

$$
\Omega_{\mathrm{CS}}=\mathrm{Tr}\Bigl(\mathcal A\wedge d\mathcal A+\tfrac23\,i\kappa\,\mathcal A\wedge\mathcal A\wedge\mathcal A\Bigr),
$$

and therefore

$$
Ϙ=\frac{1}{8\pi^2}\oint_{\partial\mathbb R^4}\Omega_{\mathrm{CS}} ,
$$

a surface integral over the three-sphere at infinity. The coefficient $\tfrac23 i\kappa$ is the one that makes the identity exact: the derivative of the cubic term contributes $3\cdot\tfrac23 i\kappa=2i\kappa$ times $\mathrm{Tr}(d\mathcal A\wedge\mathcal A\wedge\mathcal A)$, which is the cross term of $\mathrm{Tr}(F\wedge F)$, and the quartic term $\mathrm{Tr}(\mathcal A^4)$ vanishes — the trace is cyclic and the wedge is graded antisymmetric, so moving one of the four factors past the other three multiplies the term by the sign of a four-cycle, and that sign is $-1$. The index theorem's integral and the instanton's charge are therefore the same integral, computed in two ways: as the integral of the index density over the bulk, and as the Chern–Simons flux through the boundary. They agree in the defining representation, and differ by the Dynkin factor $2T(R)$ otherwise.

In the abelian case the density collapses to the framework's second invariant. Every index in these displays is written low and the four labels are summed explicitly. The alternating symbol is the orientation density: in the Lorentzian ordering $(Q_t,Q_x,Q_y,Q_z)$ it is fixed by $\epsilon_{0123}=+1$, and in the Euclidean ordering $(x_4,x_1,x_2,x_3)$ by $\epsilon_{4123}=+1$; no index is raised, so no metric sign enters it. With the components $F_{0k}=iE_k/c$ and $F_{jk}=\epsilon_{jkl}B_l$ in the Lorentzian case, and $F_{4k}=E_k$ and $F_{jk}=\epsilon_{jkl}B_l$ in the Euclidean one, the contraction reads

$$
\frac14\sum_{\mu,\nu,\rho,\sigma}\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
=
\begin{cases}
\dfrac{2i}{c}\,I_2 & (\text{Lorentzian}),\\[2mm]
2\,I_2 & (\text{Euclidean}),
\end{cases}
\qquad
I_2=\vec E\cdot\vec B ,
$$

so the abelian index density is the framework's own invariant $I_2$ up to a constant. This is the affirmative half of the story: for the abelian sector the index and the charge are written in the invariant calculus the framework already possesses.

## A Worked Case: the Abelian Index and the Charge-$n$ Zero Modes

The index formula is worth exercising in the framework's abelian sector, where every ingredient is the algebra's. Take the two-sphere with a $\mathrm{U}(1)$ gauge field whose first Chern number is $n$; the associated line bundle has $c_1=n$, and the Hopf bundle of *The Hopf Fibration and the Biquaternion Gauge Bundle* is the case $n=1$. The twisted Dirac index is

$$
\mathrm{ind}\,\mathcal D_n=\int_{S^2}\hat A(TS^2)\wedge\mathrm{ch}(L)=\int_{S^2}c_1(L)=n ,
$$

since the $\hat A$-genus of a surface is $1$. The count of zero modes is therefore $\lvert n\rvert$, with the sign of $n$ selecting the chirality, and for $n=1$ there is exactly one zero mode. This is the standard result that a charge-$n$ background binds one fermion mode per unit charge, and it is the abelian counterpart of the $n_+=k$ count in the defining representation.

The zero modes can be exhibited explicitly. In the $\mathrm{U}(1)$ patch with $a=\tfrac12(1-\cos\theta)d\phi$ of the Hopf article the two-component equation $\mathcal D\psi=0$ separates, and for $n>0$ the positive-chirality solutions are the monopole spinor harmonics of lowest angular momentum,

$$
\psi_n^{(m)}=f_n(\theta)\,\exp(im\phi),
\qquad
m=-j,\dots,j,
\qquad
j=\frac{n-1}{2},
$$

which number $2j+1=n$, matching the index; for $n=1$ the single mode is the constant section allowed in the patch where the connection is regular. The count is not the degeneracy of the scalar lowest Landau level in the same flux, which is $n+1$: the Dirac operator counts spinor harmonics, and the shift by one is the spin. What the framework supplies here is the identification of the bundle, its connection and the charged spinor with the Hopf data already computed; the counting itself is the standard one.

## The Index and the Instanton Moduli: $4k$ Adjoint Modes

The index of the adjoint Dirac operator has a second interpretation that ties this article to the instanton data. For a self-dual background of charge $k$ in the adjoint representation,

$$
n_+=4k ,
\qquad
n_-=0 ,
$$

and the framed moduli space of the background has real dimension $8k$. For $\mathrm{SU}(2)$ that space $\mathcal M_k$ is a smooth hyperkähler manifold of real dimension $8k$ and complex dimension $4k$ in each of its complex structures; the $4k$ adjoint zero modes of one chirality are counted as complex objects, so they match the complex dimension, while the $8k$ real collective coordinates are the tangent space. The index

$$
\mathrm{ind}\,\mathcal D_{\text{adjoint}}=4k=\tfrac12\dim_{\mathbb R}\mathcal M_k=\dim_{\mathbb C}\mathcal M_k
$$

is the precise form of this statement for $\mathrm{SU}(2)$.

Two consequences follow and are used in the later articles. First, the adjoint zero modes are the infinitesimal deformations of the background, so they are tangent to the moduli space: integrating over the moduli in the semiclassical expansion of *The Semiclassical Expansion and the Instanton Gas in Biquaternionic Form* is integrating over the collective coordinates, and the Grassmann integral over the zero modes fills that measure mode for mode. Second, the number of zero modes is a topological invariant and so cannot change under a deformation of the background within its charge sector. The standard bridge to the moduli counting of the ADHM construction of *The ADHM Construction and Biquaternion Instanton Data* is the quantum mechanics whose target is $\mathcal M_k$, whose index is the Euler characteristic of $\mathcal M_k$.

## The Biquaternion Reading and the Rank-Two Limitation

The framework's contribution to the index theorem is not the theorem but the identification of its ingredients. The operator is the four-cell operator $\mathcal D_R$ above, whose free part squares to $\Box$; the carrier is the algebra $\mathbb{B}$ read as a left module, $\mathbb{B}\cong S\oplus S$, and this is the Dirac module $\Delta=S\oplus\bar S$ of *The Spinor Module in Biquaternionic Form and Its Lorentz Action* read on the regular module, with $S\cong\mathbb{C}^2$ the unique simple module and the two chiral halves the two summands. The adjoint representation is the three-dimensional real subspace $\mathfrak{su}(2)=\mathrm{span}_{\mathbb R}\{\vec e_x,\vec e_y,\vec e_z\}\subset\mathbb M_-$ that the algebra carries as its own commutator algebra; and the group theory that produces the Dynkin indices is read directly from the quaternion commutators $[\vec e_a,\vec e_b]=2\varepsilon_{abc}\vec e_c$. The zero-mode counts $k$ and $4k$ are therefore a statement about the algebra's modules: the defining module gives one mode per unit charge, and the adjoint, being the algebra acting on itself, gives four.

What the framework does not supply is the *invariant* expression of the non-abelian index density. The density $\mathrm{Tr}(F\wedge F)$ requires the matrix trace over the gauge factor and the wedge of two algebra-valued two-forms, and the framework's biquaternion norm cannot produce it. The biquaternion norm pairs a single algebra element with its conjugate through the quaternion product and returns one scalar; it has one algebra slot. The index density needs two. This is the same rank-two limitation that the companion article found for the topological density and that the energy–momentum-tensor article found for the stress tensor: the framework's quadratic invariant is rank-two and single-slot, while the non-abelian index density is traced over a second algebra factor. The consequence is precise: the framework can write the index density in components with the matrix trace, and it can identify its integral as the topological charge, but the density is not an object of the biquaternion-norm invariant calculus. The zero-mode count is expressible; the invariant whose integral computes it, in the non-abelian case, is not one of the framework's invariants.

A second place where the count is imported is the fermion itself. The index theorem counts zero modes of a Dirac operator, and the operator presupposes a spinor field, a Clifford structure and the chirality grading; those are supplied by *The Spinor Module in Biquaternionic Form and Its Lorentz Action* and *Chiral Fermions in the Biquaternion Framework*, and the physical identification of the counted modes with fermionic states is standard quantum field theory. The relevant anomaly statement — that the divergence of the axial current is proportional to the same density — belongs to the spin-half programme of the corpus and is not derived here; the index theorem is its Euclidean, elliptic counterpart, and the two are related by the standard argument.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$.

In the $\mathbb{M}_-$ frame the four frame cells are

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
\gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

with $\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ and $\varepsilon=(1,-1,-1,-1)$. All four carry the same factor $i$, so the Lorentzian signs come from $i^2=-1$ together with $\vec e_k^2=-e_t$ alone. In the $\mathbb{B}$ frame, whose cells all square to $+e_t$, the four are

$$
\gamma_t[\mathbb{B}]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad
\gamma_x[\mathbb{B}]=-L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_y[\mathbb{B}]=-L_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad
\gamma_z[\mathbb{B}]=-L_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},
$$

In the axis-free display:

$$
\gamma_t[\mathbb{B}]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad
\gamma_x[\mathbb{B}]=-L_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_y[\mathbb{B}]=-L_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad
\gamma_z[\mathbb{B}]=-L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

and $\gamma_k[\mathbb{B}]=i\gamma_k[\mathbb{M}_-]$ for the three spatial directions. These four are the cells written $G_\mu$ in the body of the article.

The fifth is fixed by the four, $\gamma_5[\mathbb{M}_-]=i\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]\gamma_2[\mathbb{M}_-]\gamma_3[\mathbb{M}_-]$, so it is not a fifth direction. In the $\mathbb{M}_-$ frame it reads $\gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ and squares to $+L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$; in the $\mathbb{B}$ frame, $\gamma_5[\mathbb{B}]=-L_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, and it squares to $-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$. The grading used in the body is

$$
\chi=i\gamma_5[\mathbb{B}]=\gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}},
$$

The same identities in the axis-free display:

$$
\chi=i\gamma_5[\mathbb{B}]=\gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
$$

which squares to $+L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ and anticommutes with the four cells of either frame.

A single product is a pure tensor: writing $c(M)$ for the coefficient matrix of $M$ in the basis of the sixteen products, the products are exactly the elements with $\operatorname{rank}c(M)\le1$, a seven-dimensional cone, and a general element is a sum of at most four of them, with $\ell(M)=\operatorname{rank}c(M)$. Every sign in the products comes from $i^2=-1$ together with $\vec e_k^2=-e_t$: for one example, $\gamma_0[\mathbb{M}_-]\gamma_1[\mathbb{M}_-]=i^2L_{e_t\vec e_x}^{\mathrm{pau}}R_{\vec e_y\vec e_x}^{\mathrm{pau}}=-L_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y\vec e_x}^{\mathrm{pau}}$, where the minus sign is the square of the imaginary unit and the ordering of the right factors is the reverse of the cells'.

$\gamma_5[\mathbb{M}_-]$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi_{\mathrm{ad}}:=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$ — is a different object, represented on the Dirac module by $\gamma_5[\mathbb{M}_-]$, which is the cell $\chi$ above.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The index of the biquaternionic Dirac operator is the difference $n_+-n_-$ of the numbers of positive- and negative-chirality zero modes, and the Atiyah–Singer theorem computes it as the integral of the index density $\hat A(TM)\wedge\mathrm{ch}(E_R)$. On the flat four-dimensional slice the $\hat A$-genus is trivial and the index is $2T(R)Ϙ$, where $Ϙ$ is the instanton charge of *Instantons and Solitons in Biquaternionic Form* and $T(R)$ is the Dynkin index. For the framework's two representations the indices are $T(\text{defining})=\tfrac12$ and $T(\text{adjoint})=2$, so the counts are $n_+=k$ in the defining module and $n_+=4k$ in the adjoint, one zero mode and four for the unit self-dual instanton. The abelian specialisation on the two-sphere gives index equal to the charge, which is the Chern number $1$ of the Hopf bundle.

The index density is a total derivative whose integral equals the instanton charge, and in the abelian case it is the framework's invariant $I_2=\vec E\cdot\vec B$. The operator, its cells, its defining module, the adjoint representation and the group theory of the indices are all the algebra's; the theorem itself, the $\hat A$-genus, the boundary eta invariant and the identification of the counted modes with physical fermions are standard results transcribed. The one place where the framework is silent is the invariant form of the non-abelian density: it is computable in components with the matrix trace, but it is not an object of the biquaternion-norm invariant calculus, because that calculus is rank-two and single-slot while the density is traced over a second algebra factor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$ | Biquaternion algebra, $\cong M_2(\mathbb C)$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$, $\vec e_x \vec e_y=\vec e_z$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb M_+,\mathbb M_-$ | Informational (Hermitian) and material (anti-Hermitian) sectors |
| $\mathfrak{su}(2)=\mathrm{span}_{\mathbb R}\{\vec e_x,\vec e_y,\vec e_z\}$ | Compact gauge algebra inside $\mathbb M_-$ |
| $T_a=\tfrac12 \vec e_a$, $[T_a,T_b]=\varepsilon_{abc}T_c$ | Normalised generators |
| $\tilde\nabla=e_t\partial/\partial Q_t+\vec e_x\partial/\partial Q_x+\vec e_y\partial/\partial Q_y+\vec e_z\partial/\partial Q_z$ | Biquaternionic gradient; its free part is the Dirac operator |
| $\Box=\tilde\nabla\tilde\nabla^{\natural}=\partial^2/\partial Q_t^2+\Delta$ | d'Alembertian (B frame) |
| $\Delta=\partial^2/\partial Q_x^2+\partial^2/\partial Q_y^2+\partial^2/\partial Q_z^2$ | Laplacian in the three vector coordinates |
| $L_aR_b$, $L_aR_b\psi=a\psi b$ | Two-sided cell; $L_aR_bL_cR_d=L_{ac}R_{db}$ |
| $G_t=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$, $G_k=-L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | The four frame cells; $G_\mu^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, $\{G_\mu,G_\nu\}=2\delta_{\mu\nu}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $\mathcal D_R=\sum_\mu G_\mu D_\mu$ | Twisted Dirac operator in the representation $R$, in frame cells |
| $D_\mu=\partial/\partial Q_\mu+i\kappa\,\mathcal A_\mu$ | Covariant derivative; $[D_\mu,D_\nu]=i\kappa F_{\mu\nu}$ |
| $\chi=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$ | Chirality; $\psi\mapsto-i\psi\vec e_z$, $\chi^2=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $n_\pm$ | Dimensions of the positive/negative chirality zero-mode spaces |
| $\mathrm{ind}\,\mathcal D_R=n_+-n_-$ | Index of the Dirac operator |
| $\hat A(TM)\wedge\mathrm{ch}(E_R)$ | Index density; $\hat A=1$ on the flat slice |
| $T(R)$ | Dynkin index; $T(\text{defining})=\tfrac12$, $T(\text{adjoint})=2$ |
| $R$ | Representation label, defining (dim $2$) or adjoint (dim $3$); the right multiplication is $R_b$, distinguished by its element subscript |
| $\kappa$ | Coupling constant of the gauge field |
| $\mathcal F=d\mathcal A+i\kappa\,\mathcal A\wedge\mathcal A$ | Field-strength two-form |
| $F_{\mu\nu}=\partial/\partial Q_\mu\,\mathcal A_\nu-\partial/\partial Q_\nu\,\mathcal A_\mu+i\kappa[\mathcal A_\mu,\mathcal A_\nu]$ | Its components; $[D_\mu,D_\nu]=i\kappa F_{\mu\nu}$ |
| $Ϙ=\frac{1}{8\pi^2}\int\mathrm{Tr}(F\wedge F)$ | Topological (instanton) charge, $Ϙ\in\mathbb Z$; the trace in the defining representation |
| $\Omega_{\mathrm{CS}}$ | Chern–Simons three-form; $d\Omega_{\mathrm{CS}}=\mathrm{Tr}(F\wedge F)$ |
| $\eta(0)$, $h$ | Eta invariant and boundary zero-mode count (APS) |
| $I_2=\vec E\cdot\vec B$ | Framework's second invariant; index density in the abelian case |
| $\epsilon_{\mu\nu\rho\sigma}$ | Alternating symbol, orientation density, written all-low; $\epsilon_{0123}=+1$ Lorentzian, $\epsilon_{4123}=+1$ Euclidean |
| $\langle\tilde F\rangle_{\natural}=\tilde F\tilde F^{\natural}$ | Biquaternion norm; rank-two, single-slot, does not supply $\mathrm{Tr}(F\wedge F)$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators I", *Annals of Mathematics* 87 (1968) 484–530, for the index theorem and the index density.
- Michael F. Atiyah, Vijay K. Patodi and Isadore M. Singer, "Spectral asymmetry and Riemannian geometry I", *Mathematical Proceedings of the Cambridge Philosophical Society* 77 (1975) 43–69, for the index theorem with boundary and the eta invariant.
- Michael F. Atiyah, Nigel J. Hitchin and Isadore M. Singer, "Self-duality in four-dimensional Riemannian geometry", *Proceedings of the Royal Society A* 362 (1978) 425–461, for the instanton zero modes and the dimension formula.
- Thomas Eguchi, Peter B. Gilkey and Andrew J. Hanson, "Gravitation, gauge theories and differential geometry", *Physics Reports* 66 (1980) 213–393, for the index density, the Chern character and the eta invariant in a physics setting.
- Arthur L. Besse, *Einstein Manifolds* (Springer, 1987), for the A-roof genus and the differential-geometric background.
- Michael F. Atiyah, *Geometry of Yang–Mills Fields* (Accademia Nazionale dei Lincei, 1979), for the index theorem in the gauge-theoretic form used here.
- Roman Jackiw and Claudio Rebbi, "Solitons with fermion number $1/2$", *Physical Review D* 13 (1976) 3398–3409, for the fermion number of the instanton zero modes.
- Gerard 't Hooft, "Symmetry breaking through Bell–Jackiw anomalies", *Physical Review Letters* 37 (1976) 8–11, for the anomalous divergence and the zero-mode count.
- Mikio Nakahara, *Geometry, Topology and Physics* (CRC Press, 2nd ed. 2003), for the index theorem and the Chern–Weil construction in a form suited to the present notation.
- Raoul Bott and Loring W. Tu, *Differential Forms in Algebraic Topology* (Springer, 1982), for the Chern character and the characteristic-class calculus used throughout.
