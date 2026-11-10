# __The Fujikawa Method and the Path-Integral Anomaly in Biquaternionic Form__

## Introduction

The **Fujikawa method** derives the axial anomaly from the path integral rather than from a diagram. The observation is that the fermion measure is not invariant under a chiral rotation of the integration variables: the rotation is a linear change of variables whose Jacobian is a formal determinant, the determinant is infinite, and when it is regulated and evaluated it is not one. The anomaly is that Jacobian. The method makes the anomaly look like what it is — a property of the measure, not of the equations of motion — and it exhibits the coefficient as the weighted trace of the pseudoscalar against the heat kernel of the fermion operator.

The derivation has two facts and one regularisation.

- **A symmetry of the action.** A *global* right rotation $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}}\,e^{\alpha\omega}$ leaves the massless gradient equation invariant, because left and right multiplications commute. The exponent is the pseudoscalar $\omega=-\vec e_z$, so the two values of the field are multiplied by opposite phases: the rotation is the axial one and not a central phase, and the central $i$ stays free. A *local* rotation $\alpha(x)$ leaves the action invariant only up to a term proportional to $\partial\alpha/\partial R_\mu$, and that term is the axial current; the corresponding Ward identity is the classical one, and the anomaly is the correction to it.
- **A transformation of the measure.** The same rotation is a change of the integration variables $\tilde{Ξ}_{\mathrm{sp}},\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$, and the fermion measure $\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}\,\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$ picks up the inverse determinant of the rotation. That determinant is the whole story.
- **A regularisation.** The determinant is the product of the rotation's eigenvalues, one per mode, and it is divergent; it is regulated by a heat-kernel factor $\exp(-\mathcal{H}/M^2)$, evaluated as $M\to\infty$, and the finite remnant is the anomaly.

This article asks what the biquaternion framework supplies for this derivation. The answer is stated at the outset.

- **Supplied, and recomputed below.** The massless equation is one first-order equation in one field, $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=0$, and the massive equation is the chiral pair, because the square of the gradient with itself is not scalar. The two algebraic facts the derivation rests on are exact: $\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\Box$, and the chirality is the right multiplication by the pseudoscalar $\omega=-\vec e_z$, with $\omega^2=-e_t$, whose two values split the field into two halves of complex dimension two each. The symbol of the gradient is $-i\tilde K_{\Phi}=k_{t}^{\prime}-i\vec k_\Phi$, and on the null cone its left action on the six bivector components has rank four and a kernel of real dimension two, on which every bivector squares to zero. Those numbers are recomputed in §*The Symbol, the Cone and the Null Bivectors*, over five null wave vectors, with residual below $2\times10^{-14}$ at the level of the singular-value basis.
- **Translated once from the source.** The source's own equation is written with a derivative that carries one frame object per coordinate. Translated once, every derivative in this article is $\tilde\nabla$, the chirality stands on the right as a factor $\omega$, and the contraction is the form $\langle\tilde\nabla,\tilde J_{\Phi}\rangle_{\natural}$. The translation is fixed in §*The Gradient, the Pseudoscalar and the Two Values* and is not repeated; the source's form is not displayed.
- **Transcribed.** The measure, the Jacobian, the heat-kernel expansion, the Fujikawa coefficient and the index form of the integrated anomaly are standard. The measure is a functional-integral object and belongs to the corpus's general path-integral apparatus, which is cited and not rebuilt here.
- **Not supplied, and proved not to be.** The four-index symbol is not an object of the algebra. The chirality-weighted trace of the algebra over its four dimensions vanishes for every element, identically, because the pseudoscalar is odd under the quaternion conjugation; the insertion is taken on the right, the side the rotation acts on, and all $24$ orders of four distinct units give exactly zero. The density is therefore transcribed and not computed from an algebra trace, and §*Why the Symbol Is Not an Algebra Trace* states the theorem and what follows from it. What the algebra supplies in its place is the identification of the density with its own invariant $I_2=\vec E\cdot\vec B$, through the contraction $\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=+8\,\vec E\cdot\vec B$.
- **Gap, left visible.** The framework does not supply the functional measure: the algebra gives the operator whose determinant is taken, not the space of fields over which the integral runs. The chiral rotation itself is the axial symmetry of the linear chiral pair; the *anomaly* is the statement that this rotation is not a symmetry of the measure. The framework carries the rotation and the operator; the measure is imported.

A section fixes the gradient, the pseudoscalar and the two values, and gives the translation once. A section sets up the measure and the chiral rotation. A section computes the Jacobian with the heat-kernel regulator. A section proves that the four-index symbol is not an algebra trace and states the consequence. A section states what the symbol does on the null cone and computes the bivector kernel. A section states what the regulator must preserve and why the anomaly does not depend on it. A section compares the result with the triangle. A section extracts the coefficient and identifies the density. A section gives the integrated form and the index, and a section reads the rotation in the algebra. A section tabulates what is supplied, transcribed, and missing; the open questions follow; the summary and the notation table close the article.

**The frame and the symbols.** Every display below is read in the $\mathbb{B}_{\Phi}$ frame: its derivative, its coordinates and its metric are *Frame and Metric Conventions*, §*The $\mathbb{B}_{\Phi}$ Frame*, and are not restated here. The biquaternion gradient is
$$
\tilde\nabla=e_t\frac{\partial}{\partial R_t}+\vec e_x\frac{\partial}{\partial R_x}+\vec e_y\frac{\partial}{\partial R_y}+\vec e_z\frac{\partial}{\partial R_z},
\qquad
\tilde\nabla^{\natural}=e_t\frac{\partial}{\partial R_t}-\vec e_x\frac{\partial}{\partial R_x}-\vec e_y\frac{\partial}{\partial R_y}-\vec e_z\frac{\partial}{\partial R_z},
$$
and on $\mathbb{B}_{\Phi}$ the time derivative reads $\partial/\partial R_t=-i\partial/\partial r'_t$ (*Operator and Calculus Conventions*, §*The Gradient*). The d'Alembertian is the quaternionic norm of the gradient, $\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\partial^2/\partial R_t^2+\Delta_Q$, which on $\mathbb{B}_{\Phi}$ is $\Delta-\partial^2/\partial {r'_{t}}^2$. The pseudoscalar is $\omega=-\vec e_z$, with $\omega^2=-e_t$; it anticommutes with $\vec e_x$ and $\vec e_y$ and commutes with $\vec e_z$ (*Special Element Conventions*, §*The Chirality Convention*). A contraction of the derivative with a field is the quaternionic form $\langle\tilde\nabla,\tilde J_{\Phi}\rangle_{\natural}=\mathrm{Sc}(\tilde\nabla^{\natural}\tilde J_{\Phi})$, an explicit sum over the four coordinates. The chiral pair is written as two first-order equations,
$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R},
$$
on two elements of $\mathbb{B}$ (*Operator and Calculus Conventions*, §*The Two First-Order Equations and Their Symbol*); each line carries one gradient, the mass is the coupling of the two, and no letter is written for the two together. The pair operator that the corpus once wrote here is retired. The Dirac bilinear of two fields is written $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\xi=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*\xi\,i\vec e_x)$, with the fixed right multiplier $i\vec e_x$ standing after the product; it is not a derivative, and the multiplier is the same in every term below. The gauge covariant derivative is $D_\mu=\partial/\partial R_\mu+\frac{iϙA_{\mu}}{\hbar}$ with $[D_\mu,D_\nu]=\frac{iϙF_{\mu\nu}}{\hbar}$ for the abelian factor, and the gradient form is $\tilde D=\tilde\nabla+iϙ\tilde A_{\Phi}$. The fermion measure is written $\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}\,\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$. The four-index symbol is the orientation density of the series, taken positive on the identity order, and the field-strength components are $F_{ti}=E_i$ and $F_{ij}=+\epsilon_{ij\eta}B_\eta$, every index written low as the companion article writes it. The field invariants $I_1$ and $I_2$ are the instanton article's. Two traces appear below and are kept apart: $\mathrm{tr}$ is the trace of a complex-linear operator on the four coefficients of the field, and $\mathrm{Tr}$ is the functional trace over modes, which is what a determinant produces. Throughout, the constants are carried, with $c=1/\sqrt{\epsilon\mu}$ the speed of light in the medium and $c_0$ the vacuum value.

The framework results used here are those of the companion articles:

- Companion article *The Fermionic Path Integral in Biquaternionic Form*, for the functional integral and the fermion measure whose Jacobian is computed here.
- Companion article *Instantons and Solitons in Biquaternionic Form*, for the topological density and the winding of the gauge field.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the field strength and the invariants $I_1$ and $I_2$.
- Companion article *The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form*, for the one-sided gradient, the chiral pair, and the pseudoscalar.
- Companion article *Anomalies and Anomaly Cancellation in Biquaternionic Form*, for the diagrammatic derivation with which the result is compared.

## The Gradient, the Pseudoscalar and the Two Values

**Two equations, not one.** The framework carries two first-order equations, and they must not be read as one. The **gradient equation** is one-sided: the gradient acts by left multiplication on $\mathbb{B}$ and the field is a single element. The **chiral pair** is the same equation written for the two values separately, and it is the form in which a mass is allowed. The measure uses the second; the rotation uses the pseudoscalar, which is what the two values are the values of.

**The free equation.** The massless equation of the framework is
$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=0 ,
$$
one operator, one field, first order. This is the source's own equation translated once. The source writes its derivative with one frame object per coordinate; the translation of the time term is the $e_t\,\partial/\partial R_t$ term of $\tilde\nabla$ with $\partial/\partial R_t=-i\partial/\partial r'_t$, and the translation of each spatial term is the corresponding $\vec e_\eta\,\partial/\partial R_\eta$. Nothing is added and nothing is dropped. The translated form is the only form used below.

**The square of the gradient is not scalar.** The two products of the gradient with its conjugate are exact and scalar,
$$
\tilde\nabla\tilde\nabla^{\natural}=\sum_{\mu,\nu\in\{t,x,y,z\}}\varepsilon_\nu\,e_\mu e_\nu\frac{\partial^2}{\partial R_\mu\partial R_\nu}=\Box,
\qquad
\tilde\nabla^{\natural}\tilde\nabla=\Box ,
$$
because the terms with two distinct units annihilate one another: the factor $\varepsilon_\nu$ carries exactly the sign that exchanging the two orders requires. Diagonal terms give $\varepsilon_te_t^2\partial^2/\partial R_t^2+\sum_\eta\varepsilon_\eta e_\eta^2\partial^2/\partial R_\eta^2=\partial^2/\partial R_t^2+\Delta_Q$; mixed terms with one time index vanish because $e_t$ commutes with every unit and $\varepsilon$ is odd on the spatial indices; and mixed terms with two spatial indices vanish because distinct spatial units anticommute. The square of the gradient with itself has no such pairing, because $e_t$ commutes with every unit and the mixed time–space terms add instead of annihilating:
$$
\tilde\nabla^2=\Box-2\Delta_Q+2\sum_\eta\vec e_\eta\frac{\partial^2}{\partial R_t\partial R_\eta},
$$
which is not a scalar. Recomputed on the test field $f=Q_tQ_x+\tfrac{3}{10}Q_y^2-\tfrac{7}{10}Q_xQ_z+\tfrac12$ at $Q=(0.7,0.2,-0.4,0.9)$, the first identity leaves a residual of $3\times10^{-6}$ against $\Box f=0.599996$, and the second returns the scalar part $-0.6=\Box f-2\Delta_Qf$ together with a vector part $2.0\,\vec e_x=2\,\partial^2f/\partial R_t\partial R_x$.

**The consequence for the mass.** A single field cannot carry a mass at first order, because there is no scalar to subtract from a square that is not scalar. The massive equation is therefore the chiral pair, and it is the same dynamics written for the two values and not a second one:
$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R} .
$$
Each member acts by left multiplication, and the mass pairs the two values. Applied twice, the pair gives the scalar equation $\Box\tilde{Ξ}_{\mathrm{sp}}=k_m^{2}\tilde{Ξ}_{\mathrm{sp}}$ on each value, because $\tilde\nabla\tilde\nabla^{\natural}=\Box$. That is the whole of the mass, and it is why the article never writes a one-field first-order equation with a mass: in this algebra there is none. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

**The pseudoscalar.** The chirality of the frame is the element
$$
\omega=-\vec e_z,\qquad \omega^2=-e_t,\qquad \omega\omega^{\natural}=-e_t ,
$$
with $\omega^{\natural}=+\vec e_z=-\omega$. It anticommutes with $\vec e_x$ and $\vec e_y$ and commutes with $\vec e_z$; all three residues are exactly zero. It is the algebra's volume element: the frame's orientation density is its coordinate form, so $\omega$ is the element that carries the orientation. The source writes this object with a single letter $i$. That letter is $\omega$, not the central imaginary unit of the corpus: the two agree on no element of the algebra except the numbers, and the article keeps $\omega$ throughout so that the central $i$ stays free for the phases.

**The two values, and the side.** Right multiplication by $\vec e_z$ is a complex-linear operator on the four coefficients, and its eigenvalues are $\pm i$, each of multiplicity two. The field therefore splits into two halves of complex dimension two,
$$
\tilde{Ξ}_{\mathrm{sp},L}\vec e_z=-i\,\tilde{Ξ}_{\mathrm{sp},L},
\qquad
\tilde{Ξ}_{\mathrm{sp},R}\vec e_z=+i\,\tilde{Ξ}_{\mathrm{sp},R},
\qquad
\mathbb{B}=\mathbb{B}_L\oplus\mathbb{B}_R,
\qquad
\dim_{\mathbb{C}}\mathbb{B}_L=\dim_{\mathbb{C}}\mathbb{B}_R=2 ,
$$
and the two values are exactly two. The grading itself is $i$ times right multiplication by $\omega$: it takes the value $-1$ on $\tilde{Ξ}_{\mathrm{sp},L}$ and $+1$ on $\tilde{Ξ}_{\mathrm{sp},R}$, and it squares to the identity. **The insertion stands on the right.** The side is not a convention of printing: $\omega\vec e_x=-\vec e_y$ while $\vec e_x\omega=+\vec e_y$, so the left product and the right product are two different elements of the algebra, and only the right one is the chirality of the source's spin plane, which maps $\tilde{Ξ}_{\mathrm{sp}}$ to $-\tilde{Ξ}_{\mathrm{sp}}\vec e_z$.

**The axial rotation.** The rotation this article studies is the right multiplication
$$
\tilde{Ξ}_{\mathrm{sp}}\ \longmapsto\ \tilde{Ξ}_{\mathrm{sp}}\,e^{\alpha\omega}=\tilde{Ξ}_{\mathrm{sp}}\,(\cos\alpha+\omega\sin\alpha),
$$
with $\alpha$ a real parameter. It commutes with every left multiplication, hence with the gradient, and it is unitary because $\omega$ is anti-self-adjoint in the norm, $\omega^{\natural}=-\omega$. Its action on the two values is the pair of opposite phases
$$
e^{\alpha\omega}\tilde{Ξ}_{\mathrm{sp},L}=e^{+i\alpha}\tilde{Ξ}_{\mathrm{sp},L},
\qquad
e^{\alpha\omega}\tilde{Ξ}_{\mathrm{sp},R}=e^{-i\alpha}\tilde{Ξ}_{\mathrm{sp},R} ,
$$
recomputed on the two eigenspaces with residual below $10^{-10}$: the multipliers are $0.932327-0.361615\,i$ and $0.932327+0.361615\,i$ at $\alpha=0.37$, the two phases of one angle. The source's exponential is this one with $\alpha$ replaced by $-\alpha$, which is the sign its letter $i$ carries; the article keeps the sign above, and every sign below is computed from it.

## The Measure and the Chiral Rotation

**The generating functional.** For a biquaternion fermion field coupled to an abelian gauge field, the functional integral is
$$
Z[A] = \int \mathcal{D}\tilde{Ξ}_{\mathrm{sp}}\,\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\;\exp\!\left(i\int d^4r\;\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\bigl(\tilde D-m\bigr)\tilde{Ξ}_{\mathrm{sp}}\right),
$$
and the integral is Gaussian: it evaluates to the determinant of the operator,
$$
Z[A] = \det\begin{pmatrix}-k_m&\tilde D\\ \tilde D^{\natural}&-k_m\end{pmatrix} .
$$
The bosonic and fermionic measures, the Gaussian integration and the determinant are the subject of the corpus's fermionic path-integral article; that article constructs them and this one takes them as given. What the algebra supplies here is the operator whose determinant is taken: the two covariant gradients in one block array, whose determinant reduces to $\Box-k_m^{2}$ on one value and whose value is the product over modes of $\det\ell_{-i\tilde K_{\Phi}}=(k_{t}^{\prime\,2}-\lvert\vec k_\Phi\rvert^2)^2$ for one chiral value — the square of the symbol of the d'Alembertian, which is the Dirac determinant — and the square of that for the pair, one factor for each value. The mass is the coefficient that the condensate of the companion article fixes.

**The chiral rotation.** Rotate the integration variables by an axial phase that is local,
$$
\tilde{Ξ}_{\mathrm{sp}}(x)\ \longmapsto\ \tilde{Ξ}_{\mathrm{sp},2}(x)=\tilde{Ξ}_{\mathrm{sp}}(x)\,e^{\alpha(x)\omega},
\qquad
\tilde{Ξ}_{\mathrm{sp}}^{\dagger}(x)\ \longmapsto\ \tilde{Ξ}_{\mathrm{sp},2}^{\dagger}(x)=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}(x)\,e^{\alpha(x)\omega},
$$
with $\alpha$ a real scalar function. The exponent is a right multiplication by an element that squares to minus the identity, so the rotation is the exponential of the pseudoscalar and not of a phase: $e^{\alpha\omega}=\cos\alpha\,\mathbb 1+\sin\alpha\,\omega$, with $\mathbb 1$ written for $e_t$ when it multiplies a coefficient. The rotation is unitary and it leaves the norm of the field unchanged.

**The massless kinetic term is invariant.** Left and right multiplications commute, so a constant rotation passes through the gradient,
$$
\tilde{Ξ}_{\mathrm{sp},2}^{\dagger}\,\tilde D\,\tilde{Ξ}_{\mathrm{sp},2}
=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}e^{\alpha\omega}\,\tilde D\,(\tilde{Ξ}_{\mathrm{sp}} e^{\alpha\omega})
=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\,\tilde D\,\tilde{Ξ}_{\mathrm{sp}}\,e^{2\alpha\omega},
$$
and the last factor is a constant element of the algebra. For the *global* rotation the equation $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=0$ is invariant exactly and not to first order, since $\tilde\nabla(\tilde{Ξ}_{\mathrm{sp}} e^{\alpha\omega})=(\tilde\nabla\tilde{Ξ}_{\mathrm{sp}})e^{\alpha\omega}$. That is the sharpest form of the statement that the axial rotation is a symmetry of the massless action, and it uses no anticommutator of frame objects, only the associativity of the algebra and the commutation of the two sides.

**The local rotation produces the current.** When $\alpha$ depends on position the derivative falls on it,
$$
\tilde{Ξ}_{\mathrm{sp},2}^{\dagger}\,\tilde D\,\tilde{Ξ}_{\mathrm{sp},2}
=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\,\tilde D\,\tilde{Ξ}_{\mathrm{sp}}
+i\,\bigl\langle\tilde\nabla\alpha,\tilde J_{\Phi,5}\bigr\rangle_{\natural}
+O(\alpha^2),
\qquad
\tilde J_{\Phi,5}\ \text{the axial current},
$$
because the derivative of the rotation at $\alpha=0$ puts $\omega$ on the right of each of the four components of $\tilde\nabla\alpha$. The pseudoscalar therefore stands on the right of the field, exactly where the chirality belongs, and the contraction is the explicit sum $\langle\tilde\nabla\alpha,\tilde J_{\Phi,5}\rangle_{\natural}=\sum_\mu(\partial\alpha/\partial R_\mu)J_{5\mu}$, per the corpus's rule that a contraction names its index. Under the *global* rotation the term is absent, which is the classical statement. A mass term is not invariant,
$$
\tilde{Ξ}_{\mathrm{sp},2}^{\dagger}\,k_m\,\tilde{Ξ}_{\mathrm{sp},2}=k_m\,\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\tilde{Ξ}_{\mathrm{sp}}\,e^{2\alpha\omega}
=k_m\,\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\bigl(\cos2\alpha\,\mathbb 1+\sin2\alpha\,\omega\bigr)\tilde{Ξ}_{\mathrm{sp}},
$$
which is the classical explicit breaking of the axial symmetry, and the doubling of the angle is the identity $e^{2\alpha\omega}=\cos2\alpha+\sin2\alpha\,\omega$. In the framework's language the rotation is exactly the axial symmetry of the linear chiral pair: the central phase passes through the mass term and this one does not.

**The classical Ward identity, and the question.** Classically the massless action is invariant under the global rotation, and Noether's theorem gives the conservation of the axial current on the equations of motion,
$$
j_{5\mu}=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\,\omega\,\vec e_\mu\,\tilde{Ξ}_{\mathrm{sp}},
\qquad
\langle\tilde\nabla,\tilde J_{\Phi,5}\rangle_{\natural}=0\quad(\text{on shell}),
$$
with the pseudoscalar between the two fields and the unit on the second factor. The vector current is the same bilinear without the pseudoscalar, $j_\mu=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\vec e_\mu\tilde{Ξ}_{\mathrm{sp}}$, and the two rotate into one another as a two-vector: recomputed at $\alpha=0.41$ on a random complex field, the vector current of the rotated field equals $\cos2\alpha\,j_\mu+\sin2\alpha\,j_{5\mu}$, and the axial current of the rotated field equals $-\sin2\alpha\,j_\mu+\cos2\alpha\,j_{5\mu}$, both to the five decimals printed. The *local* rotation is not a symmetry — it fails by exactly the current term displayed above, and that failure is what identifies the current. The Ward identity is the global statement read locally. The quantum question is whether the *measure* is invariant under the same change of variables. It is not, and the failure is the anomaly.

**Why the measure can fail.** A change of integration variables in a finite-dimensional integral multiplies the measure by the Jacobian determinant, regardless of whether the integrand is invariant. A symmetry of the action is therefore not automatically a symmetry of the integral; it is a symmetry only if the Jacobian is one. The chiral rotation of a fermion field is a change of variables whose Jacobian is not one, and no local counterterm can restore it. That is why the anomaly is a property of the measure, and why the diagrammatic and path-integral derivations must agree.

## The Jacobian and the Regulated Trace

**The Jacobian.** Write the rotation as a linear map on the space of fields, $\tilde{Ξ}_{\mathrm{sp},2}=\tilde{Ξ}_{\mathrm{sp}} e^{\alpha\omega}$, and the same rotation on $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$. The measure transforms by the inverse determinants,
$$
\mathcal{D}\tilde{Ξ}_{\mathrm{sp},2}\,\mathcal{D}\tilde{Ξ}_{\mathrm{sp},2}^{\dagger} = \bigl(\det U\bigr)^{-2}\,\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}\,\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}^{\dagger},
\qquad
U=e^{\alpha\omega},
$$
and the regulated logarithm is
$$
\ln\det U=\mathrm{Tr}\ln U=i\,\mathrm{Tr}\bigl(\alpha\,\omega\bigr)_{\mathrm{reg}}
=i\int d^4r\,\alpha(x)\,\mathrm{tr}\bigl[\rho_\omega\,e^{-\mathcal{H}/M^2}\bigr]_x .
$$
The subscript on $\rho$ is the side, and it is not decoration. The rotation of §*The Measure and the Chiral Rotation* multiplies on the right, so the insertion is the right multiplication $\rho_\omega$; the heat kernel is a left action, since $\mathcal{H}$ is built from $\tilde D$ and its conjugate. The composite is therefore one left and one right multiplication, which is the shape of a basis operator. At coincidence its kernel is the composite $\ell_h\rho_\omega$ of §*Why the Symbol Is Not an Algebra Trace*, and the trace of that section is the trace written here. The side is what decides the value: with the insertion on the left, the same display would give $4\,\mathrm{Sc}(\omega h)$ and not zero.

Hence
$$
\bigl(\det U\bigr)^{-2}=\exp\!\left(-2i\int d^4r\,\alpha(x)\,a(x)\right),
\qquad
a(x)=\lim_{M\to\infty}\mathrm{tr}\bigl[\rho_\omega\,e^{-\mathcal{H}/M^2}\bigr]_x .
$$
The factor $2$ in the exponent is the two determinants, one for $\tilde{Ξ}_{\mathrm{sp}}$ and one for $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$, and $a$ is the regulated trace at coincidence. Matching the measure factor against the change of the action, $\delta S=-\int d^4r\,(\partial\alpha/\partial R_\mu)\,j_{5\mu}=\int d^4r\,\alpha\,\sum_\mu\partial j_{5\mu}/\partial R_\mu$, gives $\langle\tilde\nabla,\tilde J_{\Phi,5}\rangle_{\natural}=\sum_\mu\partial j_{5\mu}/\partial R_\mu=2a$. The anomaly density is therefore $A=2a$. The trace $a$ is the index density of the standard module, since $\int a=-(ϙ^2/32\pi^2)\int d^4r\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ in the normalization of the index section; that is why $\int A=2\int a$ is twice the index up to the sign that the all-low-index symbol carries, the factor two coming from the two determinants and not from the trace. The determinant is formal and divergent: it is the product of the eigenvalues of $U$ over a complete set of modes, one per spacetime point.

**The regulator.** To make the determinant finite and preserve gauge invariance, one regulates it with the square of the operator. Each line composed with the conjugate of the other is $\Box$, so the regulator is the d'Alembertian itself with the connection included,
$$
\mathcal{H}=-(\tilde D\tilde D^{\natural})_E ,
$$
whose scalar part is $-\Box_E$ and whose remaining part is a bivector built from the commutator $[D_\mu,D_\nu]=iϙF_{\mu\nu}$. The subscript $E$ is the continuation on which $\mathcal{H}$ has no negative eigenvalue and $\exp(-\mathcal{H}/M^2)$ converges: each spatial derivative is multiplied by $i$ and the time derivative is left alone. The continuation changes no coefficient, and it does not touch the pseudoscalar: $\omega$ is an element of the algebra and the continuation acts on the coordinates. Choosing a complete set of modes $\{\xi_n\}$ of $\mathcal{H}$, with $\mathcal{H}\xi_n=\lambda_n\xi_n$ and $\lambda_n\ge0$, the regulated trace is the coincidence value of the heat kernel. In the standard fermion module the divergent orders drop out before the limit is taken: at coincidence the heat kernel expands as $M^4/16\pi^2$ times the identity, plus an $M^2$ term proportional to the bivector of the field strength, plus an $M^0$ term proportional to its square. The first is annihilated by $\mathrm{tr}(\rho_\omega)$ and the second by $\mathrm{tr}(\ell_V\rho_\omega)$, both of which vanish in either module, so only the finite order survives the trace and nothing has to be subtracted by hand. The $M^4$ and $M^2$ divergences are still there in the determinant; it is the weighted trace that removes them. That construction is Fujikawa's and is standard. What the framework contributes is the operator inside it, and, as §*Why the Symbol Is Not an Algebra Trace* proves, not the trace: in $\mathbb{B}$ the same vanishing that removes the divergent orders removes the finite one too, and the weighted trace is identically zero.

## Why the Symbol Is Not an Algebra Trace

**The theorem.** For every element $h$ of the algebra, the trace of a left multiplication composed with the chirality insertion vanishes:
$$
\mathrm{tr}\bigl(\ell_h\,\rho_\omega\bigr)=0\qquad\text{for every }h\in\mathbb{B},
$$
where $\ell_h$ denotes left multiplication by $h$, $\rho_\omega$ right multiplication by the pseudoscalar, and the trace runs over the four complex coefficients. The composite $\ell_h\rho_\omega$ is a product of one left and one right multiplication, and it is the only two-sided shape the article uses: the regulated trace of §*The Jacobian and the Regulated Trace* is the same shape at coincidence. Both elements are named here because the vanishing below is what that shape does, and every other operator in the article is one-sided. The proof is one line. On coefficient columns $\mathrm{tr}(\ell_h\rho_b)=2\,\mathrm{Sc}(hb)+2\,\mathrm{Sc}(h\,b^{\natural})$ for every $b$, verified exactly on the sixteen basis pairs and to $3\times10^{-15}$ on six random complex pairs; at $b=\omega$ the two terms are opposite, because $\omega^{\natural}=-\omega$, so their sum is zero. The vanishing is not a property of the regulator, of the field strength or of the continuation: it holds element by element.

**The side decides the value.** Putting the insertion on the other side changes the answer, so the subscript on $\rho$ is load-bearing. The same computation gives
$$
\mathrm{tr}\bigl(\ell_\omega\,\ell_h\bigr)=\mathrm{tr}\bigl(\ell_{\omega h}\bigr)=4\,\mathrm{Sc}(\omega h),
$$
which is zero only when $\omega h$ has no scalar part: at $h=\vec e_z$ the product is $\omega\vec e_z=e_t$ and the trace is $4$. Recomputed, the right-inserted trace is exactly $0$ for $h$ equal to $e_t$, $\vec e_x$, $\vec e_y$ or $\vec e_z$, and the left-inserted one is $0$ at the first three and $4$ at $h=\vec e_z$. The rotation of this article multiplies the field on the right, so $\rho_\omega$ is the insertion the anomaly would need, and it is the one that vanishes.

**The check, on the powers that matter.** The identity was recomputed in the forms in which the heat-kernel expansion would use it. All $24$ orders of the four distinct units give exactly $0$; the products of one, two and three units give exactly $0$; the four basis elements give exactly $0$; and the field-strength element $V=\sum_{\mu<\nu}e_\mu e_\nu F_{\mu\nu}$, together with its square $V^2$, gives exactly $0$. No polynomial in the units and the field strength can produce a non-zero chirality-weighted trace, and the count is the same for the left insertion on every product of three or four units, which is the form the four-index symbol takes.

**Why the frame object was needed, and what its retirement costs.** The four-index symbol is antisymmetric in four indices, so it needs four independent directions that a trace can see. In the algebra the product of four distinct units is $\pm e_t$ or $\pm\vec e_\eta$ and never a multiple of the pseudoscalar, so the pseudoscalar has no coefficient in it and the chirality-weighted trace is blind to it. What the source used to see it was an operator that multiplies on both sides at once, so that four directions and the chirality could meet in one product of operators. That object is a frame object and not an element of the algebra; the migration retires it, and with it goes the ability to read the four-index symbol off a trace. The corpus states the same limitation from the element side: an element has one slot, its position in the product, and the chirality operator of a frame is an operator of that frame and not an element at all (*Special Element Conventions*, §*The Chirality Convention*).

**What follows.** The coefficient of the anomaly is *transcribed*, not computed from an algebra trace. The value of the regulated trace in the four-dimensional fermion module is the standard one,
$$
a(x)=-\frac{ϙ^2}{32\pi^2}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma},
$$
and it is quoted from the literature of §*Further Reading*, not re-derived here. The minus is the orientation bookkeeping of the all-low-index symbol that the corpus writes, and the companion article states the same minus at its result. The framework's own statement is the one in §*The Coefficient, the Density, and the Framework*: that the contraction is $+8$ times its invariant $I_2$ and the density minus that, up to the same bookkeeping, and that the index density is the second Chern character of the gauge field whose biquaternion form the instanton article computes. The article says plainly which of the two it is doing at each step, and it does not present a transcribed coefficient as an algebra result.

## The Symbol, the Cone and the Null Bivectors

**The symbol.** Replacing each derivative of the gradient by $ik_{\Phi,\mu}$ turns the operator into an element, its *symbol*. On the material sector, where $\partial/\partial R_t=-i\partial/\partial r'_t$ and a plane wave carries $e^{i(k_{t}^{\prime}x_0-\vec k_\Phi\cdot\vec q)}$ with $x_0=r'_{t}$, the substitution gives
$$
-i\tilde K_{\Phi}=k_{t}^{\prime}-i\vec k_\Phi=k_{t}^{\prime}-i\,(k_x\vec e_x+k_y\vec e_y+k_z\vec e_z),
\qquad
(-i\tilde K_{\Phi})^{\natural}(-i\tilde K_{\Phi})=k_{t}^{\prime\,2}-\lvert\vec k_\Phi\rvert^2 .
$$
The identity is the biquaternion norm of the symbol, and it is the symbol of the d'Alembertian: recomputed, the product is $3$ at $k=(2,1,0,0)$ and $0$ at $k=(1,1,0,0)$, matching $k_{t}^{\prime\,2}-\lvert\vec k_\Phi\rvert^2$ in both cases.

**The determinant of the gradient.** Left multiplication by $-i\tilde K_{\Phi}$ is a complex-linear operator on the four coefficients, and its determinant is the square of the scalar symbol,
$$
\det \ell_{-i\tilde K_{\Phi}}=\bigl(k_{t}^{\prime\,2}-\lvert\vec k_\Phi\rvert^2\bigr)^2 ,
$$
recomputed as $9$ at $k=(2,1,0,0)$. It is singular exactly when $k$ is null, and there its rank is two: at $k=(1,1,0,0)$, $(1,0,1,0)$, $(1,0,0,1)$ and $(3,1,2,2)$ the rank is $2$, and off the cone at $k=(2,1,0,0)$ it is $4$. A gradient plane wave is annihilated by the gradient exactly when the wave vector is null, which is the light cone and nothing else.

**The six bivector components.** The bivectors of the algebra are the six elements $\vec e_x,\ \vec e_y,\ \vec e_z,\ i\vec e_x,\ i\vec e_y,\ i\vec e_z$, the three spacelike and the three timelike ones, and a bivector field is a real combination $f$ of them. This is the sector the field strength occupies: $\tilde F$ is a bivector, and so is its square.

**The kernel on the null cone.** Left multiplication by a null symbol maps that six-dimensional real space into the four-dimensional algebra, and the image has dimension four. The kernel is therefore two-dimensional, and it consists of null bivectors. Recomputed for five null wave vectors, with an off-cone row as control:
$$
\begin{array}{c|c|c|c}
k & \text{rank} & \dim\ker & \lvert f^2\rvert\ \text{on the kernel}\\ \hline
(2,1,0,0) & 6 & 0 & \text{empty}\\
(1,1,0,0) & 4 & 2 & 4.4\times10^{-16},\ 2.2\times10^{-16}\\
(1,0,1,0) & 4 & 2 & 2.2\times10^{-16},\ 3.3\times10^{-16}\\
(1,0,0,1) & 4 & 2 & 2.2\times10^{-16},\ 2.2\times10^{-16}\\
(2,1,1,\sqrt2) & 4 & 2 & 1.2\times10^{-16},\ 2.6\times10^{-16}\\
(1,0.6,0.8,0) & 4 & 2 & 1.5\times10^{-14},\ 2.8\times10^{-16}
\end{array}
$$
**How to read the table.** The first row is the off-cone control: the symbol is invertible on the bivectors and the kernel is empty. The rank is four and the kernel is two for every null wave vector, and $f^2=0$ on the whole kernel. Two real dimensions is one complex dimension: the bivector sector carries exactly one surviving polarisation on the cone, and the bivector that survives is null in the algebra's own product.

**What the kernel says.** A bivector whose square vanishes is a radiation field: for $\tilde F=i\sqrt\epsilon\,\vec E-\sqrt\mu\,\vec H$ the square is $-\mu(\lvert\vec H\rvert^2-\epsilon\lvert\vec E\rvert^2)+2i\sqrt{\epsilon\mu}\,\vec E\cdot\vec H$, which vanishes exactly when the two fields are orthogonal and equal in magnitude. So the algebra's own statement about a null wave is that its field strength is a null bivector, and the null bivectors are precisely the components that the gradient annihilates on the cone. That is the framework's content in the sector where the index density lives, and it is what this article recomputes in place of the source's four-object trace.

## The Regulator and the Symmetry It Preserves

**Why the regulator is part of the argument.** The Jacobian is a product of infinitely many eigenvalues, and any statement about it requires a prescription that makes the product finite. The prescription is not innocent. A naive momentum cutoff, for instance, breaks the gauge invariance of the fermion determinant, and the gauge non-invariance it introduces is indistinguishable, at the level of the regulated determinant, from a genuine anomaly. The Fujikawa regulator is chosen to preserve gauge invariance: the heat-kernel factor $\exp(-\mathcal{H}/M^2)$ is built from the gauge-covariant operator, so it commutes with the gauge transformations, and every breaking it produces is attributable to the inserted pseudoscalar and not to the cutoff. The anomaly is then the *entire* failure of the axial symmetry of the measure, with no spurious part.

**The continued frame, declared.** The heat kernel is computed on the continuation where the spatial derivatives are multiplied by $i$ and the operator's spectrum has no negative part. That continuation is a computational device and not a second physics: it is the sheet on which $\exp(-\mathcal{H}/M^2)$ converges, and it changes no coefficient. It is semi-definite and not definite, since the zero modes that carry the index are exactly the kernel of $\mathcal{H}$. The pseudoscalar is untouched by it, because the continuation acts on the coordinates and $\omega$ is an element.

**Regulator independence.** Different gauge-invariant regulators give the same anomaly. Two such regulators differ by a local counterterm in the effective action, and a local counterterm cannot reproduce the anomaly: removing it would require a local functional whose gauge variation is the anomaly itself, and no local functional has that variation. That obstruction is the Wess–Zumino consistency condition, and it is what makes the coefficient a pure number rather than a function of the cutoff. The total-derivative form makes the same point locally: the density integrates to a topological charge, and a local counterterm would have to shift a topological charge, which no local functional does. The regulator's job is only to expose the finite remnant; it does not choose it.

**The heat-kernel weight and the insertion.** Two features of the construction are worth separating. The heat-kernel factor $\exp(-\mathcal{H}/M^2)$ suppresses the high modes and produces the expansion in inverse powers of $M$ whose coefficients are the Seeley–DeWitt terms; it is a gauge-invariant regulator. The insertion of the pseudoscalar is what makes the trace a weighted one; it is not a regulator and is the origin of the anomaly. In the framework's terms the division of labour is the same: $\mathcal{H}$ is built from the covariant gradient of the pair and acts on the left, and $\omega$ is the element inserted on the right, the side the rotation acts on, before the trace of the composite is taken.

## Comparison with the Diagrammatic Derivation

**The two computations agree, as they must.** The companion article on anomalies computes the divergence of the axial current from the triangle diagram, with one axial and two vector insertions, and obtains the Adler–Bell–Jackiw coefficient. This article obtains the same coefficient as the Jacobian of the measure. Two notational differences separate the two pages and neither touches the coefficient: the charge, which the companion writes $e$ in its result and $ϙ$ in its current, and this article writes $ϙ$ throughout, and the time index, which the companion writes $r'_t$ and this article writes $t$ for the frame's time coordinate. The contraction, its $+8$, its minus, and the identification with $\vec E\cdot\vec B$ are the same on both pages. The agreement is not a coincidence: both reduce to the same four-index contraction. The triangle computes it against three current insertions; the heat kernel computes it against the squared operator's field-strength term. The contraction is the same, so the coefficient is the same.

**What each derivation explains.** The diagrammatic derivation explains *what* the anomaly is as a physical process: a triangle of fermions with an axial current and two gauge currents, finite and unrenormalised. The path-integral derivation explains *why* it is unavoidable: the measure is not invariant under the symmetry, and no choice of regulator removes a symmetry the measure does not have. The second explanation is the deeper one, and it is why the anomaly survives any dynamics that leaves the measure intact: confinement, a condensate, or a change of degrees of freedom cannot remove it, which is the content of anomaly matching.

**One-loop exactness from the measure.** The Adler–Bardeen theorem is transparent in the path-integral language: the Jacobian is a one-loop determinant, because the measure's transformation is computed at the Gaussian level, and there is no higher loop in which to correct it. Regulator independence then promotes the one-loop value to an exact statement. The triangle derivation gives the same protection only after the theorem is proved diagram by diagram; the measure gives it as a structural fact. Neither route is special to the biquaternion algebra, and both are transcribed.

## The Coefficient, the Density, and the Framework

**The coefficient factorises.** The Fujikawa coefficient factorises exactly as the triangle coefficient did: a four-index contraction, which produces $+8\,\vec E\cdot\vec B$ in the conventions of the introduction, and a field-strength product, which produces $F_{\mu\nu}F_{\rho\sigma}$. The four-dimensional heat-kernel coefficient supplies the $1/16\pi^2$. Nothing in the factorisation uses a property of a specific gauge group; the abelian computation above generalises to the non-abelian case by replacing $ϙ^2F_{\mu\nu}F_{\rho\sigma}$ with the trace of the field-strength square over the gauge factor and the coefficient by the appropriate Casimir, which is the standard non-abelian Fujikawa result.

**The density is the invariant $I_2$.** The contraction is
$$
\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = +8\,\vec E\cdot\vec B,
$$
evaluated directly with $F_{ti}=E_i$ and $F_{ij}=+\epsilon_{ij\eta}B_\eta$; hence
$$
\boxed{\;A(x) = -\frac{ϙ^2}{16\pi^2}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
= -\frac{ϙ^2}{2\pi^2}\,\vec E\cdot\vec B
= -\frac{ϙ^2}{2\pi^2}\,I_2\;},
$$
so the density is a constant times the framework's second invariant $I_2$ of the biquaternion field strength $\tilde{F}=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$, in the normalization of the instanton article. The constant $+8$ belongs to the contraction above and not to the box: it is the same $+8$ the companion article carries, both pages writing every index low, and its minus in front of the contraction is the bookkeeping it names at its result. The invariant $I_2=\vec E\cdot\vec B$ is the shared object; the numerical factor belongs to the contraction, and the minus to the index orientation. The anomalous divergence therefore flows into the framework's own pseudoscalar invariant, and the density is odd under the interchange of the two parts named by the subscript for the same reason $I_2$ is; the topological character noted in the companion article is the total-derivative form of the same contraction.

**Why the pseudoscalar is the orientation.** The identity that makes the computation a statement about the algebra is that the axial insertion is the pseudoscalar: the product of the three vector units is $\vec e_x\vec e_y=\vec e_z=-\omega$, so $\omega$ is the orientation of the frame up to its sign, and $\omega^2=-e_t$ is the statement that the orientation is a square root of minus the identity. The two values a field can take are the two eigenvalues of $i$ times right multiplication by that element, and the operator that assigns them is the basis operator $-iR_{\omega}$. The antisymmetric symbol is the coordinate form of the frame's orientation — the table of its signs against the four coordinate directions — and it is exactly the part that needs both sides of a product, which is why the trace of §*Why the Symbol Is Not an Algebra Trace* cannot recover it. The axial and the vector rotation differ only by the element inserted: the vector rotation has $\ln U=i\alpha\,\mathbb 1$ and inserts the identity, the axial rotation has $\ln U=\alpha\,\omega$ and inserts the pseudoscalar. The anomaly is the statement that the pseudoscalar insertion is not a symmetry of the measure, while the identity insertion is — and, as §*Why the Symbol Is Not an Algebra Trace* proves, the *trace* of that insertion is not available in the algebra even though the element is.

**Where the $1/16\pi^2$ comes from.** The coefficient is a four-dimensional Gaussian, and it can be read off before any element is touched. In the coincidence limit the free heat kernel is
$$
\big\langle r_x\big|\exp(-\partial^2/M^2)\big|r_x\big\rangle
= \int\frac{d^4p_E}{(2\pi\hbar)^4}\,\exp(-p_E^2/(\hbar^2M^2))
= \frac{M^4}{16\pi^2},
$$
using $\int d^4p_E\,\exp(-p_E^2/(\hbar^2M^2))=(\pi\hbar^2M^2)^2=\pi^2\hbar^4M^4$ and dividing by $(2\pi\hbar)^4=16\pi^4\hbar^4$. The regulator $M$ is an inverse length, the wave number of the cutoff, because $\partial^2/M^2$ in the exponent must be a pure number and every derivative carries an inverse length; the two powers of $\hbar$ it carries are what leave the kernel an inverse four-volume. The powers of $M$ then balance, and the balance is worth displaying because it is where the $1/32\pi^2$ of the density is fixed. Write $\mathcal{H}=\mathcal{H}_0+V$, with $\mathcal{H}_0$ the scalar operator $-\partial^2$ and $V$ the field-strength part, a bivector element that acts by left multiplication and is built from $[D_\mu,D_\nu]=iϙF_{\mu\nu}$. Each insertion of $V$ brings one factor $1/M^2$ and one free propagator, so the second-order term of the heat kernel carries
$$
\frac{1}{2!\,M^4}\ \text{for the two insertions},\qquad
\frac{M^4}{16\pi^2}\ \text{for the coincidence kernel},
$$
and the two combine to $\tfrac12\cdot M^{-4}\cdot M^4/16\pi^2=1/32\pi^2$. Two insertions bring four units, and in the standard four-component module the trace over them is the four-index contraction above: $V^2$ carries $(-\tfrac{iϙ}{2})^2=-\tfrac{ϙ^2}{4}$, and the two imaginary units of the measure's exponent and of that square combine into a real density. The $M^4$ of the Gaussian and the two $M^{-2}$ of the insertions balance exactly; that balance is why the anomaly is finite and regulator independent, while a term with a different number of insertions would leave a power of $M$ behind and vanish or diverge. The same Gaussian appears in the Seeley–DeWitt expansion of the covariant sum of squares, where the coefficient is the second Seeley–DeWitt term; the anomaly uses only the field-strength part of that term. In $\mathbb{B}$ the last step is the one that fails, and not the Gaussian: the four-index contraction is what the standard module's trace supplies, and §*Why the Symbol Is Not an Algebra Trace* shows that the chirality-weighted trace of the algebra is zero for every element. The coefficient is transcribed for that reason and for no other.

## The Integrated Form and the Index

**The integral of the density.** The integrated anomaly is a topological invariant. In the massless theory, where the divergence is the anomaly alone, the total-derivative form and the index of the operator give
$$
\int d^4r\,\langle\tilde\nabla,\tilde J_{\Phi,5}\rangle_{\natural}
= \int d^4r\,A(r_x)
= -\frac{ϙ^2}{16\pi^2}\int d^4r\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
= -2\,(n_L-n_R),
$$
so the axial charge transported in a background is twice the index, the minus being the orientation bookkeeping of the all-low-index symbol that the density carries throughout the article. The index is the excess of the number of zero modes of value $L$ over the number of value $R$; the general theorem identifying it with the integral is Atiyah–Singer. The zero-mode count and the index theorem belong to the corpus's general gauge apparatus and are not developed here; the fermion-sector facts are that the integral is an integer, that the coefficient is therefore protected against renormalisation, and that a background of unit topological charge produces a net axial-charge violation.

**The zero modes and the measure.** The index interpretation makes the Fujikawa computation transparent. The rotation acts on each mode by a phase; modes of the two values are rotated with opposite phases; the regulator counts them with the heat-kernel weight; and a mismatch between the numbers of zero modes of the two values is a non-zero difference that no regulator can remove. The anomaly is that mismatch seen through the measure. In the framework's terms the mismatch is a property of the two-line operator in a background with non-zero topological charge, and the topological charge is the winding of the material-sector connection.

**One instanton.** For a unit instanton the index is one per flavour and the axial charge changes accordingly. The factor of two in front of the index is the one already identified at the measure: two determinants, one for $\tilde{Ξ}_{\mathrm{sp}}$ and one for $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$. Equivalently, the bilinear that soaks up a zero mode is $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\tilde{Ξ}_{\mathrm{sp}}$, whose axial charge is two, so a single zero mode of one value shifts the axial charge by two units. A mode and its partner of the other value enter the trace with opposite signs, so their contributions annihilate when the index vanishes, and the integral turns on the difference. Nothing here is particular to the biquaternion algebra except the identification of the winding with the material sector and of the density with $I_2$.

**The two rotations compared.** The framework's two continuous symmetries of the massless equation behave differently in the measure, and the difference is exact. The **vector** rotation $\tilde{Ξ}_{\mathrm{sp}}\mapsto e^{i\alpha}\tilde{Ξ}_{\mathrm{sp}}$ is multiplication by a central element: it rotates the two values in the same sense, and it is exactly what a gauge transformation does to the field. Because the regulator is gauge invariant, the trace its Jacobian produces is the one *without* the pseudoscalar, and that trace is even under the interchange of the two index pairs, so it contracts to $F_{\mu\nu}F_{\mu\nu}$ and never to $\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$. An even local term is absorbed by the counterterms that define the effective action, so the divergence of the vector current is not corrected. In a chiral gauge theory the same distinction appears as the cubic charge sum $\sum_LQ^3-\sum_RQ^3$, which vanishes for a vector-like spectrum. The **axial** rotation inserts the pseudoscalar; it rotates the two values oppositely, its leftover is $\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$, and no local counterterm with the symmetries of the theory absorbs it. Only the second rotation is anomalous. In the framework's terms the mass term and the measure agree about which phase is broken: the linear chiral pair conserves the central phase and breaks the axial one at the classical level, and the measure breaks the same axial phase once more at the quantum level. The two breakings add, and their sum is the ABJ divergence.

**The index density.** The relation above can be written locally. The four-dimensional index density is proportional to $\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$, the second Chern character of the gauge field, and its integral is the topological charge whose biquaternion form the companion article on instantons computes from $I_2$. The chain is therefore: the rotation inserts the pseudoscalar; the symbol's bivector sector, on the cone, keeps one null polarisation and annihilates the rest; the field-strength contraction turns that survivor into the second invariant; and the integral of the invariant is the winding of the material-sector connection. Every link but the second is a statement the algebra makes, and the second is the one §*Why the Symbol Is Not an Algebra Trace* withholds.

## The Chiral Rotation in the Biquaternion Language

**The rotation is the axial symmetry of the linear chiral pair.** The rotation $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}} e^{\alpha\omega}$ rotates the parts of the two values in opposite directions, because the multiplier is $-1$ on $\tilde{Ξ}_{\mathrm{sp},L}$ and $+1$ on $\tilde{Ξ}_{\mathrm{sp},R}$ in the grading sense, and multiplies them by $e^{+i\alpha}$ and $e^{-i\alpha}$ in the phase sense. It is the axial phase whose breaking was treated in the companion article on the condensate; there the breaking was spontaneous and belonged to the vacuum, here it is explicit and quantum-mechanical. The two are different phenomena acting on the same symmetry, and the framework keeps them distinct: the condensate supplies a coefficient to the linear chiral pair, and the anomaly violates the axial current even when the coefficient is zero.

**The angle is a central scalar, the generator is an element.** The rotation parameter is a real scalar function of position, hence a central element of the algebra times a function; it is the same kind of object as the gauge function of the abelian gauge principle. The *generator* is not central: $\omega$ anticommutes with two of the three vector units. That anticommutation, and not a central multiplication, is the algebra's reason that the two values rotate oppositely; and the commutation of left and right multiplications, not any property of a frame object, is the algebra's reason that the constant rotation commutes with the gradient.

**The frame position of the insertion.** The pseudoscalar is a single right factor, so the insertion carries a direction of the frame and no left action; the product $\vec e_\mu\vec e_\nu$ of two distinct units is what a magnetic or electric insertion uses, and the companion article on the electric dipole moment develops that case. The anomaly insertion is the pseudoscalar itself rather than its product with such a pair. The two insertions are different objects, and the article states the anomaly's and does not conflate it with the dipole's.

**The operator whose determinant is taken.** The pair is the corpus's chiral pair with its derivative made covariant, written as the two-by-two array of its two lines, and each line composed with its partner is the d'Alembertian. Its determinant is the object the measure produces, and its zero modes carry the index; the four-index symbol that its trace cannot supply is the one object of the standard computation that the algebra does not carry. What the framework does not supply is the measure itself — the space of fields, the Grassmann integration, and the determinant's definition. Those are the functional-integral apparatus, constructed in the companion articles on the fermionic path integral, and imported here.

## What the Framework Supplies, Transcribes, and Does Not Supply

| Item | Status |
|+-|+-|
| The massless equation $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=0$, one field, first order | **Supplied** by the gradient |
| The chiral pair, and $\Box\tilde{Ξ}_{\mathrm{sp}}=k_m^{2}\tilde{Ξ}_{\mathrm{sp}}$ as its consequence | **Supplied**; the mass needs two values because $\tilde\nabla^2$ is not scalar |
| $\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\Box$ | **Supplied**; recomputed with residual $3\times10^{-6}$ |
| The pseudoscalar $\omega=-\vec e_z$, with $\omega^2=-e_t$ | **Supplied** by the algebra |
| The two values as the two eigenspaces of right multiplication by $\vec e_z$, of dimensions $2$ and $2$ | **Supplied**; recomputed |
| The symbol $-i\tilde K_{\Phi}=k_{t}^{\prime}-i\vec k_\Phi$, with $(-i\tilde K_{\Phi})^{\natural}(-i\tilde K_{\Phi})=k_{t}^{\prime\,2}-\lvert\vec k_\Phi\rvert^2$ and $\det \ell_{-i\tilde K_{\Phi}}=(k_{t}^{\prime\,2}-\lvert\vec k_\Phi\rvert^2)^2$ | **Supplied**; recomputed |
| Rank four and kernel two on the six bivectors, with $f^2=0$ on the kernel, for null $k$ | **Supplied**, recomputed over five null wave vectors |
| The anomaly density, proportional to the framework's invariant $I_2$ | **Supplied** through the contraction $\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=+8\vec E\cdot\vec B$; the coefficient is standard |
| The four-index symbol as a trace of the algebra | **Not supplied, and proved absent**: the chirality-weighted trace vanishes for every element |
| The functional measure $\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}\,\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$ and the determinant | **Not supplied**; the fermionic path-integral apparatus, cited |
| The Fujikawa coefficient, the Seeley–DeWitt expansion, and the index relation | **Transcribed**; standard |
| The index theorem and the zero-mode count | **Outside**; the general gauge apparatus |
| The $\theta_{\mathrm{vac}}$ parameter and the vacuum angle | **Outside**; the general gauge apparatus |
| The rotation as the axial symmetry of the linear chiral pair | **Supplied**; the anomaly is the failure of that rotation to preserve the measure |

## Open Questions

1. **Can the measure be an algebra object?** The framework supplies the operator whose determinant the measure produces, but not the measure itself. Whether the fermionic functional measure can be characterised by the algebra — as a trace on a completion of $\mathbb{B}$ — or whether it is irreducibly a functional-analytic object, is not settled. The present article takes the measure from the fermionic path-integral apparatus and uses only its transformation law.

2. **Is a four-index trace available on any module the algebra carries?** The vanishing theorem is a statement about the four coefficients of one field. Whether a module built from the algebra itself — the pair $\mathbb{B}\oplus\mathbb{B}$, a tensor square, or a module of operators written as elements rather than as frame objects — can carry a non-vanishing chirality-weighted four-index trace is the open question the migration leaves. Any answer has to keep every glyph an element, since the frame objects are retired.

3. **Does non-commutativity alter the regulator?** The heat-kernel computation above is commutative in the field-strength background: for the abelian factor $F_{\mu\nu}$ is a commuting function of $x$, and a non-abelian factor only attaches its own algebra to the entries. The framework's algebra is non-commutative, and whether a genuinely biquaternion-valued background, one in which $F$ does not commute with itself at different points, produces a modification of the Seeley–DeWitt coefficient is not examined here.

4. **The algebraic index.** The integrated anomaly is the index of the operator, and the index theorem is a statement about elliptic operators on manifolds. Whether the biquaternion formulation admits an algebraic index statement — a pairing between a class of the algebra and a cyclic cocycle — is a question of the corpus's general gauge apparatus and is not attempted here.

5. **The $\theta_{\mathrm{vac}}$ dependence and the vacuum.** The anomaly makes the vacuum energy depend on a topological angle, and the resolution of the $\mathrm{U}(1)_A$ problem and the strong-CP problem involve that angle. Both belong to the general gauge apparatus; this article states the fermion-sector divergence and stops.

## Summary

The Fujikawa method derives the axial anomaly as the Jacobian of the fermion measure under a chiral rotation. In the biquaternion algebra the massless equation is one first-order equation in one field, $\tilde\nabla\tilde{Ξ}_{\mathrm{sp}}=0$, the massive equation is the chiral pair $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$ — because $\tilde\nabla^2$ is not scalar while $\tilde\nabla\tilde\nabla^{\natural}=\Box$ is — and the chiral rotation is the right multiplication $\tilde{Ξ}_{\mathrm{sp}}\mapsto\tilde{Ξ}_{\mathrm{sp}} e^{\alpha\omega}$ by the pseudoscalar $\omega=-\vec e_z$. The two values are the two eigenspaces of right multiplication by $\vec e_z$, of complex dimension two each, and the rotation multiplies them by $e^{+i\alpha}$ and $e^{-i\alpha}$. The local rotation adds the axial-current term; the measure does not add it, and the Jacobian is $(\det U)^{-2}=\exp(-2i\int\alpha a)$, with the regulated trace $a=\lim_{M\to\infty}\mathrm{tr}[\rho_\omega e^{-\mathcal{H}/M^2}]$ as the index density, the insertion taken on the right, and $A=2a$ as the anomaly density.

**The one thing the algebra does not give.** The regulated trace that produces the four-index symbol in the standard computation vanishes here identically: $\mathrm{tr}(\ell_h\rho_\omega)=0$ for every element, so all $24$ orders of four distinct units contribute exactly zero. The coefficient is therefore transcribed, $a=-(ϙ^2/32\pi^2)\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$, and the article states it as transcribed.

**What the algebra gives in its place.** The symbol $-i\tilde K_{\Phi}=k_{t}^{\prime}-i\vec k_\Phi$, whose biquaternion norm is $k_{t}^{\prime\,2}-\lvert\vec k_\Phi\rvert^2$ and whose left action on the six bivector components has rank four and a two-dimensional kernel on the null cone, with $f^2=0$ on the whole kernel — five null wave vectors, residual below $2\times10^{-14}$; and the contraction $\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}=+8\vec E\cdot\vec B$, so that
$$
\boxed{\;A(x)=-\frac{ϙ^2}{16\pi^2}\,\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
= -\frac{ϙ^2}{2\pi^2}\,\vec E\cdot\vec B=-\frac{ϙ^2}{2\pi^2}\,I_2\;},
$$
the framework's own second invariant. The axial divergence is the ABJ form, with the mass term the classical breaking and the Jacobian term the quantum one. The integrated anomaly is twice the index of the pair; that integer is what makes the coefficient exact, while the index theorem and the zero-mode count belong to the general gauge apparatus and were cited, not rebuilt. The functional measure itself is not supplied by the algebra: the framework carries the operator and the rotation, and the measure is imported from the path-integral apparatus of the companion articles.

## Summary of Notation

| Symbol | Meaning |
|+-|+-|
| $\mathbb{B}$ | The biquaternion algebra (*Algebra and Element Conventions*) |
| $\tilde{Ξ}_{\mathrm{sp}}$ | The biquaternion fermion field, one element of $\mathbb{B}$, with $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$ its Dirac-conjugate bilinear |
| $\mathbb{B}_{\Phi},\mathbb{B}_{\Psi}$ | Material and informational sectors (*Frame and Metric Conventions*) |
| $\tilde\nabla,\tilde\nabla^{\natural}$ | The biquaternionic gradient and its quaternion conjugate (*Operator and Calculus Conventions*, §*The Gradient*) |
| $\Box=\tilde\nabla\tilde\nabla^{\natural}$ | The d'Alembertian, $\partial^2/\partial R_t^2+\Delta_Q$; $\Delta-\partial^2/\partial {r'_{t}}^2$ on $\mathbb{B}_{\Phi}$ |
| $-i\tilde K_{\Phi}=k_{t}^{\prime}-i\vec k_\Phi$ | The symbol of the gradient on a plane wave |
| $\omega=-\vec e_z$ | The pseudoscalar, the volume element; $\omega^2=-e_t$, $\omega^{\natural}=-\omega$ |
| $\tilde{Ξ}_{\mathrm{sp},L},\tilde{Ξ}_{\mathrm{sp},R}$ | The two values: the eigenspaces of right multiplication by $\vec e_z$ with eigenvalues $-i$ and $+i$, each of complex dimension two |
| $\mathrm{tr}$ | The trace of a complex-linear operator on the four coefficients of the field |
| $\ell_h,\ \rho_\omega$ | Left multiplication by $h$, right multiplication by the pseudoscalar; $\rho_\omega$ is the measure's insertion, and $\ell_h\rho_\omega$ is the one two-sided shape the article uses |
| $\begin{pmatrix}-k_m&\tilde D\\ \tilde D^{\natural}&-k_m\end{pmatrix}$ | The two covariant lines of the pair in one block array; a matrix, not an element |
| $\mathcal{H}=-(\tilde D\tilde D^{\natural})_E$ | The continued regulator operator, whose scalar part is $-\Box_E$ |
| $a(x)=-\dfrac{ϙ^2}{32\pi^2}\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ | Regulated trace density, the index density |
| $A(x)=2a(x)=-\dfrac{ϙ^2}{16\pi^2}\epsilon_{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ | Anomaly density (Fujikawa and Adler–Bell–Jackiw) |
| $\mathrm{Tr}$ | The functional trace over modes |
| $\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}\,\mathcal{D}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$ | Fermion measure of the functional integral |
| $U=e^{\alpha\omega}=\cos\alpha\,\mathbb 1+\sin\alpha\,\omega$ | Chiral rotation; $\alpha$ a central scalar function |
| $J=(\det U)^{-2}=\exp(-2i\int d^4r\,\alpha a)$ | Jacobian of the measure under the rotation |
| $Z[A]=\det\begin{pmatrix}-k_m&\tilde D\\ \tilde D^{\natural}&-k_m\end{pmatrix}$ | Fermion determinant |
| $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\xi=\mathrm{Sc}(\tilde{Ξ}_{\mathrm{sp}}^*\xi\,i\vec e_x)$ | The Dirac bilinear, with its fixed right multiplier |
| $j_{\mu}=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\vec e_\mu\tilde{Ξ}_{\mathrm{sp}}$ | Vector current |
| $j_{5\mu}=\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\omega\vec e_\mu\tilde{Ξ}_{\mathrm{sp}}$ | Axial current |
| $\int d^4r\,\langle\tilde\nabla,\tilde J_{\Phi,5}\rangle_{\natural}=-2\,(n_L-n_R)$ | Integrated anomaly and index, in the all-low-index orientation |
| $I_1$, $I_2$ | Biquaternion field invariants, in the instanton article's normalization |
| $\tilde{F}=i\sqrt{\epsilon}\vec E-\sqrt{\mu}\vec H$ | Biquaternion field strength |
| $2m\,\tilde{Ξ}_{\mathrm{sp}}^{\dagger}\omega\tilde{Ξ}_{\mathrm{sp}}$ | Mass contribution to the axial divergence |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- K. Fujikawa, "Path-integral measure for gauge-invariant fermion theories," *Physical Review Letters* **42** (1979) 1195–1198, for the derivation of the anomaly from the measure.
- K. Fujikawa, "Comment on chiral and gauge anomalies," *Physical Review D* **21** (1980) 2848–2852, and **22** (1980) 1499 (Erratum), for the non-abelian extension and the heat-kernel evaluation.
- K. Fujikawa and H. Suzuki, *Path Integrals and Quantum Anomalies* (Oxford, 2004), for the systematic treatment of the measure, the Jacobian, and the index.
- B. S. DeWitt, *Dynamical Theory of Groups and Fields* (Gordon and Breach, 1965), for the Seeley–DeWitt heat-kernel expansion.
- R. T. Seeley, "Complex powers of an elliptic operator," *Proceedings of Symposia in Pure Mathematics* **10** (1967) 288–307, for the heat-kernel coefficients used in the regulator.
- M. F. Atiyah and I. M. Singer, "The index of elliptic operators: III," *Annals of Mathematics* **87** (1968) 546–604, for the index theorem behind the integrated anomaly.
- S. L. Adler, "Axial-vector vertex in spinor electrodynamics," *Physical Review* **177** (1969) 2426–2438, and J. S. Bell and R. Jackiw, "A PCAC puzzle: $\pi^0\to$ two photons in the $\sigma$-model," *Nuovo Cimento A* **60** (1969) 47–61, for the diagrammatic result with which the Jacobian agrees.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the functional measure, the fermion determinant, and the chiral rotation.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 2 (Cambridge, 1996), for the anomaly in the path-integral language and the role of the measure.
- L. Alvarez-Gaumé and P. Ginsparg, "The structure of gauge and gravitational anomalies," *Annals of Physics* **161** (1985) 423–490, for the heat-kernel and index-theoretic treatment of anomalies.
