# __The Fujikawa Method and the Path-Integral Anomaly in Biquaternionic Form__

## Introduction

The **Fujikawa method** derives the axial anomaly from the path integral rather than from a diagram. The observation is that the fermion measure is not invariant under a chiral rotation of the integration variables: the rotation is a linear change of variables whose Jacobian is a formal determinant, the determinant is infinite, and when it is regulated and evaluated it is not one. The anomaly is that Jacobian. The method makes the anomaly look like what it is — a property of the measure, not of the equations of motion — and it exhibits the coefficient as the trace of $\gamma_5$ against the heat kernel of the Dirac operator.

The derivation is two facts and one regularisation.

- **A symmetry of the action.** A chiral rotation $\psi\mapsto e^{i\alpha(x)\gamma_5}\psi$, $\bar{\psi}\mapsto\bar{\psi}e^{i\alpha(x)\gamma_5}$ leaves the massless Dirac action invariant, because $\gamma_5$ anticommutes with $\gamma^\mu$. Classically it is a symmetry.
- **A transformation of the measure.** The same rotation is a change of the integration variables $\psi,\bar{\psi}$, and the fermion measure $\mathcal{D}\psi\,\mathcal{D}\bar{\psi}$ picks up the inverse determinant of the rotation. That determinant is the whole story.
- **A regularisation.** The determinant is the product of the rotation's eigenvalues, one per mode, and it is divergent; it is regulated by a heat-kernel factor $e^{-(\text{operator})/M^2}$, evaluated as $M\to\infty$, and the finite remnant is the anomaly.

This article asks what the biquaternion framework supplies for this derivation. The answer is stated at the outset.

- **Established, and recomputed below.** The regulator trace is evaluated with the Clifford structure the framework already carries: the anomaly density is $\mathrm{tr}\,\gamma_5\,\mathcal{O}$, and the only nonvanishing trace with four gamma matrices is
$$
\mathrm{tr}\big(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\big) = -4i\,\epsilon^{\mu\nu\rho\sigma},
$$
recomputed here for all permutations. Because $\gamma_5=i\omega$ with $\omega$ the volume element, the trace is the framework's own chirality structure; because the field strength enters through the commutator $[D_\mu,D_\nu]$, the density is the framework's invariant $I_2=\mathbf{E}\cdot\mathbf{B}$. The method does not introduce an object the algebra lacks.
- **Standard, transcribed.** The measure, the Jacobian, the heat-kernel expansion (Seeley–DeWitt), the Fujikawa coefficient, and the index form of the integrated anomaly are standard. The measure is a functional-integral object and belongs to the corpus's general path-integral apparatus, which is cited and not rebuilt here.
- **Gap, left visible.** The framework does not supply the functional measure: the algebra gives the operator whose determinant is taken, not the space of fields over which the integral runs. The chiral rotation itself is the axial symmetry of the linear chiral pair; the *anomaly* is the statement that this rotation is not a symmetry of the measure. The framework carries the rotation and the operator; the measure is imported.

The article is organised as follows. A section sets up the measure and the chiral rotation. A section computes the Jacobian with the heat-kernel regulator. A section extracts the coefficient and identifies the density. A section gives the integrated form and the index. A section states the biquaternion reading of the rotation and the sector placement of $\alpha$. A closing section separates what is supplied, transcribed, and missing.

**Conventions.** We use those of the companion articles throughout. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and central scalar imaginary $i$, $i^2=-1$. The sectors are $\mathbb{M}_-$ (anti-Hermitian, material) and $\mathbb{M}_+$ (Hermitian, informational); the center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_0,ie_0\}$. The gradient is $\tilde{\nabla}=e_0\partial_{ict}+e_k\partial_k$ and $\Box=\partial_{ict}^2+\Delta$. The Dirac module is $\Delta=S\oplus\bar{S}$ with $S=\mathbb{C}^2$, $\gamma_5=\mathrm{diag}(-I_2,I_2)$, projectors $P_L=\tfrac12(I_4-\gamma_5)$, $P_R=\tfrac12(I_4+\gamma_5)$, and block representation

$$
\gamma^0=\begin{pmatrix}0&I_2\\ I_2&0\end{pmatrix},\qquad
\gamma^k=\begin{pmatrix}0&\sigma^k\\ -\sigma^k&0\end{pmatrix},\qquad
\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4,\qquad g=\mathrm{diag}(+1,-1,-1,-1),
$$

with $\gamma_5=i\omega$ and $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$ the volume element. The gauge covariant derivative is $D_\mu=\partial_\mu+\tfrac{iq}{\hbar}A_\mu$ with $[D_\mu,D_\nu]=\tfrac{iq}{\hbar}F_{\mu\nu}$ for the abelian factor, and $\mathcal{D}\psi\,\mathcal{D}\bar{\psi}$ denotes the fermion measure of the functional integral. The totally antisymmetric symbol has $\epsilon^{0123}=+1$, and $F_{0i}=E_i$, $F_{ij}=-\epsilon_{ijk}B_k$. The biquaternion field invariants are $I_1=\mathbf{E}^2-c^2\mathbf{B}^2$ and $I_2=\mathbf{E}\cdot\mathbf{B}$, with $\mathbf{B}=\mu\mathbf{H}$, in the instanton article's normalization. The trace formula $\mathrm{Tr}(\tilde{P}\tilde{H})=2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ is inherited unchanged. Throughout, $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ the vacuum value; natural units $\hbar=c=1$ are used in the heat-kernel section.

The framework results used here are those of the companion articles:

- Companion article *The Path Integral in Biquaternionic Form*, for the functional integral and the fermion measure whose Jacobian is computed here.
- Companion article *Instantons and Solitons in Biquaternionic Form*, for the topological density and the winding of the gauge field.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the field strength and the invariants $I_1$ and $I_2$.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the Dirac operator and the chirality operator $\gamma_5=i\omega$.

## The Measure and the Chiral Rotation

**The generating functional.** For a Dirac fermion coupled to an abelian gauge field in the functional-integral formulation, the generating functional is

$$
Z[A] = \int \mathcal{D}\psi\,\mathcal{D}\bar{\psi}\;\exp\!\left(i\int d^4x\;\bar{\psi}\big(i\gamma^\mu D_\mu-m\big)\psi\right),
$$

and the fermion integral is Gaussian: it evaluates to the determinant of the Dirac operator,

$$
Z[A] = \det\big(i\gamma^\mu D_\mu-m\big) .
$$

The bosonic and fermionic measures, the Gaussian integration, and the determinant are the subject of the corpus's general path-integral apparatus; the companion articles construct them, and this article takes them as given. What the algebra supplies here is the operator whose determinant is taken: $i\gamma^\mu D_\mu-m$ is the module representative of the framework's linear chiral pair of the massive section, with $m$ the same coefficient that the condensate of the companion article fixes.

**The chiral rotation.** Rotate the integration variables by an axial phase that is local,

$$
\psi(x)\ \longmapsto\ \psi'(x)=e^{i\alpha(x)\gamma_5}\psi(x),\qquad
\bar{\psi}(x)\ \longmapsto\ \bar{\psi}'(x)=\bar{\psi}(x)\,e^{i\alpha(x)\gamma_5},
$$

where the phase is a real scalar function. The massless kinetic term is invariant,

$$
\bar{\psi}'\,i\gamma^\mu\partial_\mu\psi'
=\bar{\psi}\,e^{i\alpha\gamma_5}\,i\gamma^\mu\partial_\mu\,e^{i\alpha\gamma_5}\psi
=\bar{\psi}\,i\gamma^\mu\partial_\mu\psi + \text{(a derivative of }\alpha\text{)},
$$

because $\{\gamma_5,\gamma^\mu\}=0$ twice cancels the two phase factors in the bilinear. Under the *local* rotation the derivative term produces a term proportional to $\partial_\mu\alpha$, which is the current; under the *global* rotation it produces nothing. A mass term is not invariant, $\bar{\psi}'m\psi'=\bar{\psi}m e^{2i\alpha\gamma_5}\psi$, which is the classical explicit breaking of the axial symmetry. In the framework's language the rotation is exactly the axial symmetry of the linear chiral pair: the vector central phase passes through the mass, and this one does not.

**The classical Ward identity, and the question.** Classically, the invariance of the massless action under the local rotation gives the conservation of the axial current, $\partial_\mu j_5^\mu=0$. The quantum question is whether the *measure* is invariant under the same change of variables. It is not, and the failure is the anomaly.

**Why the measure can fail.** A change of integration variables in a finite-dimensional integral multiplies the measure by the Jacobian determinant, regardless of whether the integrand is invariant. A symmetry of the action is therefore not automatically a symmetry of the integral; it is a symmetry only if the Jacobian is one. The chiral rotation of a Dirac field is a change of variables whose Jacobian is not one, and no local counterterm can restore it. This is why the anomaly is a property of the measure and why the diagrammatic and path-integral derivations must agree.

## The Jacobian and the Heat-Kernel Regulator

**The Jacobian.** Write the rotation as a linear map on the space of fields, $\psi'=U\psi$ with $U=e^{i\alpha\gamma_5}$, and the conjugate rotation on $\bar{\psi}$. The measure transforms by the inverse determinants,

$$
\mathcal{D}\psi'\,\mathcal{D}\bar{\psi}' = \big(\det U\big)^{-2}\,\mathcal{D}\psi\,\mathcal{D}\bar{\psi}
= \exp\!\left(-i\int d^4x\,\alpha(x)\,A(x)\right)\mathcal{D}\psi\,\mathcal{D}\bar{\psi},
$$

where the second equality *defines* the anomaly density $A(x)$ through the logarithm of the determinant; the two factors of $\det U$ (one from $\psi$ and one from $\bar{\psi}$) are absorbed into the normalisation of $A$, which is the standard convention. The determinant is formal and divergent: it is the product of the eigenvalues of $U$ over a complete set of modes, one per spacetime point per spinor component, and the product is infinite.

**The heat-kernel regulator.** To make the determinant finite and preserve gauge invariance, one regulates it with the squared Dirac operator. Choosing a complete set of modes $\{\varphi_n\}$ of the Hermitian operator $\mathcal{H}=(\gamma^\mu D_\mu)^2$ of Euclidean signature, with $\mathcal{H}\varphi_n=\lambda_n\varphi_n$, the regulated logarithm of the determinant is

$$
\ln\det U = \sum_n \langle\varphi_n|\,\ln e^{i\alpha\gamma_5}\,|\varphi_n\rangle
= i\sum_n \alpha_n\,\langle\varphi_n|\gamma_5|\varphi_n\rangle ,
$$

and the divergence is controlled by inserting the heat-kernel factor and taking the trace over the mode density:

$$
A(x) = \lim_{M\to\infty}\;\mathrm{tr}\Big[\gamma_5\,e^{-\mathcal{H}/M^2}\Big]_x ,
$$

with the normalisation fixed once and for all by requiring $A$ to be the ABJ density of the companion article. The subscript $x$ denotes the diagonal of the operator's kernel, the trace is over the spinor indices, and the $M\to\infty$ limit extracts the finite, regulator-independent remnant. This construction is Fujikawa's, and it is standard; what the framework contributes is the trace inside it.

**The heat-kernel expansion.** The operator $\mathcal{H}$ and the identity

$$
(\gamma^\mu D_\mu)^2 = D^2 + \tfrac12\gamma^\mu\gamma^\nu[D_\mu,D_\nu]
$$

(with the symmetrised form used below) fix the expansion. Using $\gamma^\mu\gamma^\nu=g^{\mu\nu}-i\sigma^{\mu\nu}$ with $\sigma^{\mu\nu}=\tfrac{i}{2}[\gamma^\mu,\gamma^\nu]$, and $[D_\mu,D_\nu]=iqF_{\mu\nu}$,

$$
(\gamma^\mu D_\mu)^2 = D^2 + \tfrac12\big(g^{\mu\nu}-i\sigma^{\mu\nu}\big)(iqF_{\mu\nu})
= D^2 + \tfrac{q}{2}\,\sigma^{\mu\nu}F_{\mu\nu},
$$

the term in the field strength surviving because $F_{\mu\nu}$ is antisymmetric. The heat kernel of $D^2$ in four dimensions has the standard Seeley–DeWitt expansion; the diagonal trace of $e^{-\mathcal{H}/M^2}$ produces, order by order, the coefficients of that expansion. The term that survives the trace with $\gamma_5$ is the one carrying four gamma matrices, and it is evaluated by the identity of the next paragraph. The overall normalisation $1/16\pi^2$ comes from the four-dimensional Gaussian and the two powers of the field strength, and its value is Fujikawa's; the article quotes it from the standard references rather than re-deriving it, since the derivation is the standard heat-kernel computation and is not special to the biquaternion algebra. What the framework fixes is the trace, and the trace is what makes the density a pseudoscalar built from the field strength.

**The one identity that matters.** For all $4!=24$ permutations,

$$
\mathrm{tr}\big(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma\big) = -4i\,\epsilon^{\mu\nu\rho\sigma},
\qquad
\mathrm{tr}\big(\gamma_5\gamma^0\gamma^1\gamma^2\gamma^3\big)=-4i ,
$$

and the trace vanishes for any repeated index; the identity was recomputed in the block basis, with residual exactly zero. Because the density must carry four distinct Dirac indices, only the quadratic part of the heat kernel contributes, and the result is proportional to $\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$.

**The result.** Putting the pieces together, the anomaly density is

$$
A(x) = \frac{q^2}{16\pi^2}\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma},
\qquad
\mathcal{D}\psi\,\mathcal{D}\bar{\psi}\ \longmapsto\ \exp\!\left(-i\int d^4x\,\alpha(x)\,A(x)\right)\mathcal{D}\psi\,\mathcal{D}\bar{\psi},
$$

and the measure is not invariant. The coefficient is Fujikawa's, and it agrees with the Adler–Bell–Jackiw value computed from the triangle in the companion article on anomalies; the agreement is not an accident but the statement that the two derivations compute the same trace. Reinstating the mass term, the axial divergence is

$$
\partial_\mu j_5^\mu = 2im\,\bar{\psi}\gamma_5\psi + A(x)
= 2im\,\bar{\psi}\gamma_5\psi + \frac{q^2}{16\pi^2}\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma},
$$

which is exactly the ABJ form of the companion article. The mass term is the classical breaking and the Jacobian term is the quantum one; the two are additive and independent.
<!-- CONVENTION — anomaly normalization: the density A(x) is written with eps^{munurhosigma}F_{munu}F_{rhosigma} and coefficient q^2/16pi^2, gamma5 = i omega, eps^{0123}=+1. Conventions that use (1/2)epsFF or the opposite gamma5 sign carry the complementary factor of 2 or a minus; do not "reconcile" the coefficients across conventions without checking the definitions of gamma5 and eps. -->

## The Regulator and the Symmetry It Preserves

**Why the regulator is part of the argument.** The Jacobian is a product of infinitely many eigenvalues, and any statement about it requires a prescription that makes the product finite. The prescription is not innocent. A naive momentum cutoff, for instance, breaks the gauge invariance of the fermion determinant, and the gauge non-invariance it introduces is indistinguishable, at the level of the regulated determinant, from a genuine anomaly. The Fujikawa regulator is chosen to preserve gauge invariance: the heat-kernel factor $e^{-\mathcal{H}/M^2}$ is built from the gauge-covariant operator $\mathcal{H}=(\gamma^\mu D_\mu)^2$, so it commutes with the gauge transformations, and every breaking it produces is attributable to the inserted $\gamma_5$ and not to the cutoff. The anomaly is then the *entire* failure of the chiral symmetry of the measure, with no spurious part. The heat kernel is defined in Euclidean signature, where the squared Dirac operator is positive definite and $e^{-\mathcal{H}/M^2}$ is convergent; the Euclidean continuation is the standard setting for the Seeley–DeWitt expansion, and it does not alter the anomaly coefficient.

**Regulator independence.** Different gauge-invariant regulators give the same anomaly. The reason is that the difference between two such regulators is a local counterterm, and the anomaly — being a total derivative with an integer integral — cannot be removed by a local counterterm that respects the symmetry. This is the path-integral form of the Adler–Bardeen non-renormalisation theorem, and it is the reason the coefficient is a number rather than a function of the cutoff. The regulator's job is only to expose the finite remnant; it does not choose it.

**The heat-kernel weight and the $\gamma_5$ insertion.** Two features of the construction are worth separating. The heat-kernel factor $e^{-\mathcal{H}/M^2}$ suppresses the high modes and produces the $1/M^2$ expansion whose coefficients are the Seeley–DeWitt terms; it is a *gauge-invariant* regulator. The insertion of $\gamma_5$ is what makes the trace chirality-weighted; it is not a regulator and is the origin of the anomaly. In the framework's terms the division of labour is the same: $\mathcal{H}$ is built from the covariant derivative of the linear chiral pair, and $\gamma_5=i\omega$ is the volume element whose trace is taken.

## Comparison with the Diagrammatic Derivation

**The two computations agree, and must.** The companion article on anomalies computes the divergence of the axial current from the triangle diagram, with one axial and two vector insertions, and obtains the Adler–Bell–Jackiw coefficient. This article obtains the same coefficient as the Jacobian of the measure. The agreement is a consistency requirement, and the reason is visible in the two computations: both reduce to the same Clifford trace, $\mathrm{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)=-4i\epsilon^{\mu\nu\rho\sigma}$. The triangle computes it against three current insertions; the heat kernel computes it against the squared Dirac operator's field-strength term. The trace is the same, so the coefficient is the same.

**What each derivation explains.** The diagrammatic derivation explains *what* the anomaly is as a physical process: a triangle of fermions with an axial current and two gauge currents, finite and unrenormalised. The path-integral derivation explains *why* it is unavoidable: the measure is not invariant under the symmetry, and no choice of regulator removes a symmetry the measure does not have. The second explanation is the deeper one, and it is why the anomaly survives any dynamics that leaves the measure intact: confinement, a condensate, or a change of degrees of freedom cannot remove it, which is the content of anomaly matching in the companion article.

**One-loop exactness from the measure.** The Adler–Bardeen theorem is transparent in the path-integral language: the Jacobian is a one-loop determinant, because the measure's transformation is computed at the Gaussian level, and there is no higher loop in which to correct it. The regulator independence then promotes the one-loop value to an exact statement. The triangle derivation gives the same protection only after the theorem is proved diagram by diagram; the measure gives it as a structural fact. Neither route is special to the biquaternion algebra, and both are transcribed.

## The Coefficient, the Density, and the Framework

**The coefficient is a Clifford trace times a field contraction.** The Fujikawa coefficient factorises exactly as the triangle coefficient did: a spinor trace, which produced $-4i\epsilon^{\mu\nu\rho\sigma}$, and a field-strength contraction, which produced $F_{\mu\nu}F_{\rho\sigma}$. The four-dimensional heat-kernel coefficient supplies the $1/16\pi^2$. Nothing in the factorisation uses a property of the specific gauge group; the abelian computation above generalises to the non-abelian case by replacing $q^2F_{\mu\nu}F_{\rho\sigma}$ with $\mathrm{tr}[F_{\mu\nu}F_{\rho\sigma}]$ and the coefficient by the appropriate Casimir, which is the standard non-abelian Fujikawa result.

**The density is the framework's invariant.** The contraction is

$$
\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma} = -8\,\mathbf{E}\cdot\mathbf{B},
$$

evaluated directly with $F_{0i}=E_i$, $F_{ij}=-\epsilon_{ijk}B_k$ for sample fields; hence

$$
A(x) = -\frac{q^2}{2\pi^2}\,\mathbf{E}\cdot\mathbf{B}
= -\frac{q^2}{2\pi^2}\,I_2 ,
$$

which is the framework's second invariant $I_2$ of the biquaternion field $\tilde{F}=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$, in the normalization of the instanton article. The anomalous divergence is therefore the divergence of the axial current into the framework's own pseudoscalar invariant; the parity-odd density is parity-odd because $I_2$ is a pseudoscalar, and the topological character noted in the companion article is the total-derivative form of the same contraction.

**Why $\gamma_5$ is the volume element.** The identity $\gamma_5=i\omega$ is what makes the whole computation a statement about the algebra rather than about a chosen basis. The chirality operator is the volume element of the Clifford algebra up to the central $i$; the anomaly trace is the trace of the volume element against the heat kernel; and the $\epsilon$ symbol is the coordinate form of the volume element. In the biquaternion language $\omega=\Phi(i)$ is the image of the central scalar imaginary, so the insertion of $\gamma_5$ is an insertion of the algebra's central element — the same element whose phase is the vector symmetry that the mass conserves. The axial and vector currents differ by which element of the center is inserted, and the anomaly is the statement that the volume-element insertion is not a symmetry of the measure.

**Where the $1/16\pi^2$ comes from.** The coefficient is a four-dimensional Gaussian, and it can be read off before any gamma matrix is touched. In the coincidence limit the free heat kernel is

$$
\big\langle x\big|e^{-\partial^2/M^2}\big|x\big\rangle
= \int\frac{d^4p}{(2\pi)^4}\,e^{-\mathbf{p}^2/M^2}
= \frac{M^4}{16\pi^2},
$$

using $\int d^4p\,e^{-p^2/M^2}=(\pi M^2)^2=\pi^2M^4$ and dividing by $(2\pi)^4=16\pi^4$. The Gaussian supplies $1/16\pi^2$ and two inverse powers of $M^2$, which are exactly what the two field-strength factors in the $(\sigma^{\mu\nu}F_{\mu\nu})^2$ term need to leave a finite result. The same Gaussian appears in the Seeley–DeWitt expansion of the curved and gauge-covariant Laplacian, where the coefficient is the $a_2$ Seeley–DeWitt term; the anomaly uses only the field-strength part of that term, since the curvature part carries no $\gamma_5$ trace.

## The Integrated Form and the Index

**The integral of the density.** The integrated anomaly is a topological invariant. Using the total-derivative form and the index of the Dirac operator,

$$
\int d^4x\,\partial_\mu j_5^\mu
= \int d^4x\,A(x)
= \frac{q^2}{16\pi^2}\int d^4x\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
= 2\,\mathrm{ind}(D\!\!\!/ ),
$$

so the axial charge transported in a background is twice the index. The index is the difference between the numbers of right- and left-handed zero modes of the massless Dirac operator, and the general theorem identifying the two sides is Atiyah–Singer. The zero-mode count and the index theorem belong to the corpus's general gauge apparatus and are not developed here; the fermion-sector facts are that the integral is an integer, that the coefficient is therefore protected against renormalisation, and that a background of unit topological charge produces a net axial-charge violation.

**The zero modes and the measure.** The index reading makes the Fujikawa computation transparent. The chiral rotation acts on each mode by a phase; modes of definite chirality are rotated with opposite signs; the regulator counts them with the heat-kernel weight; and a mismatch between the numbers of left- and right-handed zero modes is a nonzero difference that no regulator can cancel. The anomaly is the zero-mode mismatch seen through the measure. In the framework's terms, the mismatch is a property of the Dirac operator on the module $\Delta=S\oplus\bar{S}$ in a background with nonzero topological charge, and the topological charge is the winding of the material-sector connection.

**One instanton.** For a unit instanton the index is one per flavour and the axial charge changes accordingly; the explicit factor of two in front of the index is the statement that the axial current of a Dirac field counts the two chiralities against each other, while the topological charge counts the net mismatch once. The factor is the same $2-2=0$ trace identity as in the companion article: $\mathrm{tr}(\gamma_5)=0$ for a background with no net index, and the integral turns it on. Nothing here is particular to the biquaternion algebra except the identification of the winding with the material sector and of the density with $I_2$.

**The two rotations compared.** The framework's two continuous symmetries of the massless equation behave differently in the measure, and the difference is exact. The **vector** rotation $\psi\mapsto e^{i\alpha}\psi$ is multiplication by a central element; it rotates both chiralities in the same sense, and its would-be anomaly coefficient is the cubic charge sum that vanishes identically for a vector-like spectrum. It is a symmetry of the measure. The **axial** rotation $\psi\mapsto e^{i\alpha\gamma_5}\psi$ inserts the volume element; it rotates the two chiralities oppositely, and its Jacobian is not one. Only the second is anomalous. In the framework's terms the mass term and the measure agree on which symmetry is broken: the linear chiral pair breaks the axial phase and conserves the central one, and the measure does the same. A theory whose mass were vector-like would have neither breaking, and the framework's linear chiral pair is not that theory.

**The index density.** The relation above can be written locally. The four-dimensional index density is proportional to $\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$, the second Chern character of the gauge field, and its integral is the topological charge whose biquaternion form the companion article on instantons computes from $I_2$. The chain is therefore: $\gamma_5=i\omega$ inserts the volume element; the heat-kernel trace converts the volume element into the $\epsilon$ symbol; the $\epsilon$ symbol contracts the field strength into the second invariant; and the integral of the invariant is the winding of the material-sector connection. Every link is a framework object except the measure, and the last link is the general index theorem.

## The Chiral Rotation in the Biquaternion Language

**The rotation is the axial symmetry of the linear chiral pair.** The rotation $\psi\mapsto e^{i\alpha\gamma_5}\psi$ rotates the left-handed module $S$ and its conjugate $\bar{S}$ in opposite directions. It is the axial phase whose breaking was treated in the companion article on the condensate; there the breaking was spontaneous and classical-in-the-vacuum, here it is explicit and quantum-mechanical. The two are different phenomena acting on the same symmetry, and the framework keeps them distinct: the condensate supplies a coefficient to the linear chiral pair, and the anomaly violates the axial current even when the coefficient is zero.

**The phase $\alpha(x)$ is a central scalar.** The rotation parameter is a real scalar function of position, hence a central element of the algebra times a function; it is the same kind of object as the gauge function $\Gamma$ of the abelian gauge principle. The rotation therefore acts by left multiplication by a central element, which is the algebra's reason that it commutes with the covariant derivative up to the derivative term. The current $j_5^\mu$ that the variation produces is the axial bilinear, and the anomaly is the failure of the centrally-generated *axial* rotation to preserve the measure — in sharp contrast with the centrally-generated *vector* rotation, which *is* a symmetry of the measure because it is vector-like.

**The sector placement of the operator.** In the algebro-Clifford dictionary the volume element $\omega$ is the image of the central imaginary, and the EDM-type insertion $\sigma^{\mu\nu}\gamma_5$ is anti-Hermitian and sits in the material sector $\mathbb{M}_-$ (the companion article on the electric dipole moment develops this). The anomaly insertion is $\gamma_5$ itself rather than $\sigma^{\mu\nu}\gamma_5$; it is Hermitian, and its trace against the heat kernel is what the regulator computes. The two insertions are different objects and their sector placements differ; the article states the anomaly's and does not conflate it with the EDM's.

**The operator whose determinant is taken.** The Dirac operator $i\gamma^\mu D_\mu$ is the module representative of the framework's covariant biquaternion derivative on the massive sector. Its determinant is the object the measure produces, and its zero modes carry the index. What the framework does not supply is the measure itself — the space of fields, the Grassmann integration, and the determinant's definition. Those are the functional-integral apparatus, constructed in the companion articles on the path integral and on the functional integral, and imported here.

## What the Framework Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| The chirality insertion $\gamma_5=i\omega$ as the volume element | **Supplied** by the Clifford isomorphism |
| The trace identity $\mathrm{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)=-4i\epsilon^{\mu\nu\rho\sigma}$ | **Supplied**, recomputed for all permutations |
| The heat-kernel splitting $(\gamma^\mu D_\mu)^2=D^2+\tfrac{q}{2}\sigma^{\mu\nu}F_{\mu\nu}$ | **Supplied** from the Clifford relations |
| The anomaly density as the framework's invariant $I_2=\mathbf{E}\cdot\mathbf{B}$ | **Supplied**; the coefficient is standard |
| The Dirac operator whose determinant is the measure's Jacobian | **Supplied**: the module representative of the linear chiral pair |
| The functional measure $\mathcal{D}\psi\,\mathcal{D}\bar{\psi}$ and the determinant | **Not supplied**; the general path-integral and functional-integral apparatus, cited |
| The Fujikawa coefficient, the Seeley–DeWitt expansion, and the index relation | **Transcribed**; standard |
| The index theorem and the zero-mode count | **Outside**; the general gauge apparatus |
| The $\theta$ parameter and the vacuum angle | **Outside**; the general gauge apparatus |
| The rotation as the axial symmetry of the linear chiral pair | **Supplied**; the anomaly is the failure of that rotation to preserve the measure |

## Open Questions

1. **Can the measure be an algebra object?** The framework supplies the Dirac operator whose determinant the measure produces, but not the measure itself. Whether the fermionic functional measure can be characterised by the algebra — as a trace on a completion of $\mathbb{B}$ or of its module — or whether it is irreducibly a functional-analytic object, is not settled. The present article takes the measure from the general path-integral apparatus and uses only its transformation law.

2. **Does non-commutativity alter the regulator?** The heat-kernel computation above is commutative in the field-strength background: $F_{\mu\nu}$ is a matrix in the gauge factor but a commuting function of $x$ in the abelian case. The framework's algebra is non-commutative, and whether a genuinely biquaternion-valued background (one in which $F$ does not commute with itself at different points) produces a modification of the Seeley–DeWitt coefficient is not examined here. For the Standard Model's gauge fields the algebra enters only through the Clifford trace, and the standard coefficient applies.

3. **The algebraic index.** The integrated anomaly is the index of the Dirac operator, and the index theorem is a statement about elliptic operators on manifolds. Whether the biquaternion formulation admits an algebraic index statement — a pairing between a $K$-theory class of the module and a cyclic cocycle of the algebra — is a question of the corpus's general gauge apparatus and is not attempted here.

4. **The $\theta$ dependence and the vacuum.** The anomaly makes the vacuum energy depend on a topological angle, and the resolution of the $U(1)_A$ problem and the strong-CP problem involve that angle. Both belong to the general gauge apparatus and to the spin-$0$ subcategory; this article states the fermion-sector divergence and stops.

## Summary

The Fujikawa method derives the axial anomaly as the Jacobian of the fermion measure under a chiral rotation. The massless Dirac action is invariant under $\psi\mapsto e^{i\alpha(x)\gamma_5}\psi$; the measure is not; the Jacobian is $\exp(-i\int\alpha A)$, and the regulated trace defines the anomaly density. Regulating with $\mathcal{H}=(\gamma^\mu D_\mu)^2$ and the heat-kernel factor $e^{-\mathcal{H}/M^2}$, the density is the trace of $\gamma_5$ against the heat kernel; the only surviving gamma-matrix trace is $\mathrm{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)=-4i\epsilon^{\mu\nu\rho\sigma}$, recomputed for all $4!$ permutations with residual exactly zero, and the result is

$$
A(x)=\frac{q^2}{16\pi^2}\,\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}
= -\frac{q^2}{2\pi^2}\,\mathbf{E}\cdot\mathbf{B},
$$

so the anomaly density is proportional to the framework's second field invariant $I_2=\mathbf{E}\cdot\mathbf{B}$. The axial divergence is the ABJ form, with the mass term the classical breaking and the Jacobian term the quantum one.

The biquaternion content is threefold: the chirality insertion is the volume element, $\gamma_5=i\omega$; the heat-kernel splitting follows from the Clifford relations; and the density is the framework's own pseudoscalar invariant. The rotation is the axial symmetry of the linear chiral pair, and the anomaly is the statement that this rotation does not preserve the measure — while the vector central rotation, being vector-like, does. The integrated anomaly is twice the index of the Dirac operator, which makes the coefficient an integer and therefore exact; the index theorem and the zero-mode count belong to the general gauge apparatus and were cited, not rebuilt. The functional measure itself is not supplied by the algebra: the framework carries the operator and the rotation, and the measure is imported from the path-integral apparatus of the companion articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $\mathbb{M}_-,\mathbb{M}_+,\mathbb{C}_{\mathbb{B}}$ | Material sector, informational sector, center |
| $\Delta=S\oplus\bar{S}$ | Dirac module; $S=\mathbb{C}^2=(\tfrac12,0)$ |
| $\gamma_5=\mathrm{diag}(-I_2,I_2)=i\omega$ | Chirality operator as volume element |
| $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$ | Clifford volume element |
| $\mathrm{tr}(\gamma_5\gamma^\mu\gamma^\nu\gamma^\rho\gamma^\sigma)=-4i\epsilon^{\mu\nu\rho\sigma}$ | The regulator trace |
| $\mathcal{H}=(\gamma^\mu D_\mu)^2=D^2+\tfrac{q}{2}\sigma^{\mu\nu}F_{\mu\nu}$ | Regulator operator (Euclidean) |
| $A(x)=\dfrac{q^2}{16\pi^2}\epsilon^{\mu\nu\rho\sigma}F_{\mu\nu}F_{\rho\sigma}$ | Anomaly density (Fujikawa) |
| $\mathcal{D}\psi\,\mathcal{D}\bar{\psi}$ | Fermion measure of the functional integral |
| $U=e^{i\alpha(x)\gamma_5}$ | Chiral rotation; $\alpha$ a central scalar function |
| $J=\exp(-i\int d^4x\,\alpha A)$ | Jacobian of the measure under the rotation, both determinant factors included |
| $Z[A]=\det(i\gamma^\mu D_\mu-m)$ | Fermion determinant |
| $\int d^4x\,\partial_\mu j_5^\mu=2\,\mathrm{ind}(D\!\!\!/)$ | Integrated anomaly and index |
| $I_1=\mathbf{E}^2-c^2\mathbf{B}^2$, $I_2=\mathbf{E}\cdot\mathbf{B}$ | Biquaternion field invariants |
| $\tilde{F}=i\sqrt{\epsilon}\mathbf{E}-\sqrt{\mu}\mathbf{H}$ | Biquaternion field strength |
| $2im\bar{\psi}\gamma_5\psi$ | Mass contribution to the axial divergence |
| $c=1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- K. Fujikawa, "Path-integral measure for gauge-invariant fermion theories," *Physical Review Letters* **42** (1979) 1195–1198, for the derivation of the anomaly from the measure.
- K. Fujikawa, "Comment on chiral and gauge anomalies," *Physical Review D* **21** (1980) 2848–2852, and **22** (1980) 1499 (Erratum), for the non-abelian extension and the heat-kernel evaluation.
- K. Fujikawa and H. Suzuki, *Path Integrals and Quantum Anomalies* (Oxford, 2004), for the systematic treatment of the measure, the Jacobian, and the index.
- B. S. DeWitt, *Dynamical Theory of Groups and Fields* (Gordon and Breach, 1965), for the Seeley–DeWitt heat-kernel expansion.
- R. T. Seeley, "Complex powers of an elliptic operator," *Proceedings of Symposia in Pure Mathematics* **10** (1967) 288–307, for the heat-kernel coefficients used in the regulator.
- M. F. Atiyah and I. M. Singer, "The index of elliptic operators: III," *Annals of Mathematics* **87** (1968) 546–604, for the index theorem behind the integrated anomaly.
- S. L. Adler, "Axial-vector vertex in spinor electrodynamics," *Physical Review* **177** (1969) 2426–2438, and J. S. Bell and R. Jackiw, "A PCAC puzzle: $\pi^0\to\gamma\gamma$ in the $\sigma$-model," *Nuovo Cimento A* **60** (1969) 47–61, for the diagrammatic result with which the Jacobian agrees.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), for the functional measure, the fermion determinant, and the chiral rotation.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 2 (Cambridge, 1996), for the anomaly in the path-integral language and the role of the measure.
- L. Alvarez-Gaumé and P. Ginsparg, "The structure of gauge and gravitational anomalies," *Annals of Physics* **161** (1985) 423–490, for the heat-kernel and index-theoretic treatment of anomalies.
