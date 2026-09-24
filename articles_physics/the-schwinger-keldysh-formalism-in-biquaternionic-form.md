# __The Schwinger–Keldysh Formalism in Biquaternionic Form__

## Introduction

The **Schwinger–Keldysh formalism** — the closed-time-path or *in-in* formalism — is the real-time functional-integral method for a quantum field in an arbitrary state, thermal or not. Its device is a contour in complex time that runs forward and then backward, so that every field is doubled into a **plus** branch and a **minus** branch, and the correlation functions become a $2\times2$ matrix indexed by the branch. A rotation in branch space (the **Keldysh rotation**) brings the matrix to a form in which its entries are the retarded, advanced, and Keldysh Green's functions, and the last of these carries the state's statistical information. It is the standard language of non-equilibrium field theory, and at equilibrium it is equivalent to the Matsubara formalism.

This article asks what the biquaternion algebra $\mathbb{B}$ contributes. The answer is a clarification and a set of transcriptions.

- **Established (framework): the branch doubling is not the algebra's doubling.** The biquaternion algebra is a complex algebra with a two-dimensional irreducible module and an isomorphism $\Phi:\mathbb{B}\to M_2(\mathbb{C})$; the closed-time-path construction also produces a two-dimensional structure, the branch space. These two "twos" are **different**. The branch index is external to $\mathbb{B}$: the CTP field space is $\mathbb{B}\otimes\mathbb{C}^2_{\mathrm{br}}$ (for a scalar) or a spinor module tensored with $\mathbb{C}^2_{\mathrm{br}}$, and the branch factor is not the algebra's $M_2(\mathbb{C})$. Identifying them would be a genuine error, and this article states the separation explicitly.
- **Established (algebra).** The Keldysh rotation is a real orthogonal transformation of the branch space,
$$
R=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
R\in O(2),\quad \det R=-1,\quad R^2=I_2 ,
$$
an element of $O(2)=U(1)\rtimes\mathbb{Z}_2$, and the $\mathbb{Z}_2$ is the exchange of the two branches — the reversal of the contour's orientation. In the rotated basis the $2\times2$ Green's function matrix takes the form
$$
\hat{\mathcal G} = \begin{pmatrix} G^K & G^R \\ G^A & 0\end{pmatrix},
$$
with the $qq$ entry **exactly zero**; this was verified by explicit rotation of a consistent CTP matrix and is a general algebraic identity, not an approximation.
- **Established (algebra).** At equilibrium the Keldysh component obeys the **fluctuation–dissipation relation**
$$
G^K(\omega) = \coth\frac{\beta\omega}{2}\,\big(G^R(\omega)-G^A(\omega)\big)
= \big(1+2n_{\mathrm B}(\omega)\big)\big(G^R(\omega)-G^A(\omega)\big),
$$
whose thermal factor is a **central scalar**, so it multiplies every entry of the module structure identically. For a scalar biquaternion field the whole CTP structure is therefore block diagonal with respect to the sector split, with the branch index external; for a spinor field the entries are matrix-valued and non-central.
- **Established (framework).** The equivalence with Matsubara is the standard equivalence, and the framework's reading is that the KMS analyticity strip — the compactified material direction — is what makes the equilibrium Keldysh function determined by the spectral function. Away from equilibrium the strip is absent and the Keldysh function is an independent datum.

The article proceeds as follows. A section fixes the contour and the doubled fields. A section separates the branch doubling from the algebra's doubling. A section gives the Keldysh rotation and the matrix of Green's functions, with the verification. A section treats the equilibrium relations and the fluctuation–dissipation theorem, a section the relation to Matsubara and the thermal states of the companion articles, and a section the non-equilibrium case. A section separates what is established from what is interpretation.

**Conventions.** We use those of the companion articles, in particular *The Matsubara Formalism in Biquaternionic Form*, *The KMS Condition and the Biquaternion Framework*, *The Unruh Effect in Biquaternionic Form*, and *Hawking Radiation in Biquaternionic Form*. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, central scalar imaginary $i$, and isomorphism $\Phi(e_k)=-i\sigma_k$. The sectors are $\mathbb{M}_-$ and $\mathbb{M}_+$; $\tilde X=ict\,e_0+\mathbf x$ is the material coordinate; $\tilde\nabla=e_0\partial_{ict}+e_k\partial_k$ and $\Box=\tilde\nabla\bar{\tilde\nabla}=\partial_{ict}^2+\Delta$; the $ict$ metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)$; the trace pairing is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$. The inverse temperature is $\beta=\hbar/(k_BT)$ and the Bose occupation number is $n_{\mathrm B}(\omega)=1/(e^{\beta\omega}-1)$. The branch index is written $\alpha,\beta\in\{+,-\}$ or, in the rotated basis, $\{cl,q\}$.

## The Closed-Time-Path Contour and the Doubled Fields

The formalism begins with a contour and produces a doubling; the doubling is what needs to be placed correctly with respect to the algebra.

**The contour.** The **closed-time path** $\mathcal{C}$ runs along the real time axis from $-\infty$ to $+\infty$ and then back from $+\infty$ to $-\infty$, with a possible excursion into the imaginary direction. Writing the two legs as $\mathcal{C}_+$ and $\mathcal{C}_-$, the field is defined on each leg separately:
$$
\tilde\Phi_+(t,\mathbf x) \equiv \tilde\Phi(t,\mathbf x)\big|_{t\in\mathcal{C}_+},
\qquad
\tilde\Phi_-(t,\mathbf x) \equiv \tilde\Phi(t,\mathbf x)\big|_{t\in\mathcal{C}_-}.
$$
The generating functional is
$$
Z[\tilde J_+,\tilde J_-] = \int\mathcal{D}\tilde\Phi_+\mathcal{D}\tilde\Phi_-\;e^{\,iS[\tilde\Phi_+]-iS[\tilde\Phi_-]+i\int(\tilde J_+\tilde\Phi_+-\tilde J_-\tilde\Phi_-)},
$$
with the relative sign between the two branches. The two-branch action is the difference of two copies of the ordinary action, and the minus branch is integrated with the opposite orientation, which is what makes the formalism genuinely *in-in*: the final state is summed over, not fixed. This is standard (Schwinger 1961; Keldysh 1964; Kadanoff–Baym; see the cited reviews) and is transcribed.

**The doubled Green's functions.** The basic objects are the branch-indexed two-point functions
$$
G^{\alpha\beta}(x,y) = -i\big\langle T_{\mathcal{C}}\,\tilde\Phi_\alpha(x)\,\tilde\Phi_\beta(y)\big\rangle ,
\qquad \alpha,\beta\in\{+,-\},
$$
whose components are the time-ordered ($G^{++}$), anti-time-ordered ($G^{--}$), and mixed ($G^{+-}$, $G^{-+}$) functions. They are not independent: they satisfy the sum rules
$$
G^{++}+G^{--} = G^{+-}+G^{-+} = G^K ,
\qquad
G^{++}-G^{+-}=G^R ,
\qquad
G^{+-}-G^{--}=G^A ,
$$
which define the Keldysh, retarded, and advanced functions. These identities are algebraic and are the skeleton of the whole formalism; they hold for biquaternion-valued fields as they stand, because they involve only the branch index.

**The two-branch action in the framework.** For the quadratic biquaternion action with central operator $\tilde K$ the two-branch action is $S[\tilde\Phi_+]-S[\tilde\Phi_-]$, and each branch's Gaussian is the one of the functional-integral article. The branch-space propagator matrix in the $(\Phi_+,\Phi_-)$ basis is therefore
$$
\hat G_0 = \begin{pmatrix} \tilde K^{-1} & 0 \\ 0 & -\tilde K^{-1}\end{pmatrix},
$$
block-diagonal, with the minus sign of the reversed branch. The Keldysh rotation of this matrix is not the equilibrium form $\left(\begin{smallmatrix}G^K&G^R\\G^A&0\end{smallmatrix}\right)$ — the free contour's matrix has no Keldysh component in the vacuum — and the equilibrium form appears only once the state is specified. Two structural points follow and are the framework's: the free propagator is central in each block, so the branch structure and the module structure are independently diagonal; and the sector decomposition of $\tilde K^{-1}$ multiplies each block, so a scalar biquaternion field's free CTP propagator is the standard one taken twice in the module and twice in the branch. The interactions couple the branches and the sectors; the vertex carries the relative sign of the two branches, which is what makes the loop integrals converge with the in-in boundary conditions rather than the Feynman ones.

## The Branch Doubling and the Algebra's Doubling

This is where a plausible-looking identification is wrong, and it is worth being explicit.

**The algebra's module is two-dimensional too.** The biquaternion algebra has a two-dimensional complex irreducible module $\mathbb{B}P_+(\hat{\boldsymbol\mu})\cong\mathbb{C}^2$, and the isomorphism $\Phi$ represents $\mathbb{B}$ by $2\times2$ complex matrices. Numerically, "two" appears in both structures.

**The branch factor is external.** The CTP field is a map from the contour pair to the field's own value space; the field's value space is the module (a two-dimensional complex space for a scalar, the spinor module for a spinor). Hence the doubled field space is a **tensor product**,
$$
\mathcal{V}_{\mathrm{CTP}} = \mathcal{V}_{\mathrm{field}}\otimes\mathbb{C}^2_{\mathrm{br}} ,
$$
with $\mathbb{C}^2_{\mathrm{br}}$ the branch space. Multiplying dimensions, a biquaternion scalar has $2\times2=4$ complex components per mode, a biquaternion spinor has more; and the branch factor is a bookkeeping index with no relation to the algebra's centre or to its minimal ideals.

**Why the identification would be wrong.** The branch space carries the two contour orientations; the algebra's $M_2(\mathbb{C})$ carries the left and right multiplication, the minimal left ideals, and the chirality structure. A rotation in branch space acts on $\mathbb{C}^2_{\mathrm{br}}$ and commutes with $\mathbb{B}$; a left or right multiplication by an element of $\mathbb{B}$ acts on the module and commutes with the branch index. The two actions commute, and no element of $\mathbb{B}$ is a branch rotation. Conflating them would produce a spurious identification of the Keldysh rotation with an algebra element and of the Keldysh component with a chirality component; the separation is the framework's contribution to this formalism.

**What the framework does supply.** The field's value space, its sector decomposition, and the material-direction imaginary time along which the contour may be deformed. The last is the link to the KMS structure; the first two are the module structure that each entry of the $2\times2$ matrix carries.

## The Keldysh Rotation and the Matrix of Green's Functions

The branch matrix is made physical by a rotation whose entries are the classical and quantum combinations of the doubled fields.

**The rotation.** Define the classical and quantum fields by
$$
\begin{pmatrix}\tilde\Phi_{cl}\\\tilde\Phi_q\end{pmatrix} = R\begin{pmatrix}\tilde\Phi_+\\\tilde\Phi_-\end{pmatrix},
\qquad
R=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}.
$$
The matrix $R$ is symmetric, orthogonal, and of determinant $-1$ and square $I_2$:
$$
R^T R = I_2 ,
\qquad
\det R = -1 ,
\qquad
R^2 = I_2 ,
$$
so $R\in O(2)$. The group $O(2)=U(1)\rtimes\mathbb{Z}_2$ is the group of the branch-space rotations, and its $\mathbb{Z}_2$ subgroup is the exchange of the two branches, i.e. the reversal of the contour's orientation. The same group governs the one-mode Bogoliubov transformations of the companion article on Bogoliubov transformations; the $\mathbb{Z}_2$ there is the particle–hole exchange, and here it is the branch exchange. That the two are the same $O(2)$ is a statement about the two-dimensional real orthogonal group, not an identification of the two physical operations.

**The rotated matrix.** Rotating the CTP matrix $\hat G=\left(\begin{smallmatrix}G^{++}&G^{+-}\\G^{-+}&G^{--}\end{smallmatrix}\right)$ by $R$, $\hat{\mathcal G}=R\,\hat G\,R^{T}$ (with $R^T=R$), and using the sum rules gives
$$
\hat{\mathcal G} = \begin{pmatrix} G^K & G^R \\ G^A & 0\end{pmatrix}.
$$
The $qq$ entry vanishes identically. **Verification.** With the consistent real set $G^{++}=2.5$, $G^{+-}=1$, $G^{-+}=3$, $G^{--}=1.5$ (so that $G^{++}+G^{--}=G^{+-}+G^{-+}=4$), the rotation gives
$$
\hat{\mathcal G} = \begin{pmatrix} 4 & 1.5 \\ -0.5 & 0\end{pmatrix},
\qquad
G^R=G^{++}-G^{+-}=1.5 ,
\qquad
G^A=G^{+-}-G^{--}=-0.5 ,
\qquad
G^K=4 ,
$$
with the $qq$ entry exactly $0$ (to machine precision) and the off-diagonal entries exactly $G^R$ and $G^A$. The two off-diagonal entries are transposes of each other in the matrix-valued (spinor) case, where they are not central; for a scalar biquaternion field they are central scalars.

**Biquaternion content.** Each entry of $\hat{\mathcal G}$ is a module object. For a scalar field the entries are central scalars times the identity on the module and the matrix is the standard one taken twice (the sector copies); for a spinor field the entries are $M_2$-valued in the spinor module and the matrix is not diagonal in the module index. The vanishing of the $qq$ entry is a branch-space fact and holds in both cases; the module structure multiplies it entrywise.

## Equilibrium and the Fluctuation–Dissipation Relation

At equilibrium the Keldysh component is not independent of the spectral structure, and the relation between them is where the thermal state enters.

**The relation.** In frequency space the retarded and advanced functions are the boundary values of one analytic function, $G^{R/A}(\omega)=G(\omega\pm i\epsilon)$, and their difference is $i$ times the spectral function,
$$
G^R(\omega)-G^A(\omega) = i\,A(\omega) ,
\qquad
A(\omega)\ \ge 0 .
$$
The Keldysh component at inverse temperature $\beta$ is
$$
G^K(\omega) = \coth\frac{\beta\omega}{2}\big(G^R(\omega)-G^A(\omega)\big)
= \big(1+2n_{\mathrm B}(\omega)\big)\big(G^R(\omega)-G^A(\omega)\big),
$$
the **fluctuation–dissipation relation**. **Verification.** With the model retarded and advanced functions $G^{R/A}(\omega)=1/(\omega-E\pm i\gamma)$, $E=1.1$, $\gamma=0.3$, $\beta=2$, the two forms of the coefficient — $\coth(\beta\omega/2)$ and $1+2n_{\mathrm B}(\omega)$ — agree identically, and both reproduce $G^K$ at $\omega=0.2,1.1,2.5$; the identity $\coth(\beta\omega/2)=1+2n_{\mathrm B}(\omega)$ was checked at several frequencies to machine precision.

**Centrality and the framework.** The thermal factor $\coth(\beta\omega/2)$ is a central scalar, so the fluctuation–dissipation relation multiplies every component of the module structure identically: the relation is diagonal in the module and in the sector index. Consequently, for a scalar biquaternion field the equilibrium CTP structure factorizes into the two sectors, and each sector carries the same thermal factor; for a spinor field the factor is still central but the difference $G^R-G^A$ is a matrix, and the relation is a matrix proportionality rather than a scalar one.

**Where the thermal factor comes from.** It comes from the state, not the algebra: the KMS condition at inverse temperature $\beta$ — the analyticity of $G$ in the strip $0<\mathrm{Im}\,t<\beta$ and the boundary relation $G(t+i\beta)=G(-t)$ — is what forces the coefficient to be $\coth(\beta\omega/2)$. The framework houses the strip as the complexified material direction; the value of $\beta$ is an input, exactly as in the Matsubara article.

## Relation to Matsubara and to the Thermal States

The two real-time formalisms are one at equilibrium, and the framework's version of the statement is the material-direction one.

**Equivalence at equilibrium.** At equilibrium the Keldysh function is determined by the spectral function and the thermal factor, and the Matsubara function is determined by the same data; the relation between them is the analytic continuation
$$
G(i\omega_n)\ \longleftrightarrow\ G^{R}(\omega)\ \longleftrightarrow\ G^K(\omega) ,
$$
the Matsubara function on the discrete grid, the retarded function on the real axis, and the Keldysh function through the fluctuation–dissipation relation. This equivalence is standard (Landsman–van Weert; Kadanoff–Baym) and is cited. The framework's reading is that the continuation is a movement within the complexified material time, and that the discrete grid and the real axis are the same analytic function sampled on the circle and on the cut respectively.

**The thermal states of the companions.** The Unruh and Hawking states are equilibrium states at $\beta=2\pi c/a$ and $\beta=2\pi c/\kappa$; their CTP description is the equilibrium one above, with the Keldysh component carrying the thermal factor and the retarded/advanced functions carrying the causal response. The framework adds no new ingredient: the imaginary material time is intrinsic, which is why the KMS strip has a preferred direction, and the temperature is the input that the Unruh and Hawking articles state it to be.

**Consistency with the KMS article.** The modular Hamiltonian $K=-\log\rho$ is a Hermitian element of $\mathbb{M}_+$ in the KMS article's finite-dimensional setting, and the Keldysh component is $\rho$-dependent through the thermal factor; for a Gibbs state $\rho=e^{-\beta H}/Z$ the two agree. The same caveat as in the Matsubara article applies: the field-algebra modular operator is not constructed in the framework, and the equilibrium CTP function is used as the standard one.

## The Non-Equilibrium Case

Away from equilibrium the Keldysh function is an independent dynamical object, and this is where the formalism earns its keep.

**Independence.** For a state that is not thermal there is no KMS strip and no fluctuation–dissipation relation; $G^K$ must be computed from the state's initial correlations and evolved, and the three functions $G^R$, $G^A$, $G^K$ (equivalently the four branch functions subject to the sum rules) are the dynamical data. The real-time in-in formalism is built for exactly this situation, and the framework's role is the same as at equilibrium: it supplies the module on which each entry is a value and the material direction in which the contour may be deformed, and it supplies nothing about the state.

**The contour deformation and the material direction.** The standard trick of deforming the contour into the imaginary direction is available because the framework's material time has an intrinsic imaginary part; the deformation picks up the state's initial correlations and is the route by which the thermal state is recovered as a special case. That the deformation is possible is the framework's statement that the material direction's complexification is available; the choice of deformation is the standard analytic choice, and the propagator article's caution applies — the algebra supplies the complex structure, not the contour.

**A caution on the spurious identification.** In a non-equilibrium setting the temptation to read the branch matrix as an algebra element is strongest, because both carry a two-valued structure and both appear in the same formula. The article's separation holds: the branch matrix is external, and the algebra acts on each entry. Keeping this straight is the difference between a correct doubling and a spurious one.

## The Kadanoff–Baym Equations

The dynamical content of the formalism is a matrix Dyson equation, and it is worth stating how the framework's objects enter it.

**The matrix Dyson equation.** With the free propagator matrix $\hat G_0$ and the self-energy matrix $\hat\Sigma$, the exact propagator obeys
$$
\hat G^{-1} = \hat G_0^{-1}-\hat\Sigma ,
\qquad\text{equivalently}\qquad
\hat G = \hat G_0+\hat G_0\,\hat\Sigma\,\hat G ,
$$
a $2\times2$ equation in branch space. In the rotated basis it splits into a retarded/advanced equation and a kinetic equation for the Keldysh component; the retarded equation fixes the spectral function $A$, and the kinetic equation for $G^K$ is the quantum Boltzmann equation, whose collision term is built from $\hat\Sigma$. At equilibrium the kinetic equation is satisfied by the fluctuation–dissipation form of $G^K$, and the fluctuation–dissipation relation is its solution rather than an independent input. This is the standard Kadanoff–Baym structure and is cited.

**Biquaternion content.** Each entry of $\hat G$ and $\hat\Sigma$ is a module object. When the self-energy is central the matrix Dyson equation is a set of scalar equations taken twice over the sectors; when it is not central — a spinor self-energy coupling chiralities — the entries are matrices in the spinor module and the products in the Dyson equation are module products, with the trace pairing supplying the scalar invariants. The branch index is external throughout, so the matrix structure and the module structure never mix: the Dyson equation is the tensor product of a $2\times2$ branch algebra with the module algebra, and the framework's contribution is the identification of the second factor.

**The kinetic limit.** Gradient-expanding the Dyson equation gives the semiclassical transport equation, in which the Keldysh component becomes the distribution function and the retarded one the spectral density. The framework adds to this its module-valued distribution function, whose sector decomposition is the two-species structure; the transport equation itself is standard.

## The Contour Generating Functional and the CTP Rules

The generating-functional structure of the previous articles carries over with the source doubled, and the perturbation theory is a set of rules on the contour.

**The contour generating functional.** Doubling the source,
$$
\tilde J = \begin{pmatrix}\tilde J_+\\\tilde J_-\end{pmatrix},
\qquad
Z[\tilde J_+,\tilde J_-] = \int\mathcal{D}\tilde\Phi_+\mathcal{D}\tilde\Phi_-\;e^{\,iS[\tilde\Phi_+]-iS[\tilde\Phi_-]+i\int(\tilde J_+\tilde\Phi_+-\tilde J_-\tilde\Phi_-)} ,
$$
one defines $W=-i\log Z$ and obtains the branch-indexed connected functions as its source derivatives; the Legendre transform in both sources gives the two-particle-irreducible effective action, whose stationarity is the Kadanoff–Baym equation. This is the contour version of *The Generating Functional and the Effective Action in Biquaternionic Form*, with the fields and sources taking values in the module and with one extra external index. The biquaternion content is unchanged: the sources are module-valued, the quadratic operator is the norm-form operator, and the sector factorization holds whenever the operator is central.

**The CTP Feynman rules.** Each internal line is the branch-indexed propagator $G^{\alpha\beta}$ (or its rotated form); each vertex carries the branch index of the contour leg on which it sits; each internal vertex is summed over the branches with the relative sign $+$ for the forward leg and $-$ for the backward leg; and the external legs carry the branch indices appropriate to the observable, which are $+$ and $-$ for an in-in matrix element and the rotated components for a physical response. The contour's closing is what enforces the in-in boundary condition, and it is a rule of the formalism and not of the algebra.

**The largest-time equation.** The invariance of the contour integral under a deformation of the contour leads to the largest-time equation, the relation among the branch functions that expresses causality; it is the statement that the $G^{\alpha\beta}$ are not independent but are tied by the contour's closure. The equation is standard and is cited; in the framework it is a relation among module-valued functions with a central thermal factor at equilibrium and no thermal factor away from it. The algebra contributes the value space and the sector decomposition, and nothing to the causal relation itself.

## What Is Established and What Is Interpretation

**Established (framework and algebra).**
- The CTP field space is the field module tensored with a branch space, $\mathcal{V}_{\mathrm{field}}\otimes\mathbb{C}^2_{\mathrm{br}}$; the branch index is external to $\mathbb{B}$, and it must not be identified with the algebra's $M_2(\mathbb{C})$ or with the material/informational decomposition.
- The Keldysh rotation is $R\in O(2)$ with $\det R=-1$, $R^2=I_2$; the rotated Green's function matrix is $\left(\begin{smallmatrix}G^K&G^R\\G^A&0\end{smallmatrix}\right)$ with the $qq$ entry exactly zero; verified on an explicit consistent CTP matrix.
- At equilibrium $G^K=\coth(\beta\omega/2)(G^R-G^A)=(1+2n_{\mathrm B})(G^R-G^A)$; verified for a model retarded function and several frequencies. The thermal factor is central and multiplies the module structure identically.

**Standard, and transcribed.**
- The closed-time-path construction, the two-branch action, the $2\times2$ Green's functions and their sum rules, the Keldysh rotation, the fluctuation–dissipation relation, the equivalence with the Matsubara formalism, and the non-equilibrium use.

**Interpretation.**
- Reading the contour deformation as a movement in the complexified material direction, and the KMS strip as its manifestation, is the framework's structural reading; it is consistent with the KMS, Matsubara, Unruh, and Hawking articles.

**Open.**
- The state is an input; the framework does not determine it, at equilibrium or away from it.
- The general modular operator of a field algebra is not constructed in the framework; the equilibrium CTP function is the standard one.
- The framework's statement that the branch doubling is external is a clarification of the formalism, not a new result; no independent derivation of the CTP construction is offered or claimed.

## Summary

The Schwinger–Keldysh formalism in biquaternionic form is the standard closed-time-path construction with the fields taking values in the algebra's module. The contour doubles every field into a plus and a minus branch, and the doubled field space is
$$
\mathcal{V}_{\mathrm{CTP}} = \mathcal{V}_{\mathrm{field}}\otimes\mathbb{C}^2_{\mathrm{br}} ,
$$
the branch factor being **external** to $\mathbb{B}$ and not to be identified with the algebra's own $M_2(\mathbb{C})$ or with the material/informational decomposition; this separation is the framework's clarification. The Keldysh rotation
$$
R=\frac{1}{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad R\in O(2),\ \det R=-1,\ R^2=I_2 ,
$$
brings the matrix of Green's functions to
$$
\hat{\mathcal G}=\begin{pmatrix}G^K&G^R\\G^A&0\end{pmatrix},
$$
with the $qq$ entry exactly zero; this was verified on the consistent set $G^{++}=2.5$, $G^{+-}=1$, $G^{-+}=3$, $G^{--}=1.5$, which gives $G^R=1.5$, $G^A=-0.5$, $G^K=4$, and the rotated matrix $\left(\begin{smallmatrix}4&1.5\\-0.5&0\end{smallmatrix}\right)$. At equilibrium the fluctuation–dissipation relation
$$
G^K(\omega)=\coth\frac{\beta\omega}{2}\big(G^R(\omega)-G^A(\omega)\big)=\big(1+2n_{\mathrm B}(\omega)\big)\big(G^R(\omega)-G^A(\omega)\big)
$$
was checked for a model retarded function at $\beta=2$ and several frequencies; its thermal factor is central and multiplies the module structure identically, so a scalar biquaternion field's equilibrium CTP structure is block diagonal with respect to the sector split rather than a doubling of independent fields. The equivalence with the Matsubara formalism, the thermal states of the Unruh and Hawking articles, and the non-equilibrium use are all standard and transcribed; the state and its temperature remain inputs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathcal{C}=\mathcal{C}_+\cup\mathcal{C}_-$ | Closed-time-path contour (forward then backward) |
| $\tilde\Phi_\pm$ | Field on the plus / minus branch |
| $\mathbb{C}^2_{\mathrm{br}}$, $\alpha,\beta\in\{+,-\}$ | Branch space and branch index (external to $\mathbb{B}$) |
| $\mathcal{V}_{\mathrm{CTP}}=\mathcal{V}_{\mathrm{field}}\otimes\mathbb{C}^2_{\mathrm{br}}$ | Doubled field space |
| $G^{\alpha\beta}=-i\langle T_{\mathcal{C}}\tilde\Phi_\alpha\tilde\Phi_\beta\rangle$ | Branch-indexed Green's functions |
| $G^{++},G^{--},G^{+-},G^{-+}$ | Time-ordered, anti-time-ordered, mixed functions |
| $G^K=G^{++}+G^{--}=G^{+-}+G^{-+}$ | Keldysh component |
| $G^R=G^{++}-G^{+-}$, $G^A=G^{+-}-G^{--}$ | Retarded and advanced functions |
| $R=\frac{1}{\sqrt2}\left(\begin{smallmatrix}1&1\\1&-1\end{smallmatrix}\right)\in O(2)$ | Keldysh rotation; $\det R=-1$, $R^2=I_2$ |
| $\tilde\Phi_{cl},\tilde\Phi_q$ | Classical / quantum components |
| $\hat{\mathcal G}=\left(\begin{smallmatrix}G^K&G^R\\G^A&0\end{smallmatrix}\right)$ | Rotated Green's-function matrix ($qq$ entry $0$) |
| $A(\omega)=G^R-G^A$ (times $-i$) | Spectral function, $A\ge0$ |
| $G^K=\coth(\beta\omega/2)(G^R-G^A)$ | Fluctuation–dissipation relation |
| $n_{\mathrm B}(\omega)=1/(e^{\beta\omega}-1)$ | Bose occupation number |
| $\beta=\hbar/(k_BT)$ | Inverse temperature (input) |

## Further Reading

- J. Schwinger, "Brownian motion of a quantum oscillator," *Journal of Mathematical Physics* **2** (1961) 407–432, for the closed-time-path formulation.
- L. V. Keldysh, "Diagram technique for nonequilibrium processes," *Soviet Physics JETP* **20** (1965) 1018–1026, for the contour and the rotated matrix of Green's functions.
- L. P. Kadanoff and G. Baym, *Quantum Statistical Mechanics* (Benjamin, 1962), for the real-time Green's functions and the fluctuation–dissipation relation.
- A. Kamenev, *Field Theory of Non-Equilibrium Systems* (Cambridge, 2011), for the Keldysh rotation, the $2\times2$ structure, and the non-equilibrium perturbation theory.
- J. Rammer and H. Smith, "Quantum field-theoretical methods in transport theory of metals," *Reviews of Modern Physics* **58** (1986) 323–359, for the rotated Green's functions and their sum rules.
- N. P. Landsman and C. G. van Weert, "Real- and imaginary-time field theory at finite temperature and density," *Physics Reports* **145** (1987) 141–249, for the equivalence with the Matsubara formalism.
- E. M. Lifshitz and L. P. Pitaevskii, *Statistical Physics, Part 2* (Pergamon, 1980), for the fluctuation–dissipation theorem and its thermal factor.
- R. Kubo, "The fluctuation–dissipation theorem," *Reports on Progress in Physics* **29** (1966) 255–284, for the general statement of the relation.
- M. Le Bellac, *Thermal Field Theory* (Cambridge, 1996), for the comparison of the real-time and imaginary-time formalisms.
- N. D. Birrell and P. C. W. Davies, *Quantum Fields in Curved Space* (Cambridge, 1982), for the real-time description of thermal states.
- Companion articles: *The Matsubara Formalism in Biquaternionic Form*, for the imaginary-time counterpart and the equivalence; *The KMS Condition and the Biquaternion Framework*, for the analyticity strip and the modular Hamiltonian; *The Unruh Effect in Biquaternionic Form* and *Hawking Radiation in Biquaternionic Form*, for the thermal states this formalism describes in real time; *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the module on which each entry of the matrix is valued; *The Feynman Propagator in Biquaternionic Form*, for the retarded/advanced boundary values and the contour caution.
