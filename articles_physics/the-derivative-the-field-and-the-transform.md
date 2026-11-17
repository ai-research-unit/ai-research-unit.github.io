# __The Derivative, the Field and the Transform__

## Introduction

**This entry reads the analysis block of the mathematical category.** Ten articles, one construction.

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial R_\mu},
\qquad
\Box=\tilde\nabla\tilde\nabla^{\natural}
=e_t\frac{\partial^2}{\partial R_t^2}+\Delta_Q ,
\qquad
\tilde\Xi:\Omega\subseteq\mathbb{B}\longrightarrow\mathbb{B}.
$$

**The first claim is that the derivative of this algebra is an element and not a limit.** The quotient definition fails twice, on non-commutativity and on the zero divisors, and the operator definition survives both because it takes no inverse. What is left is a single element $\tilde\nabla$ whose four coefficients are the four coordinate derivatives: the derivative is an element of the same algebra as the field it differentiates, and it acts by multiplication. That is the whole reason the section exists, and it is also the reason the section after it was the operators.

**The second claim is that the square of that element is the wave operator, and the square is where the physics lives.** $\Box$ is the d'Alembertian on the material sector, the Laplacian on the quaternion subspace, and the same operator with one sign moved on the informational sector. The sign is not a convention of the analyst. It is the sector, and the four sectors give four sign patterns, of which two are elliptic and two are hyperbolic.

**The third claim is that regularity is not an extra condition imposed on a field.** $\tilde\nabla\tilde\Xi=0$ is the statement that the field is a differentiable function of the algebra's variable in the algebra's own sense. Written in components it is four equations — one scalar and one vector, each with its divergence or its curl — and on the material sector those four are the free Maxwell pair. The field equation is therefore not transcribed from anywhere: it is the differentiability condition of one function of one variable, and the transcription of Maxwell into the algebra and the derivation of Maxwell from the algebra meet at the same four equations.

**The fourth claim is that the second definition of the derivative gives a different equation on a different cone.** The two-sided condition $dF=L\,dZ\,R$ takes no inverse either, but it is quadratic in the first derivatives and its solution set is not a vector space. It says that every component's gradient is a zero divisor, that is, that the gradient lies on the light cone. The two conditions have the same characteristic set and neither contains the other, and the second is the primary equation of the algebrodynamical programme.

**The fifth claim is that the only place a source can enter is the integral.** The homogeneous condition has an infinite-dimensional space of solutions and no scale. The integral supplies both: the fundamental solution $G_{\mathrm{fn}}=\tilde R^{\natural}/\|\tilde R\|^{4}$ is the kernel, its distributional gradient is a delta, and the Cauchy formula turns a field into boundary data plus the integral of its own failure to be regular. A regular field is fixed by its boundary; the interior has no freedom left, and the residue of the kernel is the only place where strength is counted.

**The sixth claim is the reading, and it is stated here so that it can be judged against the mathematics.** Six words, one object each. The derivative is the field equation. The first-order root is the propagation. The regular function is the on-shell field. The Fueter extension is the axial completion. The integral is the action. The exponential is the flow. Each of the six is a statement about the same operator read at a different order, on a different sector, or through a different construction, and each is developed as an interpretation below rather than asserted here.

**The strongest objection is that this is Clifford analysis with new letters.** It is, on the quaternion subspace: $\mathbb{B}_{H}$ is the even subalgebra of $\mathrm{Cl}_{0,3}$ and $\mathbb{B}$ the even subalgebra of $\mathrm{Cl}_{1,3}$, the gradient is the Cauchy–Riemann–Fueter operator, and the Cauchy kernel, the mean value property, the maximum principle, Liouville's theorem and the Fueter construction are the classical theorems. The answer is not that the theorems are new. It is that the classical theory is stated on one algebra with one sign pattern, while the corpus's object has four real forms of four different inertias cut out of one complex algebra by one conjugation, and the four restrictions of one operator are the content of §*The Four Sign Patterns*. The classical theory is the $\mathbb{B}_{H}$ row of that table.

**A second objection is that the six readings are metaphors and predict nothing.** They are metaphors in the sense that any physical vocabulary is: the word *field* does not appear in the algebra. They are not metaphors in the sense that matters, because each names a specific algebraic object and a specific failure. The light cone is the zero-divisor cone, which is a set. The mass is a shift whose square is the negative of the parameter, which is an equation. The on-shell condition is a linear equation whose solutions are a module, which is a computation. What the entry does not do is select a dynamics, and that limit is stated in §*The Limits*.

**A third objection is that the direction of explanation is backwards.** Physics is written with field equations and then finds operators; the entry finds an operator and then reads equations off it. The answer is that both directions occur in the corpus and they are not the same claim. Maxwell and the Dirac equation are transcribed, with the algebra adding a reading and a constraint. The free Maxwell pair, the Helmholtz equation, the chiral pair and the eikonal arise from the two differentiability conditions, with nothing transcribed. The first route assumes the dynamics; the second produces it and must then explain why it produced this one. §*The Regular Field* keeps the two apart.

**A fourth objection is that Fueter's construction needs an axis, and on this algebra an axis is not canonical.** That is correct and it is the sharpest limit of the section. On $\mathbb{B}_{H}$ the roots of $-1$ form a two-sphere and the axial construction is axis-free. On $\mathbb{B}$ the roots of $-1$ form a three-parameter family that is not a sphere, so the slice must be chosen, one root at a time. The construction is therefore a family indexed by a root, exactly as the minimal left ideals are a family indexed by an axis, and the corpus states the dependence instead of hiding it.

**The letters.** The variable is $\tilde R=\sum_\mu R_\mu e_\mu$ with $R_\mu=r_\mu+ir'_\mu$, and on a four-dimensional subspace the coefficients are real or purely imaginary and the derivative with respect to them is an ordinary real derivative. The field is $\tilde\Xi$, a biquaternion-valued function of $\tilde R$. The gradient is $\tilde\nabla$, its quaternion conjugate $\tilde\nabla^{\natural}$, and the d'Alembertian $\Box$. The fundamental solution is $G_{\mathrm{fn}}$, and the Cauchy kernel is the same object read as a kernel. The two semi-derivatives of the two-sided condition are $L$ and $R$, and the coefficient function of a solution is $\Sigma$. The sector subscripts are $\Phi$ for the anti-Hermitian, material half and $\Psi$ for the Hermitian, informational half; the subspace subscripts are $H$ for the quaternion and $iH$ for the anti-quaternion subspace. The conventions are *Operator and Calculus Conventions*, and this entry uses them and defines none of them.

**Boundaries.** The algebra and its conjugations are *The Element, the Six Subspaces and the Two Ledgers*; the operators are *The Operators of the Algebra*; the cone is *The Zero Divisors and the Invertibles* and *The Topology of the Zero-Divisor Cone*; the topology of the group of invertibles is *The Group of Invertibles, the Cone and the Orders*; the transform theory proper is the next section, *The Harmonic Analysis: The Transform as a Change of Description*. The physical reading of the two-sided derivative is the companion *The Differentiable Field: One Primary Equation and the Linear Sector of the Biquaternion Universe*, and the external programme it records is *The Algebrodynamical Programme*. No dynamics, no action principle and no quantum postulate appear.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the metric structure of $\mathbb{B}$, limits and continuity, the two obstructions to differentiability, functions on a four-dimensional subspace, the gradient and its conjugate, the d'Alembertian and the convective derivative, the relation to Fueter and Clifford analysis | [Biquaternion Analysis](../articles_maths/biquaternion-analysis.html) |
| the d'Alembertian as the norm of the gradient, the two senses of a first-order root, the Clifford relation, the minimal carrier $\mathbb{C}^{4}$, the three generators inside $\mathbb{B}$, the regular module and the two-sided generators, the unshifted and the shifted root, $\det\mathsf D_\lambda=(\Box-\lambda)^2$ | [The First-Order Root of the Biquaternion D'Alembertian](../articles_maths/the-first-order-root-of-the-biquaternion-d-alembertian.html) |
| regularity as single-plane holomorphy against hypercomplex regularity, the system of regularity equations, examples, harmonicity, the Cauchy formula where it holds, the shifted operator and its three branches, the splitting of the Helmholtz null set by the differential projectors | [Biquaternion Regular Functions](../articles_maths/biquaternion-regular-functions.html) |
| the three definitions of the derivative, the rank-one criterion, the identity $\det\mathsf D\Sigma=\tfrac14N(\nabla\Sigma)$, the complex eikonal, the general solution through one twistor coordinate, the linear sector | [The Two-Sided Derivative over the Biquaternion Algebra](../articles_maths/the-two-sided-derivative-over-the-biquaternion-algebra.html) |
| the Fueter operator and its conjugate, the factorisation of the Laplacian, the componentwise system, harmonicity and the mean value, the axial extension and the affine kernel, the Fueter–Sce theorem, the power series and the Fischer decomposition | [Fueter Theory for Biquaternions](../articles_maths/fueter-theory-for-biquaternions.html) |
| the integral, its linearity and additivity, integration by parts, the divergence theorem, the Green formulas, the fundamental solution and the representation formula, the Cauchy integral formula, the mean value property, the maximum principle, Liouville, the identity theorem, the residue theorem | [Biquaternion Integration](../articles_maths/biquaternion-integration.html) |
| the two questions, the six subspaces in one table, the restriction of $\Box$ as the operator of the norm, the elliptic and the hyperbolic type, the null sets | [Remarkable Subspaces and the Analysis](../articles_maths/remarkable-subspaces-and-the-analysis.html) |
| the group of invertibles, the exponential and its closed form, the group law, the failure of surjectivity, the subgroups and the real forms, the $\mathrm{U}(2)$ decomposition, the Killing form, the enlarged carrier and the closed forms for $\mathrm{SU}(3)$ and $\mathrm{SU}(4)$ | [Biquaternion Lie Group and Exponential Structure](../articles_maths/biquaternion-lie-group-and-exponential-structure.html) |
| the exponential, the logarithm with its branch lattice, the powers and roots, the trigonometric and hyperbolic functions, the relations to the neighbouring cases | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |
| the Bessel functions, the orthogonal polynomials, the hypergeometric function, the gamma and zeta functions, and the Cauchy, Poisson and Green kernels that arise from the analysis | [Biquaternion Higher Special Functions](../articles_maths/biquaternion-higher-special-functions.html) |

**The first and the sixth rows own the section.** The first defines the operator and the sixth defines the integral; the second to the fifth are two readings of the first-order condition and two extensions of it; the last four are the finite-dimensional constructions that the operator meets.

## The Results in Brief

**The derivative.** $\tilde\nabla=\sum_\mu e_\mu\partial/\partial R_\mu$ is the one element-valued derivative. The quotient definition reduces to the affine maps, and the operator definition has an infinite-dimensional solution space. The derivative is a sum of left multiplications by the four units, so it is one of the operators of the preceding section used on a field.

**The characteristic set.** The symbol of the gradient is $S(\xi)=\sum_\mu\xi_\mu\mathsf M_2(e_\mu)$, and $\det S(\xi)=\sum_\mu\xi_\mu^{2}=N(\xi)$. The characteristic set is the zero-divisor cone, so the operator is elliptic at a real covector exactly when the covector is not null.

**The root.** $\Box=\tilde\nabla\tilde\nabla^{\natural}$ has no first-order root by left multiplication alone. The root exists in the operator algebra of the regular module, $\mathsf D^{2}=\Box I$, and a shift by the pseudoscalar gives $\mathsf D_\lambda=\mathsf D+c\gamma_5$ with $c^{2}=-\lambda$ and $\det\mathsf D_\lambda=(\Box-\lambda)^{2}$.

**The regular field.** $\tilde\nabla\tilde\Xi=0$ is four equations in the four components. Left and right regularity differ only in the sign of the curl term. Every regular field is harmonic, hence real-analytic, and satisfies the mean value property.

**The two-sided condition.** $dF=L\,dZ\,R$ is equivalent, componentwise, to the rank of the two-by-two array of coordinate derivatives being at most one, and the determinant of that array is $\tfrac14N(\nabla\Sigma)$. The condition is the eikonal, it is quadratic, and its solution set is not a vector space.

**Fueter.** $\Delta_4$ of the axial extension of a holomorphic function of one complex variable is both left- and right-regular. The map is injective modulo the affine functions, and the Fueter–Sce generalisation requires the odd dimension.

**The integral.** The fundamental solution is $G_{\mathrm{fn}}(\tilde R)=\tilde R^{\natural}/\|\tilde R\|^{4}$, homogeneous of degree $-3$, with $\tilde\nabla G_{\mathrm{fn}}=2\pi^{2}\delta_0e_t$ distributionally. The Cauchy formula holds on $\mathbb{B}_{H}$, and its consequences are the mean value property, the maximum principle, Liouville's theorem, the identity theorem, the Cauchy estimates and a residue theorem.

**The sign patterns.** $\Box$ restricted to a remarkable subspace is $e_t$ times the operator of the norm of that subspace: $\Delta_4$ of inertia $(4,0)$ on $\mathbb{B}_{H}$, $-\Delta_4$ of inertia $(0,4)$ on $\mathbb{B}_{iH}$, and the wave operator of inertia $(1,3)$ on $\mathbb{B}_{\Psi}$ and $(3,1)$ on $\mathbb{B}_{\Phi}$. The operator is elliptic exactly on the subspaces that contain no zero divisor.

**The group.** $\mathbb{B}^{\times}$ is a real Lie group of dimension eight, $\mathbb{B}^{\times}_1$ of dimension six, and $S^{3}$ of dimension three. The exponential is a local diffeomorphism at the identity and is not surjective onto $\mathbb{B}^{\times}_1$. The Killing form has inertia $(3,3)$ and radical the centre.

**The functions.** Every direct elementary function of $\tilde Q$ lies in $\mathbb{C}[\tilde Q]$, with two regimes set by the complex norm of the vector part: the oscillatory regime with two eigenvalues, and the nilpotent regime where every series truncates. The identities of one variable survive; the addition formulas of two variables fail.

## The Derivative Is an Element

**The quotient fails, and the failure is the definition.** For a commutative algebra with division, differentiability is $dF=H\,dR$, and $H$ is the derivative. For $\mathbb{B}$ the equation cannot be solved for $H$: $dR$ may be a zero divisor, so no inverse exists, and even where it exists, $H$ depends on the side on which it is written. The quotient definition, carried through, admits only the affine maps.

**What survives is the operator.** Write

$$
\tilde\nabla\tilde\Xi=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial\tilde\Xi}{\partial R_\mu},
$$

an element of $\mathbb{B}$ obtained from four derivatives of the field and the four units. No inverse is taken, no division occurs, and a zero divisor in the field or in the derivative is harmless. The price is that the construction is not the unique derivative of the function: it is one of several first-order conditions that an element-valued function can satisfy, and the others are the subject of §*The Two-Sided Derivative and the Eikonal*.

**It is linear, and it is left multiplication.** For central $\alpha,\beta$ and differentiable fields, $\tilde\nabla(\alpha\tilde\Xi+\beta\tilde\Upsilon)=\alpha\tilde\nabla\tilde\Xi+\beta\tilde\nabla\tilde\Upsilon$, and the derivative is the sum of four left multiplications, one per coordinate,

$$
\tilde\nabla\tilde\Xi=\sum_\mu L_{e_\mu}\bigl(\partial_\mu\tilde\Xi\bigr).
$$

So the analysis of this section is a chapter of the operator section that precedes it: the same left multiplication, applied to a field instead of to an element, with the parameter replaced by a derivative.

**The symbol, and the cone.** Replace $\partial/\partial R_\mu$ by a covector $\xi_\mu$ and the gradient becomes the two-by-two matrix

$$
S(\xi)=\sum_{\mu}\xi_\mu\mathsf M_2(e_\mu),
\qquad
\det S(\xi)=\sum_{\mu}\xi_\mu^{2}=N(\xi).
$$

The determinant of the symbol is the norm of the covector. Hence the characteristic set of the first-order condition — the covectors at which the operator is not elliptic — is the zero divisor cone, and it is the same set for the second-order operator, whose symbol is $N(\xi)$ itself. Three names, one set: the null cone of the norm, the characteristic set of the gradient and the set of the zero divisors.

**The two coordinate systems.** The derivative with respect to a complex coordinate is the difference of two real derivatives, $\partial/\partial R_\mu=\partial/\partial r_\mu-i\,\partial/\partial r'_\mu$. On a four-dimensional subspace one of the two vanishes at each slot, so the same glyph denotes a real derivative on the real coefficients and $-i$ times a real derivative on the purely imaginary ones. That one arithmetic fact is the whole of the difference between the four sign patterns of §*The Four Sign Patterns*, and it is why the analysis is done on subspaces and not on the full algebra.

**The reading.** One element, one derivative, and no second object called the field. In the transcription of a physical theory the field and its derivative are different kinds of thing: a section of a bundle and a connection on it. Here they are two elements of one algebra, and the derivative is obtained from the field by the algebra's own product. That is a genuine simplification and a genuine restriction: it is available only because the algebra is non-commutative and finite-dimensional, and the price of it is that differentiability is one condition among several rather than a theorem about limits.

## The First-Order Root and the Propagation

**The square.** The product of the gradient with its conjugate is the d'Alembertian,

$$
\tilde\nabla\tilde\nabla^{\natural}
=\sum_{\mu}e_\mu e_\mu^{\natural}\frac{\partial^{2}}{\partial R_\mu^{2}}
=\sum_{\mu}\frac{\partial^{2}}{\partial R_\mu^{2}}
=e_t\frac{\partial^{2}}{\partial R_t^{2}}+\Delta_Q
=\tilde\nabla^{\natural}\tilde\nabla=\Box ,
$$

the diagonal terms all giving $e_t$ because $e_t^{\natural}=e_t$ and $\vec e_k\vec e_k^{\natural}=-\vec e_k^{2}=e_t$, and the cross terms cancelling in pairs because the three spatial units anticommute with each other and the temporal one commutes with all of them. On the material part $\partial/\partial R_t=-i\,\partial/\partial r'_t$ and $\partial/\partial R_\eta=\partial/\partial r_\eta$, so

$$
\Box_\Phi=\Delta_\Phi-\frac{\partial^{2}}{\partial {r'_t}^{2}},
$$

a minus on the time term and a plus on the three space terms.

**There is no root inside the algebra.** A first-order operator $D$ with $D^{2}=\Box I$ cannot be built from the four units alone. The algebra is four-dimensional over $\mathbb{C}$, and the attempt fails at the fourth generator: three of them exist inside $\mathbb{B}$, namely $i\vec e_x$, $i\vec e_y$, $i\vec e_z$, which square to $e_t$ and anticommute in pairs, and the fourth has no left multiplication to supply it. The obstruction is the dimension of the minimal module: the Clifford relation $\{\gamma_\mu,\gamma_\nu\}=2\delta_{\mu\nu}I$ needs a carrier of complex dimension four, while a minimal left ideal of $\mathbb{B}$ has complex dimension two.

**What does work.** The root exists in the operator algebra of the regular module, $\operatorname{End}(\mathbb{B})\cong M_4(\mathbb{C})$. The two minimal left ideals $S_{\pm}=\mathbb{B}\tilde\Pi_{\pm}$ are exchanged by an element $u$ with $u^{2}=e_t$, the grading $G=R_{\tilde\Pi_+}-R_{\tilde\Pi_-}$ anticommutes with $R_u$, and the two-sided generators

$$
\gamma^{t}=R_u,\qquad \gamma^{k}=L_{i\vec e_k}G
$$

satisfy the Clifford relation. The resulting operator $\mathsf D$ is two-sided, satisfies $\mathsf D^{2}=\Box I$, and its determinant is $\Box^{2}$, which is the square of the determinant of the matrix image of the gradient.

**The shift, and the mass.** A parameter is introduced by adding the pseudoscalar,

$$
\mathsf D_\lambda=\mathsf D+c\gamma_5,\qquad c^{2}=-\lambda,\qquad
\det\mathsf D_\lambda=(\Box-\lambda)^{2},
$$

and the equation $\mathsf D_\lambda\psi=0$ has the chiral form

$$
D_+\psi_+=c\,\psi_-,\qquad D_-\psi_-=-c\,\psi_+,
$$

two first-order equations in two components, each coupling one chiral half to the other through the constant $c$. The scalar shift and the factorisation $(\mathsf D-\kappa)(\mathsf D+\kappa)=\Box-\kappa^{2}$ give the same statement with a real parameter.

**The reading.** The root is the propagation. A second-order wave equation says that a disturbance propagates at a speed fixed by the symbol; a first-order root says the same thing as a transport, with the two chiralities transported independently and the shift coupling them. The two halves are the two minimal left ideals $S_{\pm}$, and the coupling constant is the shift, so the algebra states in one place why a massless field has two decoupled chiral halves and a massive one has two coupled halves. The corpus's Dirac equation has exactly this structure, and its mass term is the one place where the field is multiplied on the right rather than on the left: the derivative acts on one side, the mass on the other, and the algebra's two-sidedness is what makes a mass term possible at all.

**What the reading does not say.** It does not identify $c$ with a mass, and it does not supply the constant that relates the shift to an energy. The root's parameter is a parameter of an operator; the identification with $mc/\hbar$ is an input of the corpus and is recorded as imported, not derived.

## The Regular Field

**The condition.** A field is **regular** when

$$
\tilde\nabla\tilde\Xi=0 .
$$

Written in a scalar part $F_0$ and a vector part $\vec F$, the condition is the pair

$$
\frac{\partial F_0}{\partial R_t}=\operatorname{div}\vec F,
\qquad
\frac{\partial\vec F}{\partial R_t}=-\operatorname{grad}F_0-\operatorname{rot}\vec F,
$$

four complex equations for the four components. Right regularity, $\tilde\Xi\tilde\nabla=0$, gives the same system with $+\operatorname{rot}\vec F$, and the two conditions coincide exactly when the curl vanishes. The regular fields form a complex vector space, closed under right multiplication by constants and under no multiplication in general.

**On the material sector.** The temporal derivative is $-i\partial/\partial r'_t$ and the three spatial derivatives are the ordinary ones. The scalar part of the condition therefore carries the two divergences and the vector part the two curls, and the one element equation is the free Maxwell pair. With a source the equation becomes

$$
\tilde\nabla_\Phi\tilde F=-\sqrt{\mu}\,\tilde J_\Phi ,
$$

whose scalar part is the constraint on the source and whose vector part is the dynamical equation; the componentwise identification is in *Maxwell's Equations in the Biquaternionic Formulation*, §*The Three-Vector Form*. This is the sharpest agreement in the corpus between the two routes: the equations that were transcribed into the algebra in the electromagnetism block are the differentiability condition of the material sector, written without a transcription.

**On the informational sector.** The $i$ moves from the time slot to the three space slots. The condition is then first order in the real time and second order in the imaginary spatial coordinates, which is the algebraic shape of a Schrödinger equation: one real time derivative, an $i$ on the spatial operator, and a second-order spatial symbol. No $\hbar$ appears, and the identification of the rate with an energy is not made here. What the algebra supplies is the shape, and the shape is what the two sectors differ by.

**On the cone.** The characteristic set is the null cone, so the initial-value problem on $\mathbb{B}_\Phi$ requires data on a surface that is not characteristic, and the Cauchy problem on the light-like surfaces is not determined by the same data. On $\mathbb{B}_H$ there is no cone, the symbol is definite, and the operator is elliptic; on $\mathbb{B}_{iH}$ it is elliptic with the opposite sign.

**Harmonicity.** Every regular field is harmonic, $\Box\tilde\Xi=0$ componentwise, because $\Box=\tilde\nabla\tilde\nabla^{\natural}$ and the factors commute. Regularity is therefore strictly stronger than harmonicity, and the difference is a first-order condition that halves the local degrees of freedom: a harmonic field has two functions' worth of freedom per component, a regular field one.

**The reading.** The regular function is the on-shell field. The phrase is exact rather than analogical: a field satisfies its free equation precisely when it is a differentiable function of the algebra's variable in the algebra's sense, so "on shell" and "regular" are the same predicate. The gain is that the predicate is not a differential equation imposed from outside but the differentiability of a function; the loss is that the predicate is linear, so it carries no interaction and no scale.

**What regularity does not give.** No mass, because a mass is a shift and a shift is a constant term, not a derivative; the shifted operator $D_\alpha=D+M_\alpha$ is a different condition with a different kernel, and it is discussed in *Biquaternion Regular Functions* with its three branches and its boundary-value criterion. No charge, because a coupling needs a second element and a product, and the regular condition is homogeneous and linear. Both enter through the integral, or through the two-sided condition, and not through this one.

## The Two-Sided Derivative and the Eikonal

**The third definition.** Let $\Omega$ be open in $\mathbb{B}$ and let $F$ be of class $C^{1}$ in the four complex coordinates. The function admits a **two-sided derivative** at $\tilde Z\in\Omega$ when there are elements $L,R$, neither zero, with

$$
dF=L\,dZ\,R\qquad\text{for every }dZ\in\mathbb{B}.
$$

The pair is determined only up to $L\mapsto L\alpha$, $R\mapsto\alpha^{-1}R$ with $\alpha$ central, because only a central element commutes past $dZ$ on both sides. So the pair is a projective object with one complex parameter of freedom. Two features are the whole of its interest: no inverse is taken, and the condition is not linear in $F$.

**The criterion, and the identity that makes it an equation.** For each component $\Sigma=F_{CD}$ the four coordinate derivatives form a two-by-two array,

$$
\mathsf D\Sigma=
\begin{pmatrix}
\dfrac{\partial\Sigma}{\partial\upsilon} & \dfrac{\partial\Sigma}{\partial w}\\[4pt]
\dfrac{\partial\Sigma}{\partial p} & \dfrac{\partial\Sigma}{\partial v}
\end{pmatrix},
$$

and the condition is that this array have rank at most one. For a two-by-two array that is the vanishing of the determinant, and the determinant is a quarter of the norm of the biquaternion gradient,

$$
\det\mathsf D\Sigma=\tfrac14 N(\nabla\Sigma)
=\tfrac14\left[\left(\frac{\partial\Sigma}{\partial z_0}\right)^{2}
-\left(\frac{\partial\Sigma}{\partial z_1}\right)^{2}
-\left(\frac{\partial\Sigma}{\partial z_2}\right)^{2}
-\left(\frac{\partial\Sigma}{\partial z_3}\right)^{2}\right],
$$

in the coordinates $z_0=\tfrac12(\upsilon+v)$, $z_3=\tfrac12(\upsilon-v)$, $z_1=\tfrac12(w+p)$ and $z_2=\tfrac{i}{2}(w-p)$ of complexified Minkowski space. The identity is a chain-rule computation; the source article verified it on one hundred generic complex points with a largest residual of $1.4\times10^{-14}$.

**The eikonal.** The corollary is that the two-sided condition on every component is

$$
N(\nabla\Sigma)=0 ,
$$

the complex eikonal, and it says that the gradient of every component is a zero divisor or zero. The condition is first order, quadratic, homogeneous of degree two in the gradient and therefore scale covariant componentwise, and it is conformally invariant without a compensating weight. It is not additive: for two null gradients the norm of the sum is twice their pairing, so the solution set is not a vector space.

**The two conditions compared.** They have the same number of complex equations, four, and the same characteristic set, the zero-divisor cone, because the determinant of the symbol of $\tilde\nabla$ is the norm. They differ in degree: one is linear in the first derivatives, one quadratic. Neither contains the other, and the witnesses are the identity $\tilde Z$, which is two-sided with $\tilde\nabla\tilde Z=-2e_t$ and is not regular, and the single-plane holomorphic function $A^{2}$, which is regular with a determinant that vanishes only on the two planes $z_0=\pm z_1$. The nonlinearity is inert on the class the programme actually constructs, because there the two first-order relations multiply to the eikonal and cross-differentiate to $\Box\Sigma=0$, so every member of that class is harmonic as well.

**The reading.** The two-sided condition is the primary equation, and the derivative is defined before any equation is written. That is the sense in which the algebrodynamical programme inverts the corpus's order: it does not ask which equation a field satisfies, it asks what a differentiable function of an algebraic variable can be, and it accepts a condition that is quadratic rather than linear. The physical content of the answer is that the gradient is light-like everywhere, so the singular set of a solution is a null set, and it is at the singularities that the programme places its particles. The generating function of the Kerr solution is the worked case, and the self-quantised charge is the programme's headline claim.

**The boundaries of the reading.** This is an external programme. The corpus records it, verifies the algebraic parts, and does not adopt it: the derived systems are weaker than Maxwell's equations, cannot displace the corpus's $\tilde\nabla_\Phi\tilde F=-\sqrt\mu\tilde J_\Phi$, and the particle interpretation is labelled as the programme's. What the corpus takes from it is the existence proof: a genuinely nonlinear holomorphy over this algebra exists, and the linear Fueter theory is a choice rather than the only option.

## The Fueter Construction and the Axis

**The construction.** Let $f_0$ be holomorphic on a disc, written $f_0(A)=u(a,a')+iv(a,a')$ with $u$ and $v$ real-valued. Its **axial extension** replaces the variable $A$ by $q_t$ and its imaginary part $a'$ by the radius $\rho=\|\vec q\|$, and replaces the complex imaginary unit by the unit vector $\vec u_{\mathrm d}=\vec q/\rho$, which is legitimate because $\vec u_{\mathrm d}^{2}=-1$. Fueter's theorem states that

$$
F_{\mathrm{fn}}=\Delta_4\,f_{\mathrm{ax},0}
=\frac{2\,\partial_\rho u}{\rho}
+\vec u_{\mathrm d}\left(\frac{2\,\partial_\rho v}{\rho}-\frac{2v}{\rho^{2}}\right)
$$

is real-analytic on the ball, by continuity at $\rho=0$, and is both left- and right-regular there. The second-order operator is the whole of the difference between a holomorphic seed and a regular field: the identity map is slice-regular and not regular, since

$$
\tilde\nabla\tilde Q=\sum_\mu e_\mu e_\mu=e_t-\vec e_x^{2}-\vec e_y^{2}-\vec e_z^{2}=-2e_t\neq0 ,
$$

while the completed seed is regular by construction: the square completes to the constant field $\Delta_4\tilde Q^{2}=-4e_t$, whose gradient vanishes identically. The completion of a seed of degree $n$ has degree $n-2$, and two consequences follow at once. The affine seeds complete to zero, so the map has the affine kernel and is injective only modulo it. And the first seed that produces a field at all is the quadratic one, which produces a constant. Recomputed here in double precision on a generic point, the Laplacian is $-3.99999999\,e_t$, the gradient of $\tilde Q^{2}$ itself being $-4Q_te_t$ and not zero.

**The odd dimension.** The generalisation, the Fueter–Sce theorem, takes $n$ odd and applies $\Delta^{(n-1)/2}$ to the axial extension on $\mathbb{R}^{n+1}$. Three hypotheses are needed and none can be dropped: the seed must be holomorphic, the affine kernel must be quotiented out, and the exponent must be a non-negative integer. The parity condition is the reason the construction is stated for the quaternion and biquaternion case at $n=3$ and not for an arbitrary dimension.

**The axis.** On $\mathbb{B}_{H}$ the imaginary units form the two-sphere of unit pure imaginary quaternions, every element with nonzero vector part is $\tilde Q=q_t+I\rho$ with $I$ on that sphere, and the slices meet only in the real line. On $\mathbb{B}$ the roots of $-1$ are the larger family $\pm i$, $\pm\mu$ and $b\mu+d\nu i$ with $\mu,\nu$ perpendicular unit pure real quaternions and $b^{2}-d^{2}=1$, which is not a sphere. There is therefore no single imaginary sphere on which to base the theory, and the axial construction must select one root, hence one slice, at a time.

**The reading.** The Fueter extension is the axial completion. A holomorphic function of one complex variable is two real functions of two real variables; its completion is a field on four real dimensions, and the completion operator is the second-order operator of the theory. Three statements follow, and each is a statement about physics as much as about algebra. First, the minimal data of an axially symmetric regular field is one complex function of one complex variable, so the four-dimensional field contains no more information than a two-dimensional one. Second, the reconstruction is unique only modulo the affine seeds, which is exactly what a second-order operator cannot see: a constant and a linear function are invisible to $\Delta_4$. Third, the axis is a parameter of the family and not a datum of the algebra, the same way the axis of the idempotents $\tilde\Pi_\pm(\vec u)$ is a parameter. A configuration with an axis is therefore a choice of slice, and a theory that admits every axis at once is a family of theories indexed by a point of the root set.

**What the reading does not say.** It does not say that every physical field is axially symmetric. It says that the axially symmetric ones have one-variable data, and that the completion is unique up to two invisible modes. The general regular field is the $\tilde\nabla$-kernel, which is much larger than the axial class and is not obtained from any holomorphic seed by this construction.

## The Integral and the Source

**The integral.** For a biquaternion-valued field on a domain of a four-dimensional subspace, the integral is defined componentwise against the Lebesgue measure of the four real coordinates. It is linear, additive, bounded by the sup norm times the volume, and it exists for continuous fields on compact domains. Integration by parts, the divergence theorem and the Green formulas follow componentwise, and the formula for the d'Alembertian is the biquaternionic Kirchhoff–Green representation: the volume integral carries the source and the surface integral carries the boundary data.

**The kernel.** The fundamental solution of the gradient is

$$
G_{\mathrm{fn}}(\tilde R)=\frac{\tilde R^{\natural}}{\|\tilde R\|^{4}},
\qquad
\tilde\nabla G_{\mathrm{fn}}=2\pi^{2}\delta_0\,e_t ,
$$

homogeneous of degree $-3$, singular at the origin and regular off it, with $2\pi^{2}$ the surface area of the unit three-sphere. On $\mathbb{B}_{H}$ the Cauchy integral formula holds in the form

$$
\tilde\Xi(\tilde R_0)=\frac{1}{2\pi^{2}}\int_{\partial\Omega}G_{\mathrm{fn}}(\tilde R_0-\tilde R)\;\tilde u_{\mathrm n}(\tilde R)\;\tilde\Xi(\tilde R)\,dS ,
$$

for $\tilde R_0$ inside $\Omega$ and $\tilde u_{\mathrm n}$ the unit normal of the boundary. When $\tilde\nabla\tilde\Xi$ does not vanish a second integral over the volume, against the same kernel, is added and carries the failure of regularity; the order and the sign of the factors are fixed by the convention of the source article, where the representation formula for $\Box$ is stated. For a regular field the boundary integral alone reproduces the field.

**The consequences.** The mean value property, the maximum principle, Liouville's theorem, the identity theorem and the Cauchy estimates follow in the classical way, and a residue theorem holds with the residue defined as a boundary integral rather than as a coefficient, because non-commutativity forbids the coefficient reading.

**The reading.** The integral is the action, and the objects of the reading are the objects of the representation formula. The boundary term is the data; the volume term is the source; the kernel is the propagator. The identification is not an analogy of vocabulary but a statement about where strength enters: a regular field has no volume term at all, so a field that is not free is a field whose own failure to be regular is integrated against the kernel, and that failure is the only place a strength can be read. In the corpus's own terms the same kernel is both the Cauchy kernel of the analysis and the propagator of the field theory, and the two integrals of the series meet at one set: the pole set of the kernel is the shell, and the residue there is the weight of the mode. The biquaternion form adds one thing to that picture: the pole is a set of elements, not a set of numbers, so the shell is a subset of the algebra.

**Liouville, and the price of a definite sign.** On the quaternion subspace the maximum principle holds, so a regular field bounded on all of space is constant. A non-constant regular field is therefore unbounded somewhere, and since it is real-analytic off its singular set, it has a singular set. That is a statement with a physical face: in the elliptic sector regularity forbids a non-trivial field that is finite everywhere, so every field carries a source. On the material sector the argument fails, because a hyperbolic operator has no maximum principle, and something else takes its place: the kernel is no longer the Euclidean one, the point singularity becomes a cone, and the domains of the Cauchy theory must avoid the cone and not merely the origin.

**What the reading does not say.** It does not identify the volume term with a Lagrangian density, and it does not derive an action principle. The corpus's variational principles are stated for the field equations, in the archived variational articles, and carry their own functionals; the word *action* in the reading names the integral of the field against the kernel, which is a representation formula, not a variational principle. The distinction is stated in §*The Limits* and is the honest boundary of III.1.h.

## The Four Sign Patterns

**One operator, six restrictions.** The restriction of $\Box$ to a remarkable subspace is $e_t$ times the operator of the norm of that subspace, so the principal symbol of the restriction is the norm itself. The table states the result.

| subspace | $\dim_{\mathbb{R}}$ | inertia of the norm | type |
| --- | --- | --- | --- |
| the centre $\mathbb{B}_{C}$ | $2$ | $(1,1)$ | elliptic |
| the vector subspace $\mathbb{B}_{V}$ | $6$ | $(3,3)$ | not elliptic |
| the quaternion subspace $\mathbb{B}_{H}$ | $4$ | $(4,0)$ | elliptic |
| the anti-quaternion subspace $\mathbb{B}_{iH}$ | $4$ | $(0,4)$ | elliptic |
| the informational sector $\mathbb{B}_{\Psi}$ | $4$ | $(1,3)$ | hyperbolic |
| the material sector $\mathbb{B}_{\Phi}$ | $4$ | $(3,1)$ | hyperbolic |

**The equivalence.** The centre's $(1,1)$ and the vector subspace's $(3,3)$ are the inertias of the real part of the norm, which is complex on the two complex subspaces; on the four real forms the norm is real and the entry is its own inertia. Ellipticity, the absence of a zero divisor and the absence of a null set then coincide on all six, though for two different reasons: on the real forms the criterion is the definiteness of the norm, and on the centre it is the field property, the complex symbol vanishing only at the origin. So ellipticity and invertibility of every nonzero element are one condition, and it holds on the centre, the quaternion and the anti-quaternion subspaces and fails on the other three, where the domains of any contour theory must avoid a cone of real codimension one.

**The reading.** The sign pattern is the sector, and the sector is the world. The two subspaces that carry the physics of the corpus are the two indefinite ones, and they are the only two on which a light cone exists. A world with a causal structure is therefore a world whose analysis is non-elliptic, and the ellipticity of the quaternion subspace — the classical Fueter setting — is exactly the property that a relativistic world cannot have. The material sector's $(3,1)$ and the informational sector's $(1,3)$ differ by one sign, and that sign is the placement of the imaginary unit: on the material side it sits on the temporal coefficient, on the informational side on the three spatial ones. The two sectors are one algebra read with the $i$ on one side or the other, and the two sign patterns are the same statement about which side.

**What the table does not decide.** It does not select a dynamics on any subspace, and it does not say that the material sector is the only physically relevant one. It says that the type of the equation is fixed by the subspace and that the type is not negotiable: a hyperbolic equation on $\mathbb{B}_{\Phi}$ cannot be made elliptic by a change of variables that stays inside the subspace, because the inertia is a property of the norm.

## The Group and the Exponential

**The group.** $\mathbb{B}^{\times}$ is the group of invertibles, a real Lie group of dimension eight. Its exponential is defined by the series, computed in closed form in the elementary-functions article, and it is a local diffeomorphism at the identity: it maps a neighbourhood of zero in the Lie algebra onto a neighbourhood of $e_t$ in the group. The norm-one subgroup

$$
\mathbb{B}^{\times}_1=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=1\}
$$

has real dimension six, is connected, simply connected and non-compact, and has centre $\{\pm e_t\}$. The unit quaternions $S^{3}$ have real dimension three, are compact, and are the maximal compact subgroup. The $*$-unitary elements form $\mathrm{U}(2)$, decomposed as

$$
\mathrm{U}(2)=S^{3}\cdot\mathrm{U}(1)\cong\bigl(SU(2)\times U(1)\bigr)/\{\pm(1,1)\}.
$$

**The Lie algebra.** The Killing form is $\kappa(\tilde X,\tilde Y)=16\operatorname{Re}(\operatorname{Sc}(\tilde X\tilde Y)-\operatorname{Sc}\tilde X\operatorname{Sc}\tilde Y)$, with radical the centre $\mathbb{C}e_t$ and inertia $(3,3)$ on the scalar-free part: negative on the compact subalgebra and positive on $i$ times it.

**The failure of surjectivity.** The exponential is surjective onto the compact $S^{3}$ and not surjective onto $\mathbb{B}^{\times}_1$. The obstruction is a non-semi-simple element with the repeated eigenvalue $-1$, the same obstruction as in $SL(2,\mathbb{R})$. The image still contains a neighbourhood of the identity and generates the connected group, so failure of surjectivity is not failure of generation.

**The reading.** The exponential is the transform. A derivative is a derivation, a derivation is a rate, and the exponential turns a rate into an element — and an element is what acts on a field by multiplication. That is the algebraic content of the word: the transform is the map that converts a generator into a frame, so that a differential operator becomes a multiplication and a differential equation becomes an algebraic one. The two real directions of the trace-free part are the two physical families of transformations: the compact one, generated by a real vector, is the rotations, and the non-compact one, generated by $i$ times a vector, is the boosts. Compactness is exactly the difference between them, and it is visible in the Killing form, which is negative on the first and positive on the second. The group of the norm modulo its centre is the Lorentz group, which is why the interval and its group come out of one condition $\langle\tilde Q\rangle_{\natural}=1$ rather than from a postulate about a metric.

**The ceiling.** The group reached this way is the algebra's own, of real dimension eight, and its subgroups are the ones listed. A larger group needs a larger carrier and not a larger algebra: $M_n(\mathbb{B})\cong M_{2n}(\mathbb{C})$, so $M_3(\mathbb{B})\cong M_6(\mathbb{C})$ contains $\mathfrak{su}(3)$, and the closed forms for $\mathrm{SU}(3)$ and $\mathrm{SU}(4)$ are matrices of biquaternions. The octet is not inside $\mathbb{B}$, and no reading in this entry puts it there.

## The Elementary and the Special Functions

**The spectral setting.** Every direct elementary function is defined by applying a scalar power series to $\tilde Q$, and every value lies in the commutative subalgebra $\mathbb{C}[\tilde Q]$ generated by $\tilde Q$. The characteristic quadratic of $\tilde Q$ has trace $2Q_t$ and norm $Q_t^{2}+B^{2}$ with $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$, and its discriminant $-4B^{2}$ separates two regimes. In the **oscillatory regime** $B\neq0$ the subalgebra is $\mathbb{C}\times\mathbb{C}$, the element has eigenvalues $Q_t\pm iB$, and the closed forms are built on $\tilde Q=Q_t e_t+B\vec U$ with $\vec U^{2}=-e_t$. In the **nilpotent regime** $B=0$ with $\vec Q\neq0$ the subalgebra is $\mathbb{C}[\epsilon]/(\epsilon^{2})$ and every series truncates after the linear term: $\exp(\tilde Q)=e^{Q_t}(e_t+\vec Q)$, $\operatorname{Log}\tilde Q=\operatorname{Log}Q_t\,e_t+\vec Q/Q_t$.

**What survives, and what fails.** The Pythagorean identity, the hyperbolic identity, the double-angle formulas and the relation between the exponential and the trigonometric functions survive non-commutativity for a single variable, because they are identities inside one commutative subalgebra. The addition formulas for two independent biquaternions do not survive, and they fail on the smallest possible example, $\tilde Q_1=\vec e_x$ and $\tilde Q_2=\vec e_y$.

**The logarithm.** In the oscillatory regime the logarithm is

$$
\tilde Q_{\log}=\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-,
\qquad
\mu_\pm=\operatorname{Log}\lambda_\pm+2\pi ik_\pm,
\qquad
\tilde\Pi_\pm=\tfrac12(e_t\mp i\vec U),
$$

with the parity-matched lattice $\ker\exp\cap\mathbb{C}[\tilde Q]=\{\pi im\,e_t+\pi n\,\vec U:\ m\equiv n\ (\mathrm{mod}\ 2)\}$ as its fibre. The principal branch is single-valued and real-analytic off the walls where an eigenvalue is a negative real number, and no continuous single-valued logarithm exists on all of $\mathbb{B}^{\times}$.

**The reading.** The elementary functions are the flows written out. The exponential is the one-parameter group, the logarithm is its inverse read on the group, the powers are its iterates, and the trigonometric functions are the oscillatory regime of the same series. Two statements of the section are statements about flows in general and not about this algebra in particular. First, the addition formula is a commutativity statement: two flows add their parameters exactly when their generators commute, and $\vec e_x$ and $\vec e_y$ do not. Second, the nilpotent regime is a flow that truncates, so the transformation it generates is not periodic and not exponential in the parameter; it is a single step, and its series has only two terms.

**The special functions.** The functions that arise from the analysis are the kernels: the Cauchy kernel, the Poisson kernel and the Green's function of the d'Alembertian. The power-series functions — Bessel, the orthogonal polynomials, the hypergeometric function — reduce on the vector part and are organised by the same complex norm $B$ that separates the two regimes, and the integral-defined ones, gamma and zeta, raise a definition problem that the corpus leaves open. The reading is short and it is the same reading as §*The Integral and the Source*: the special functions of this algebra are its propagators, so a table of special functions is a table of kernels.

## The Interpretations

### III.1.a — The Derivative Is the Field Equation

**The object.** $\tilde\nabla$ is an element of $\mathbb{B}$, the field $\tilde\Xi$ is an element of $\mathbb{B}$, and the derivative is a product.

**The warrant.** The four coefficients of $\tilde\nabla$ are the four coordinate derivatives, and the four units multiply them; no inverse and no limit enters. The characteristic set of $\tilde\nabla$ is the zero-divisor cone, so the operator's own algebra decides where it degenerates.

**The reading.** There is no second object called the derivative. In a transcription the field and its derivative are a section and a connection; here they are two elements of one algebra, and the derivative is obtained from the field by the algebra's product. The simplification is real and it is also the restriction: differentiability becomes one condition among several, and the others are not equivalent to it.

### III.1.b — The Second Order Is Where the Sectors Part

**The object.** $\Box=\tilde\nabla\tilde\nabla^{\natural}$ restricts to four different operators on the four real forms, with inertias $(4,0)$, $(0,4)$, $(1,3)$ and $(3,1)$.

**The warrant.** The restriction theorem of *Remarkable Subspaces and the Analysis*: on each real form $\Box$ is $e_t$ times the operator of the norm, and the norm has the inertia of the form. Ellipticity is equivalent to the absence of zero divisors on the form.

**The reading.** The derivative is one object and the field equation is four, and the difference is the sector. A world with a light cone is a world whose second-order operator is hyperbolic, so the light cone is not added to the theory: it is the failure of ellipticity of the restriction of one operator to one subspace. The two sectors that carry the physics are the two indefinite ones, and the one sign that separates them is the placement of the imaginary unit.

### III.1.c — The Root Is the Propagation

**The object.** A first-order operator $\mathsf D$ with $\mathsf D^{2}=\Box I$, and its shifted form $\mathsf D_\lambda=\mathsf D+c\gamma_5$ with $\det\mathsf D_\lambda=(\Box-\lambda)^{2}$.

**The warrant.** No root exists by left multiplication alone, because a minimal left ideal has complex dimension two and the Clifford relation needs four. The root exists in the operator algebra of the regular module, built from the two ideals, the exchange $u$ and the grading $G$, and its shifted form has the chiral rows $D_+\psi_+=c\psi_-$ and $D_-\psi_-=-c\psi_+$.

**The reading.** A second-order wave is two first-order transports. The two transported objects are the two chiral halves, which are the two minimal left ideals, and the shift is what couples them. A massless field has two decoupled halves and a massive one has two coupled halves, and the algebra says so in one line. The corpus's Dirac equation has the same structure, with the mass as the one term that multiplies on the right.

### III.1.d — The On-Shell Field Is the Regular Field

**The object.** The condition $\tilde\nabla\tilde\Xi=0$, and its componentwise form $\partial_tF_0=\operatorname{div}\vec F$, $\partial_t\vec F=-\operatorname{grad}F_0-\operatorname{rot}\vec F$.

**The warrant.** The operator is the gradient, so the condition is the differentiability of the field in the algebra's own sense. On the material sector the same four equations are the free Maxwell pair, and with a source they are $\tilde\nabla_\Phi\tilde F=-\sqrt\mu\tilde J_\Phi$.

**The reading.** "On shell" and "regular" are the same predicate, so the free field equation is not a postulate imposed on the field but a property of the function. The corpus's electromagnetism and the corpus's analysis meet here without a transcription step: the four equations of the free field are the four equations of differentiability, written once.

### III.1.e — The Characteristic Cone Is the Light Cone

**The object.** The symbol $S(\xi)=\sum_\mu\xi_\mu\mathsf M_2(e_\mu)$ and its determinant $\det S(\xi)=N(\xi)$.

**The warrant.** The determinant of a sum of scaled units is the norm of the covector, so the characteristic set of the gradient is the set of null covectors, which is the zero-divisor cone. The same computation gives the characteristic set of the second-order operator, whose symbol is the norm itself.

**The reading.** The light cone is not put into the theory as a postulate about a metric; it is the set on which the algebra's own product fails to be invertible, read on covectors. Three descriptions coincide: the null cone of the norm, the set of zero divisors, and the characteristic set of the derivative. A theory built on this algebra therefore has a causal structure for the same reason that it has zero divisors, and the two cannot be separated.

### III.1.f — The Two-Sided Condition Is the Primary Equation

**The object.** $dF=L\,dZ\,R$, the rank-one criterion, and the eikonal $N(\nabla\Sigma)=0$.

**The warrant.** The condition needs no inverse and survives the zero divisors, at the price of being nonlinear. Its componentwise form is the vanishing of a determinant, and the determinant is a quarter of the norm of the gradient, so the condition says that the gradient is null everywhere.

**The reading.** One can define the derivative before writing any equation, and the equation that follows is quadratic. The physical consequence is that the singular set of a solution is null, so a singularity is a light-like object and can carry the data that a particle carries. This is the reading the algebrodynamical programme develops, and the corpus records it as external: the algebraic statements are verified, the particle interpretation is the programme's.

### III.1.g — The Fueter Extension Is the Axial Completion

**The object.** The map $f_0\mapsto\Delta_4f_{\mathrm{ax},0}$ from holomorphic functions of one complex variable to regular fields on four real dimensions.

**The warrant.** Fueter's theorem, with the affine kernel: the completion of a seed of degree $n$ has degree $n-2$, so the affine seeds complete to zero, the quadratic seed to a constant, and the reconstruction is unique modulo the two invisible modes. The Fueter–Sce generalisation needs the odd dimension.

**The reading.** The minimal data of an axially symmetric field is one complex function of one complex variable, so four-dimensional data are two-dimensional data completed by a second-order operator. The invisible modes are exactly what a second derivative cannot see, and the axis is a parameter of the family, chosen one root at a time, exactly as the idempotents are chosen one axis at a time.

### III.1.h — The Integral Is the Action, the Kernel Is the Propagator, the Pole Is the Shell

**The object.** The Cauchy–Lanczos–Fueter formula, the fundamental solution $G_{\mathrm{fn}}=\tilde R^{\natural}/\|\tilde R\|^{4}$ and its distributional gradient $2\pi^{2}\delta_0e_t$.

**The warrant.** Integration by parts and the divergence theorem give the representation formula; the kernel is homogeneous of degree $-3$ and regular off the origin; the regular case drops the volume term and leaves the boundary integral alone.

**The reading.** The three terms of the formula are the three objects of the reading. The boundary term is the data, the volume term is the source, the kernel is the propagator. Strength enters only through the failure of regularity, so a free field has no volume term and a non-free one is its own failure integrated against the kernel. The pole set of the kernel is the shell, and the corpus's two integral articles — the action and the transform — meet at that set.

### III.1.i — Liouville Forces a Singularity

**The object.** Liouville's theorem: a regular field bounded on all of $\mathbb{B}_{H}$ is constant.

**The warrant.** The mean value property and the maximum principle, both consequences of the Cauchy formula, give Liouville's theorem on the elliptic subspace. On the hyperbolic sectors the maximum principle fails and the argument does not carry over; there the kernel changes and the domains must avoid the cone.

**The reading.** In the elliptic sector a non-constant regular field cannot be finite everywhere, so every field carries a singular set. The price of a definite inertia is therefore that the field must be singular somewhere; the price of an indefinite inertia is that the singular set is a cone rather than a point. Neither price can be avoided, and the two together say that a source-free, everywhere-finite, everywhere-regular field exists only in one case: the constant.

### III.1.j — The Exponential Is the Flow

**The object.** The exponential from the Lie algebra to the group of invertibles, its closed form, and its failure to be surjective onto the norm-one group.

**The warrant.** The exponential is a local diffeomorphism at the identity, its closed form is computed case by case, its image contains a neighbourhood of the identity and generates the connected group, and the obstruction to surjectivity is a non-semi-simple element with the repeated eigenvalue $-1$.

**The reading.** The transform is the map that turns a rate into a frame. A derivative is a derivation and a derivation is a rate; an element is a frame and acts by multiplication. The exponential is what converts one into the other, so a differential equation becomes an algebraic one, and the parameter of the group is the accumulated rate. The failure of surjectivity says that not every frame is one exponential of one rate, which is a statement about transformations and not about flows: some frames are products of flows and not flows.

### III.1.k — The Two Real Directions Are Rotation and Boost

**The object.** The trace-free part of the Lie algebra, its two real directions, the compact subalgebra and $i$ times it, and the Killing form of inertia $(3,3)$.

**The warrant.** The generators $i\vec e_k$ are anti-Hermitian and the generators $\vec e_k$ are Hermitian; the first family is the non-compact direction, the second the compact one; the Killing form is negative on the compact subalgebra and positive on $i$ times it. The norm-one group is $SL(2,\mathbb{C})$ with centre $\{\pm e_t\}$, and modulo the centre it is the Lorentz group.

**The reading.** The Lorentz group and the rotation group are the two real forms of one complex group, and the difference between them is compactness, which is the sign of one quadratic form. A boost is a rotation by an imaginary angle, and the algebra states this as the placement of the $i$ on the generator rather than as an analytic continuation performed afterwards. The group of the interval is the group of the norm, so the metric and its group are one condition.

### III.1.l — Addition Fails, and That Is Non-Commutativity

**The object.** The exponential and the trigonometric functions of one variable, and their failure to satisfy the addition formulas for two independent elements.

**The warrant.** Every direct elementary function lies in $\mathbb{C}[\tilde Q]$, where the scalar identities hold. For two independent elements the subalgebras differ, the generators do not commute, and the identity fails at $\tilde Q_1=\vec e_x$, $\tilde Q_2=\vec e_y$.

**The reading.** An addition formula is a statement that two flows compose by adding their parameters, which holds exactly when the generators commute. The failure is therefore not a defect of the trigonometry but the non-commutativity of two flows, and the correct law is the group law, $\exp(\tilde X)\exp(\tilde Y)$, which is a product and not a sum. In the nilpotent regime the same statement has a second face: the flow truncates, so the transformation it generates is a single step whose series has two terms.

## The Limits

**The entry has no dynamics.** No element is selected, no equation of motion is imposed, and no action principle is stated. The six readings are readings of one operator at different orders and on different sectors; none of them fixes a Lagrangian, and the corpus records that it has none.

**The word action names an integral and not a variational principle.** III.1.h identifies the representation formula with the action because both integrate the field against a kernel and both carry the strength. It does not claim that the volume term is a Lagrangian density, and the distinction is not cosmetic: a variational principle would supply the dynamics that this entry does not have.

**No constant is derived.** $\hbar$ does not appear in the analysis, and the identification of the root's shift with a mass, of the flow's rate with an energy, and of the kernel's pole with a shell are inputs of the corpus. The algebra supplies the shape of each identification and none of the numbers.

**The integral theory is stated on one subspace.** The Cauchy formula, its consequences and the residue theorem are theorems on $\mathbb{B}_{H}$, where the norm is definite. On the indefinite sectors the kernel is not the Euclidean one, the domains must avoid the cone, and the integral theory is open; the corpus records this as an open question and not as a result.

**Fueter theory needs an axis.** On $\mathbb{B}_{H}$ the axis is free; on $\mathbb{B}$ the roots of $-1$ are not a sphere and the slice must be chosen. Every statement of §*The Fueter Construction and the Axis* is therefore a statement about one slice at a time, and no axis-free version is claimed.

**The two-sided condition is an external programme.** The algebraic part is verified in the corpus's own terms; the particle reading is the programme's and is recorded and not endorsed. The derived systems are weaker than the corpus's Maxwell equation and cannot displace it.

**The group is the algebra's group.** It is not a gauge group, and the gauge ceiling is untouched: $\mathfrak{su}(3)$ is reached by enlarging the carrier to $M_3(\mathbb{B})$, not by finding an octet inside $\mathbb{B}$.

**The transform here is not the Fourier transform.** The exponential of a generator is the transform of this entry; the kernel $\exp(-2\pi i\tilde Z\omega t)$ and the inversion theorem belong to the next section, and the two are related by one fact only: the Fourier kernel is the exponential of a root of $-1$. Nothing in this entry states an inversion theorem, a Plancherel theorem or a convolution theorem.

## Summary

**The derivative of this algebra is an element.** $\tilde\nabla=\sum_\mu e_\mu\partial/\partial R_\mu$ takes no inverse, survives the zero divisors and acts by left multiplication. Its coefficients are the four coordinate derivatives, so the derivative and the field are two elements of one algebra, and the operator section that precedes this one is the chapter of which this is the application.

**Its square is the d'Alembertian, and the square splits by sector.** $\Box=\tilde\nabla\tilde\nabla^{\natural}$ is the Laplacian on the quaternion subspace, minus the Laplacian on the anti-quaternion subspace, and the wave operator of inertias $(1,3)$ and $(3,1)$ on the two Hermitian sectors. The restriction of $\Box$ to a remarkable subspace is the operator of that subspace's norm, so the type of the equation is the inertia of the norm and ellipticity is the absence of zero divisors.

**The characteristic set is the zero-divisor cone.** The determinant of the symbol of the gradient is the norm of the covector, so the first-order and the second-order operators have one characteristic set, and it is the light cone. The causal structure of the theory and the failure of invertibility of the algebra are one fact.

**Regularity is the field equation.** $\tilde\nabla\tilde\Xi=0$ is four equations; left and right regularity differ by the sign of the curl; on the material sector the four are the free Maxwell pair; on the informational sector the same system has one real time derivative and an $i$ on the spatial operations. Every regular field is harmonic, and regularity is strictly stronger.

**The two-sided condition is a second, quadratic equation.** $dF=L\,dZ\,R$ is the rank-one condition on each component's derivative array, and the determinant of that array is a quarter of the norm of the gradient, so the condition is the complex eikonal and its gradient is null everywhere. It has the same characteristic set as the linear condition and neither contains the other.

**Fueter's construction completes one-variable data.** $\Delta_4$ of the axial extension of a holomorphic function is regular, the completion lowers the degree by two, the affine seeds are invisible, and the construction needs a chosen axis because the roots of $-1$ on $\mathbb{B}$ are not a sphere.

**The integral carries the source.** The fundamental solution of the gradient is $\tilde R^{\natural}/\|\tilde R\|^{4}$ with distributional gradient $2\pi^{2}\delta_0e_t$; the Cauchy formula holds on the quaternion subspace and its regular case is a boundary integral alone; the mean value property, the maximum principle, Liouville's theorem and a residue theorem follow. A free field has no volume term, so strength enters only through the failure of regularity.

**The exponential is the transform.** The group of invertibles is a Lie group of dimension eight, the norm-one group of dimension six, the unit quaternions of dimension three; the exponential is a local diffeomorphism and not surjective; the Killing form has inertia $(3,3)$ with radical the centre. The two real directions of the trace-free part are the rotations and the boosts, and the group of the norm modulo its centre is the Lorentz group.

**The elementary functions are the flows written out.** Every direct function lies in $\mathbb{C}[\tilde Q]$, with an oscillatory and a nilpotent regime; the identities of one variable survive and the addition formulas of two fail; the special functions that arise from the analysis are its kernels.

## Summary of Notation

| object | notation | content |
| --- | --- | --- |
| the algebra | $\mathbb{B}$ | $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, units $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| the variable | $\tilde R$ | $\sum_\mu R_\mu e_\mu$, with $R_\mu=r_\mu+ir'_\mu$ |
| the field | $\tilde\Xi$ | a biquaternion-valued function of $\tilde R$ |
| the gradient | $\tilde\nabla$ | $\sum_\mu e_\mu\partial/\partial R_\mu$ |
| the conjugate gradient | $\tilde\nabla^{\natural}$ | $\sum_\mu\varepsilon_\mu e_\mu\partial/\partial R_\mu$, $\varepsilon=(1,-1,-1,-1)$ |
| the d'Alembertian | $\Box$ | $\tilde\nabla\tilde\nabla^{\natural}=\partial^2/\partial R_t^2+\Delta_Q$ |
| the spatial Laplacian | $\Delta_Q$ | $\sum_\eta\partial^2/\partial R_\eta^2$ |
| the Euclidean Laplacian | $\Delta_4$ | $\sum_\mu\partial^2/\partial q_\mu^2$ on $\mathbb{B}_{H}$ |
| the norm of an element | $N=\langle\tilde Q\rangle_{\natural}$ | $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ |
| the symbol | $S(\xi)$ | $\sum_\mu\xi_\mu\mathsf M_2(e_\mu)$, with $\det S=N(\xi)$ |
| the regular field | $\tilde\nabla\tilde\Xi=0$ | the free field equation |
| the right-regular field | $\tilde\Xi\tilde\nabla=0$ | the same system with $+\operatorname{rot}$ |
| the two-sided derivative | $dF=L\,dZ\,R$ | the semi-derivatives $L$ and $R$, defined up to a central scalar |
| the derivative array | $\mathsf D\Sigma$ | the $2\times2$ array of the four coordinate derivatives of a component |
| the eikonal | $N(\nabla\Sigma)=0$ | the rank-one condition, equivalently $\det\mathsf D\Sigma=0$ |
| the axial extension | $f_{\mathrm{ax},0}$ | $u(q_t,\rho)+\vec u_{\mathrm d}v(q_t,\rho)$ |
| the axis | $\vec u_{\mathrm d}=\vec q/\rho$ | the root of $-1$ of the chosen slice |
| the fundamental solution | $G_{\mathrm{fn}}$ | $\tilde R^{\natural}/\|\tilde R\|^{4}$ |
| the delta coefficient | $2\pi^{2}$ | the surface area of the unit three-sphere |
| the Cauchy formula | $\tilde\Xi(\tilde R_0)$ | boundary integral minus volume integral against $G_{\mathrm{fn}}$ |
| the residue | $\mathrm{Res}$ | the boundary integral at an isolated singularity |
| the first-order root | $\mathsf D$ | two-sided, with $\mathsf D^{2}=\Box I$ |
| the shift | $c$ | $\mathsf D_\lambda=\mathsf D+c\gamma_5$, $c^{2}=-\lambda$ |
| the pseudoscalar | $\gamma_5$ | the two-sided generator of the chirality |
| the chiral halves | $\psi_\pm$ | the two minimal left ideals $S_\pm=\mathbb{B}\tilde\Pi_\pm$ |
| the group of invertibles | $\mathbb{B}^{\times}$ | real dimension $8$ |
| the norm-one group | $\mathbb{B}^{\times}_1$ | real dimension $6$, centre $\{\pm e_t\}$ |
| the unit quaternions | $S^{3}$ | real dimension $3$, the maximal compact subgroup |
| the $*$-unitary group | $\mathrm{U}(2)$ | $S^{3}\cdot\mathrm{U}(1)/\{\pm(1,1)\}$ |
| the exponential | $\exp$ | the series and its closed form; the transform of this entry |
| the complex norm | $B$ | $\sqrt{Q_x^{2}+Q_y^{2}+Q_z^{2}}$, the discriminant of $\mathbb{C}[\tilde Q]$ |
| the eigenvalues | $\lambda_\pm$ | $Q_t\pm iB$ in the oscillatory regime |
| the material sector | $\mathbb{B}_{\Phi}$ | inertia $(3,1)$, hyperbolic |
| the informational sector | $\mathbb{B}_{\Psi}$ | inertia $(1,3)$, hyperbolic |
| the quaternion subspace | $\mathbb{B}_{H}$ | inertia $(4,0)$, elliptic |

## Further Reading

**The derivative.** [Biquaternion Analysis](../articles_maths/biquaternion-analysis.html) defines the gradient, its conjugate and the d'Alembertian, and states the two obstructions to differentiability; [Operator and Calculus Conventions](operator-and-calculus-conventions.html) fixes the glyphs and the two coordinate systems used above.

**The root.** [The First-Order Root of the Biquaternion D'Alembertian](../articles_maths/the-first-order-root-of-the-biquaternion-d-alembertian.html) proves the no-go for a root by left multiplication and builds the two-sided root from the two ideals; [The Operators of the Algebra](the-operators-of-the-algebra.html) is the chapter of operators on which that construction rests.

**The regular field.** [Biquaternion Regular Functions](../articles_maths/biquaternion-regular-functions.html) treats regularity, its shifted operator and its three branches; [Maxwell's Equations in the Biquaternionic Formulation](maxwells-equations-in-the-biquaternionic-formulation.html) gives the three-vector form of the material-sector condition and the retarded Green's function.

**The two-sided condition.** [The Two-Sided Derivative over the Biquaternion Algebra](../articles_maths/the-two-sided-derivative-over-the-biquaternion-algebra.html) states the rank-one criterion, the determinant identity, the eikonal and the general solution; [The Differentiable Field: One Primary Equation and the Linear Sector](the-differentiable-field-one-primary-equation-and-the-linear-sector.html) reads it in physics and states its price; [The Algebrodynamical Programme](the-algebrodynamical-programme-nonlinear-cauchy-riemann-conditions-self-quantized-charge-and-induced-causal-geometry.html) records the external programme in full.

**The completion.** [Fueter Theory for Biquaternions](../articles_maths/fueter-theory-for-biquaternions.html) proves Fueter's theorem, computes the affine kernel and states the Fueter–Sce hypotheses; [Biquaternion Analysis](../articles_maths/biquaternion-analysis.html), §*The Relation to Fueter and Clifford Analysis*, places the construction against the classical theory.

**The integral.** [Biquaternion Integration](../articles_maths/biquaternion-integration.html) proves the Cauchy formula and its consequences and states the residue theorem; [The Two Integrals: The Action and the Transform, Confronted Rung by Rung](../articles_internal/the-two-integrals-the-action-and-the-transform-confronted-rung-by-rung.html) puts the action integral and the transform integral side by side and locates the point where they meet.

**The sign patterns.** [Remarkable Subspaces and the Analysis](../articles_maths/remarkable-subspaces-and-the-analysis.html) gives the restriction table and the ellipticity criterion; [The Two Sectors: Split and the Four Bridges](the-two-sectors-split-and-the-four-bridges.html) reads the sectors as the two halves of the physical world.

**The group.** [Biquaternion Lie Group and Exponential Structure](../articles_maths/biquaternion-lie-group-and-exponential-structure.html) gives the exponential, the subgroups, the real forms and the Killing form; [The Group of Invertibles, the Cone and the Orders](the-group-of-invertibles-the-cone-and-the-orders.html) is the topology of the same group; [The Lorentz Group as Biquaternion Norm Automorphisms](the-lorentz-group-as-biquaternion-norm-automorphisms.html) reads the norm-one group as the group of the interval.

**The functions.** [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) computes the exponential, the logarithm with its lattice and the trigonometric functions; [Biquaternion Higher Special Functions](../articles_maths/biquaternion-higher-special-functions.html) collects the kernels and the functions defined by series.

**The next section.** [The Harmonic Analysis: The Transform as a Change of Description](the-harmonic-analysis-a-change-of-description.html) takes the exponential of a root of $-1$, builds the Fourier kernel from it and proves the inversion and Plancherel theorems that this entry does not state.

