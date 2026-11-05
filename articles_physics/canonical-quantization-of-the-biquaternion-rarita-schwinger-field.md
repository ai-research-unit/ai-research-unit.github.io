# __Canonical Quantization of the Biquaternion Rarita–Schwinger Field__

## Introduction

The Rarita–Schwinger field is the field of spin $\tfrac32$: a vector-spinor $\psi_\mu$, carrying one Lorentz vector index and one Dirac spinor index, subject to the constraint that its trace vanish. As a classical field equation the Rarita–Schwinger equation is the subject of the companion article *The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form*; the present article takes that equation as given and develops the **canonical quantization** of the field in the biquaternion framework: the constraint structure, the mode expansion, the anticommutators, the count of physical polarizations, and the gauge and ghost structure of the massless case.

The biquaternion framework is well suited to this field, because the two indices of $\psi_\mu$ correspond to the two kinds of object the framework distinguishes. The vector index carries the **material** vector representation, which the article on integer-spin quantization identifies with the adjoint action on the vector part $V\subset\mathbb{M}_-$; the spinor index carries the representation that the Dirac article identifies as the spin-$\tfrac12$ carrier. The Rarita–Schwinger field is therefore the tensor product of the two, and its decomposition is the framework's own:

$$
\boxed{\;1\otimes\tfrac12=\tfrac32\oplus\tfrac12,
\qquad
3\cdot 2=4+2\;},
$$

so that the tensor product of the material vector with the spinor contains a spin-$\tfrac32$ piece and a spin-$\tfrac12$ piece, and the trace constraint removes the latter. The same pattern appears for the graviton, where the symmetric square of the material triplet decomposes as $0\oplus2$ with $6=1+5$, and the trace-free part is the spin-two carrier of dimension five. In both cases the antisymmetrized kinetic structure carries the top spin and a trace removes the lower component; for the half-integer field the trace is taken with the frame cells, and it is the constraint that makes the field irreducible.

The article is organized as follows. The field and its frame are fixed first, and every display is then written as an action on an element; three composites are then named once — the pair operator, its Fourier symbol, and the trace spinor — so that no display of the body repeats a sum. The gamma dictionary is collected once, in *The Legacy Pauli Gamma Formulation* at the end, so that no display of the body needs a gamma. The chiral pair, the constraint, and the consequence that transversality follows from the two are stated next, and the projector onto the traceless part is constructed and verified. The gauge structure of the massless case and the second-class structure of the massive case are contrasted. The canonical quantization is then carried out: momenta, Dirac brackets, anticommutators, the mode expansion, and the fermionic Fock space. The propagator and its gauge fixing are recorded, the biquaternion interpretation of the decomposition is developed, and the article closes with the accounting of what the algebra supplies and what is imported.

- Companion article *The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form*, for the classical equation, the chiral pair, and the rest-frame reduction.
- Companion article *The Dirac Equation in Biquaternionic Form*, for the spinor carrier and the frame cells.
- Companion article *Canonical Quantization of the Biquaternion Maxwell Field*, for the massless gauge field whose gauge structure the massless Rarita–Schwinger case generalizes.
- Companion article *The Spin–Statistics Theorem in Biquaternionic Form*, for the fermionic quantization of half-integer-spin fields.

## The Field, Its Constraint, and Transversality

### The Field and Its Cell

The field is a vector-spinor: four components $\psi_\mu$, each an element of $\mathbb{B}$. The vector index is carried by the **frame cells** of *Matrix Representations Conventions*: the cell of the coordinate $x_\mu$ is $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, with $\nu(t)=x$ and $\nu(k)=y$, and its action on an element is

$$
\psi\longmapsto i\,e_\mu\,\psi\,\vec e_{\nu(\mu)} .
$$

The cell of the time component is therefore the single right multiplier $\psi\mapsto i\psi\vec e_x$, and the cell of a spatial component is the two-sided action $\psi\mapsto i\vec e_k\psi\vec e_y$. The label of a cell is the coordinate index of its left multiplier, and it is written low. The four actions anticommute up to the sign vector: two of them composed in the two orders multiply the left factors and the right factors in opposite orders, so the two compositions add to $2\varepsilon_\mu\delta_{\mu\nu}$ times the identity action, with $\varepsilon=(1,-1,-1,-1)$ the plain weight of the product. The two imaginary units of a pair of cells are multiplied to $-1$ wherever a pair is composed, so the displays below carry the product of the units and never a double $i$. No index is raised, and every contraction of two low indices carries the sign vector.

Two composites recur often enough to name once. They are sums and contractions rather than single cells, so they carry letters where no frame cell does. The first is the **pair operator** of *Operator and Calculus Conventions* read on the module, written for the derivative and for the momentum,

$$
\mathbb{D}\psi:=-\sum_\mu\varepsilon_\mu\,e_\mu\frac{\partial\psi}{\partial x_\mu}\vec e_{\nu(\mu)},
\qquad
\mathbb{D}_p\psi:=\sum_\mu\varepsilon_\mu\,i\,e_\mu\,\psi\,\vec e_{\nu(\mu)}\,p_\mu ,
$$

with $\mathbb{D}^2=\Box$ and $\mathbb{D}_p^2=p^2$; the minus sign of $\mathbb{D}$ is the product of the imaginary unit of the frame cell and the one the Dirac operator carries, $i\cdot i=-1$, and $\mathbb{D}_p$ keeps the single one of the cell. The second is the **trace spinor** of a vector-spinor, the metric contraction of its vector index with the frame cells,

$$
\Sigma(\psi):=\sum_\mu\varepsilon_\mu\,i\,e_\mu\,\psi_\mu\,\vec e_{\nu(\mu)} .
$$

It is the spinor the companion article writes $S$; the letter $\Sigma$ is used here so as not to collide with the spinor carrier $S$ of the Dirac article.

### The Equations

The spinor index is the carrier of the Dirac article, and the field equation is the **chiral pair**: for each $\mu$,

$$
\boxed{\;
\tilde\nabla\tilde\Psi_{\mu,R}=m\tilde\Psi_{\mu,L},
\qquad
\tilde\nabla^{\natural}\tilde\Psi_{\mu,L}=m\tilde\Psi_{\mu,R}
\;}
$$

with $\tilde\Psi_\mu=\tilde\Psi_{\mu,L}+\tilde\Psi_{\mu,R}$. The two equations are the two values of the chirality subscript, not two independent dynamics: the first couples the gradient to the right-chiral value, the second the conjugate gradient to the left-chiral value, and the conjugation $\natural$ is what exchanges the two. This is the two-sided operator theorem of *Operator and Calculus Conventions*: a right action on $\psi$ is a left action on $\psi^{\natural}$, so the pair is complete as written and no second field is needed. The chirality cell acts by $\psi\mapsto-i\psi\vec e_z$, and it anticommutes with the four frame cells: each cell therefore carries one value into the other, which is what makes the pair a two-sided form of a single equation rather than two dynamics.

On the spinor module the pair is transcribed as the single **cell equation**

$$
\bigl(\mathbb{D}-m\bigr)\psi_\mu=0 ,
$$

with the operator of the preceding paragraph. The two imaginary units — the one of the frame cell and the one the operator carries — are already multiplied to $-1$ inside $\mathbb{D}$, so the display carries no $i$; the minus sign of $\mathbb{D}$ *is* that product. What remains is a plain two-sided contraction. The single equation is the transcription of the pair, not a second equation: the operator multiplies on both sides, and its action on the two chiral values is the pair above. The companion article states the same equivalence from the classical side, and *The Legacy Pauli Gamma Formulation* reads $\mathbb{D}$ in the gamma notation.

The field is irreducible only with the **trace constraint**

$$
\boxed{\;\Sigma(\psi)=\sum_\mu\varepsilon_\mu\,i\,e_\mu\,\psi_\mu\,\vec e_{\nu(\mu)}=0.\;}
$$

The constraint is not an equation of motion; it removes the spin-$\tfrac12$ components that a bare vector-spinor would contain. The fully antisymmetric form of the Rarita–Schwinger equation — the antisymmetrized triple contracted with the derivative and the antisymmetrized pair multiplying the mass — is the Lagrangian origin of the system. For $m\neq0$ it implies the component equation and the trace constraint, and the pair and the constraint displayed above are the reduced form; the companion article gives the reduction. For quantization the pair and the constraint are the starting point.

In the algebra the weighted trace is one element: multiplying it on the left by the invertible cell $\psi\mapsto i\psi\vec e_x$ gives $\tilde\Psi_0-\sum_k\vec e_k\tilde\Psi_k\vec e_z$, so the constraint is that single element, and the element needs no frame once the frame has been used to state it. The weight is not optional: the projector below annihilates the weighted contraction, and the same sum without the sign vector is not annihilated by it.

### Transversality from the Constraint

Apply the trace map to the momentum-space field equation. What does the work is one identity, and it follows from the anticommutation relation of the frame cells: for every vector-spinor,

$$
\Sigma\bigl(\mathbb{D}_p\psi\bigr)=2\,p\cdot\psi-\mathbb{D}_p\,\Sigma(\psi),
$$

the trace of the operator times the field being the divergence of the field minus the operator applied to the trace. The field equation is $(\mathbb{D}_p-m)\psi_\mu=0$, so its trace is

$$
m\,\Sigma(\psi)=\Sigma\bigl(\mathbb{D}_p\psi\bigr)=2\,p\cdot\psi-\mathbb{D}_p\,\Sigma(\psi) ,
\qquad\text{that is}\qquad
2\,p\cdot\psi=\bigl(\mathbb{D}_p+m\bigr)\Sigma(\psi) .
$$

The divergence of the field is therefore the trace spinor propagated by the field operator, and it vanishes when the trace does. Hence the constraint and the field equation together imply the **transversality** condition

$$
\boxed{\;p\cdot\psi:=\sum_\mu\varepsilon_\mu p_\mu\psi_\mu=0\;},
$$

which is not independent but follows from the two. The identity and the implication were verified with explicit $4\times4$ matrices of the frame cells, with $p$ on shell: the identity to machine precision, and $p\cdot\psi=0$ on every solution of the equation and the constraint.

### The Projector onto the Traceless Part

The constraint is imposed by the projector, defined by its action on a vector-spinor,

$$
(P\psi)_\mu:=\psi_\mu-\tfrac14\,i\,e_\mu\,\Sigma(\psi)\,\vec e_{\nu(\mu)},
$$

the second term being the frame cell of $\mu$ applied to the trace spinor. Its entries are read from the action whenever a display needs them, $(P\psi)_\mu=\sum_\nu\varepsilon_\nu P_{\mu\nu}\psi_\nu$.

The trace of the projected field vanishes. The second term of $\Sigma(P\psi)$ carries the cell of $\mu$ twice in a row, and the square of a cell is $\varepsilon_\mu$ times the identity; with the weight in front the product is $\varepsilon_\mu^2=1$, so each of the four terms subtracts exactly one quarter of the trace:

$$
\Sigma(P\psi)=\Sigma(\psi)-\tfrac14\sum_\mu\varepsilon_\mu\,i\,e_\mu\bigl(i\,e_\mu\,\Sigma(\psi)\,\vec e_{\nu(\mu)}\bigr)\vec e_{\nu(\mu)}=\Sigma(\psi)-\Sigma(\psi)=0 .
$$

The projector is idempotent, and the proof is the line above read twice: its output has no trace, so applying it to that output subtracts nothing. It annihilates the trace on either side of its two indices, and both annihilations are the same square of a cell.

The rank of the projector on the sixteen components of the vector-spinor is

$$
\boxed{\;\mathrm{rank}\,P = 12 = 16-4\;},
$$

verified by Gaussian elimination over the complex numbers, so that the trace constraint removes exactly a four-component spinor from the sixteen components of the vector-spinor.

## Gauge Structure: Massless and Massive

### The Massless Case

When $m=0$ the Rarita–Schwinger field has a gauge symmetry,

$$
\psi_\mu \;\longmapsto\; \psi_\mu+\partial/\partial x_\mu\,\epsilon ,
$$

with $\epsilon$ an arbitrary spinor parameter. The transformation changes $\psi_\mu$ by a gradient of a spinor, and it is the spin-$\tfrac32$ analogue of the gauge transformation of the vector field. The two objects are preserved for different reasons. The field equation survives for every $\epsilon$, because the kinetic structure is antisymmetric in the derivative index and the two derivatives of the gradient commute. The trace constraint survives only when the parameter satisfies the massless Dirac equation, $\mathbb{D}\epsilon=0$, since the gradient shifts the trace by $\mathbb{D}\epsilon$. The gauge symmetry is a **first-class** structure: the primary constraint $\pi_0\approx0$ and the divergence constraint $\partial\cdot\pi\approx0$ are first class, the trace is a gauge choice that meets each orbit once, and the physical content is the quotient of the constraint surface by the gauge orbits. The trace gauge is the analogue of the Lorentz gauge, and it leaves a residual gauge freedom whose quantization requires Faddeev–Popov ghosts — Grassmann-even (commuting) **spinor** ghosts, in the Dirac representation of the gauge parameter. The physical states are the two helicities $\pm\tfrac32$; the helicities $\pm\tfrac12$ that the massless field would otherwise carry are removed by the gauge structure, exactly as the longitudinal and timelike states of the massless vector are removed.

### The Count of Physical States

The component counting makes the role of the constraints explicit. A vector-spinor has sixteen complex components. The trace constraint removes four, leaving twelve; the transversality condition $p\cdot\psi=0$ removes a further four on shell, leaving eight; the first-order field equation halves the remaining eight, leaving four, which are the four polarizations of the massive spin-$\tfrac32$ multiplet — the helicities $\pm\tfrac32$ and $\pm\tfrac12$ — for the particle, with the same four for the antiparticle of the complex field. The field equation does not project onto positive frequency; it is first order, and it halves the solution space of the second-order Klein–Gordon equation that follows on squaring.

The two helicities of largest magnitude are the genuinely new content of spin $\tfrac32$; the two helicities $\pm\tfrac12$ are the lower members of the same massive multiplet. The trace constraint removes the independent spin-$\tfrac12$ field that the two-index carrier would otherwise contain; it does not remove the $\pm\tfrac12$ helicities of the massive multiplet. In the massless case the gauge symmetry removes those helicities, leaving the two states $\pm\tfrac32$, so that the massless field has just two physical polarizations. The count was confirmed componentwise: the projector's rank of twelve is the statement that the trace removes four of the sixteen components, and the remaining steps are the standard on-shell reduction.

### The Massive Case

When $m\neq0$ the gauge symmetry is absent: the field equation is not invariant under $\psi_\mu\mapsto\psi_\mu+\partial/\partial x_\mu\,\epsilon$, because the mass term is not. The constraints are then **second class**: the trace and its conjugate do not commute weakly, and the canonical quantization must use the Dirac bracket rather than the Poisson bracket. The count of physical polarizations is the standard $2s+1=4$ for $s=\tfrac32$ — the helicities $\pm\tfrac32$ and $\pm\tfrac12$ — and no ghosts appear, since there is no gauge redundancy to fix. This is the same contrast as in the vector case: the massless field has a gauge redundancy and two physical states, the massive field has no redundancy and three (or, for spin $\tfrac32$, four) states, and the extra states are the ones the gauge would have removed.

## Canonical Quantization

### Momenta, Constraints, and Dirac Brackets

The canonical momentum conjugate to $\psi_\mu$ is, from the standard Rarita–Schwinger Lagrangian,

$$
\pi_\mu = \frac{\partial\mathcal{L}}{\partial(\partial/\partial t'\,\psi_\mu)}=\sum_\lambda T_{\lambda t\mu}\bigl(\bar\psi_\lambda\bigr),
\qquad
\bar\psi_\lambda:=\psi_\lambda^{\dagger}iR_{\vec e_x}^{\mathrm{axf}} ,
$$

the element the triple produces from the Dirac adjoint, with the normalization of the Lagrangian left free. The triple is the antisymmetrized product of three plain cells,

$$
T_{\mu\nu\rho}:=\tfrac1{3!}\sum_{\mathrm{perms}}\pm L_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\,L_{e_\nu}^{\mathrm{axf}}R_{\vec e_{\nu(\nu)}}^{\mathrm{axf}}\,L_{e_\rho}^{\mathrm{axf}}R_{\vec e_{\nu(\rho)}}^{\mathrm{axf}} .
$$

It is antisymmetric in its three indices and vanishes when two of them coincide. The cells anticommute, so the six terms of the sum are one and the same element, and the display is the definition that shows the antisymmetry; when two indices coincide the terms come in cancelling pairs. Its factors are plain cells rather than frame cells, so it carries no imaginary unit: the only one in the momentum is the $i$ of the adjoint, the same single $i$ that the Dirac article's momentum carries. The canonical analysis gives the primary constraint $\pi_0\approx0$ — automatic here, since $T_{\lambda t\mu}$ carries the time index in its middle slot, and $\mu=t$ puts it in the last slot too — together with the trace constraint and the conjugate constraints. The constraint algebra is second class for $m\neq0$, so the equal-time bracket is the Dirac bracket

$$
\{A,B\}_D = \{A,B\}_P-\sum_{a,b}\{A,\chi_a\}_P\,(\Delta^{-1})_{ab}\,\{\chi_b,B\}_P ,
\qquad
\Delta_{ab}=\{\chi_a,\chi_b\}_P ,
$$

with $\chi_a$ the second-class constraints. The effect of the Dirac bracket is to replace the naive anticommutator by the projected one: the fields are restricted to the constraint surface, and the algebra closes on the projected field $(P\psi)_\mu$ rather than on $\psi_\mu$ itself. This is the standard treatment and is cited below; the point to record is that the projection is the projector of the preceding section, so the algebraic content of the constraints is the biquaternion projector and its rank.

### Anticommutators and Modes

The quantized field is fermionic: the equal-time anticommutator of the field and its momentum is the projection of the naive anticommutator onto the constraint surface. Write $\vec x:=x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ for the spatial point and $\vec y$ for the same construction with $y$; then

$$
\{\psi_\mu(t',\vec x),\,\pi_\nu(t',\vec y)\}=i\,P_{\mu\nu}\,\delta^{(3)}(\vec x-\vec y) ,
$$

the naive $\delta_{\mu\nu}$ replaced by the entries of the projector of the preceding section, read from its action, and it is that projector that closes the algebra on $(P\psi)_\mu$. The mode expansion carries four polarizations,

$$
\psi_\mu(x) = \int\frac{d^3p}{(2\pi)^3}\frac{1}{\sqrt{2E_p}}
\sum_{r=1}^{4}\left[
a_r(\vec p)\,\xi_{\mu,r}(p)\,\exp(-ip\cdot x)
+ b_r^\dagger(\vec p)\,v_{\mu,r}(p)\,\exp(+ip\cdot x)
\right] ,
$$

with $E_p=\sqrt{\vec p^2+m^2}$, $p\cdot x=E_p t'-\vec p\cdot\vec x$, and with the Rarita–Schwinger polarization spinors satisfying

$$
\bigl(\mathbb{D}_p-m\bigr)\xi_{\mu,r}=0 ,
\qquad
\Sigma(\xi_r)=0 ,
\qquad
p\cdot\xi_r=0 ,
$$

together with the completeness relation of the four polarizations,

$$
\sum_{r=1}^{4}\xi_{\mu,r}\bar\xi_{\nu,r}=\bigl(\mathbb{D}_p+m\bigr)\Pi_{\mu\nu} .
$$

The object $\Pi_{\mu\nu}$ is the **transverse** traceless projector, the on-shell projector onto the intersection of the two constraints — the trace and the transversality — of rank eight on the vector-spinor space and four on the positive-energy solutions. It is not the constraint projector $P_{\mu\nu}$ of the preceding section: transversality requires the additional momentum-dependent terms, and the contraction of $p$ with the entries of $P$ does not vanish, so the completeness relation cannot be carried by $P_{\mu\nu}$ alone. It is the standard Rarita–Schwinger projector and is cited below. The creation and annihilation operators satisfy the fermionic algebra

$$
\{a_r(\vec p),\,a_s^\dagger(\vec k)\}
= \{b_r(\vec p),\,b_s^\dagger(\vec k)\}
= (2\pi)^3\,\delta_{rs}\,\delta^{(3)}(\vec p-\vec k) ,
$$

with all other anticommutators vanishing, and the Fock space is built by acting on the vacuum with $a_r^\dagger$ and $b_r^\dagger$. The four polarizations $r=1,\dots,4$ are the two helicities $\pm\tfrac32$ and the two helicities $\pm\tfrac12$.

The biquaternion interpretation of the mode expansion is the same as the Dirac article's, one vector index richer: each polarization spinor is an element of the algebra, labelled by the internal direction $r$ that the adjoint action supplies; the four internal labels are the four vectors of the spin-$\tfrac32$ representation, that is, the (traceless) product of the spin-$\tfrac12$ label with the material triplet.

### Fermionic Statistics

The field is quantized with anticommutators, not commutators, and the reason is the spin-statistics relation: the field carries half-integer spin, so its excitations are fermions. The framework's account of the relation, and the argument that only half-integer spins can be quantized with anticommutators while preserving positivity and microcausality, is the subject of the companion article on the spin–statistics theorem; here it is imported and used. The vector index does not change the statistics: a vector-spinor is still a spinor, and the material vector label is an internal label like any other, so the field is fermionic despite the integer index.

## The Propagator and Its Gauge Fixing

The momentum-space propagator is the inverse of the quadratic form that the field equation and the constraint define on the traceless subspace. It is of the general form

$$
G_{\mu\nu}(p) = -\frac{i}{p^2-m^2}\Bigl[\bigl(\mathbb{D}_p+m\bigr)\Pi_{\mu\nu} + \text{(lower-spin terms)}\Bigr] ,
$$

where the transverse projector $\Pi_{\mu\nu}$ is the one of the completeness relation and the lower-spin terms are the parts that the constraint removes; in the standard covariant form the propagator carries the gauge-fixing dependence of the massless case and a $p_\mu p_\nu$ term whose coefficient involves $1/m^2$ for the massive case. The detailed form, including the dependence on the gauge-fixing parameter and the $D$-dimensional continuation, is the standard result and is cited below; the framework's contribution is the identification of the trace part of the projector with the algebra's traceless projector and the interpretation of the lower-spin terms as the removed $\left(\tfrac12\right)$ component.

The massless case requires the gauge fixing, and the gauge-fixing parameter enters the propagator in the same way as in the vector case, through the longitudinal-traceless decomposition of the field. The ghost fields are spinor and commuting, so they live in the spinor carrier tensored with the even part of the algebra; the BRST structure is the standard one, with the gauge parameter now a spinor.

## The Biquaternion Reading

The algebraic content of this article is the tensor-product decomposition and the constraint that selects the top component, and it is worth stating in the framework's terms.

The carrier is the material four-vector index tensored with the spinor carrier $S$ of the Dirac article, sixteen complex components before the constraint. Its spatial part is the material triplet $V$, the adjoint action's carrier, and the triplet tensored with the spinor decomposes under the rotation algebra as

$$
1\otimes\tfrac12 = \tfrac12\oplus\tfrac32 ,
\qquad
3\cdot 2 = 4+2 ,
$$

the spin-$\tfrac32$ piece of dimension four and a spin-$\tfrac12$ piece of dimension two. The trace constraint removes the spin-$\tfrac12$ piece, and the projector that does it is $(P\psi)_\mu=\psi_\mu-\tfrac14\,i\,e_\mu\Sigma(\psi)\vec e_{\nu(\mu)}$, whose rank on the sixteen components of the vector-spinor is twelve — the four removed components being exactly the spin-$\tfrac12$ trace. This was verified by the explicit rank computation. The massive multiplet is the spin-$\tfrac32$ piece, with its four polarizations; the massless field, when the gauge symmetry is present, keeps the two states of helicity $\pm\tfrac32$ and the gauge removes the $\pm\tfrac12$ members of the same multiplet.

The parallel with the integer-spin case is close. There, the carrier is a tensor power of the material vector and the trace removal selects the top component: for the graviton, the symmetric trace-free square, $1\otimes1$ symmetric and traceless $=2$ with dimension five, verified by the transverse-traceless projection. Here, the carrier is the material vector tensored with the spinor, and the trace removes the lower component: $1\otimes\tfrac12=\tfrac32\oplus\tfrac12$, with the $\tfrac32$ of dimension four retained. In both cases the framework's statement is the same: the higher-spin field is obtained by tensoring the material vector with a lower-spin carrier and projecting onto the top component with a projector built from the algebra's own invariant form — the metric pairing for the integer-spin case, the trace for the half-integer one. The difference is that the spinor carrier is not a tensor power of the vector, and that is why the half-integer case requires the frame cells while the integer case does not.

## Consistency of the Coupled Theory

A spin-$\tfrac32$ field is not consistent as a fundamental field in an arbitrary background, and the reason is visible in the constraint structure developed above. Transversality followed from the field equation and the trace constraint through the trace identity of the transversality section, and that derivation used the free field equation. Coupling the field to a background — an electromagnetic field or the gravitational field — changes the field equation, and the change modifies the contraction by terms involving the background field strength or curvature. The constraint then ceases to be preserved by the evolution unless the background satisfies its own equations of motion: for the gravitational coupling the consistency condition is that the background be a solution of the Einstein equations, which is the Deser–Kay–Stelle condition of supergravity, and for the electromagnetic coupling the analogous condition (the Velo–Zwanziger analysis) restricts the background field strength and, when it fails, admits modes propagating faster than light. In the framework's terms the statement is that the trace constraint is preserved by the free evolution but not by the coupled evolution, so the removal of the $\left(\tfrac12\right)$ component is maintained only when the background is on shell. This is why the spin-$\tfrac32$ field is treated either as the gauge field of local supersymmetry, whose consistency is tied to the background geometry, or as an effective field with a cutoff; the framework does not change the conclusion, and it exhibits the mechanism through its projector.

## The Pattern Across the Spins

The three quantized fields of this subcategory — the vector, the Rarita–Schwinger field, and the graviton — share one structure, and the sharing is the framework's main statement about higher spins.

In each case the carrier is a tensor product of a lower-spin object with the **material vector index** — the triplet $V$ for the integer cases, the material four-vector for the Rarita–Schwinger field, whose spatial part is the same triplet — on which the adjoint action generates the spin-one rotation: the vector field is $V$ itself, with dimension three; the Rarita–Schwinger field is the material four-vector tensored with the spinor $S$, of dimension sixteen, reduced to twelve by the trace constraint; and the graviton is the symmetric trace-free square of $V$, with dimension five. In each case a projector built from the algebra's invariant form selects the top-spin component: the metric pairing for the integer cases, the trace for the half-integer one, and the traceless-and-symmetric projection for the graviton. And in each case the physical count is the standard one: $2s+1$ states for the massive field, and two states of helicity $\pm s$ for the massless field.

| $s$ | $\text{carrier}$ | $\dim$ | $\text{massive} \to \text{massless}$ |
|---|---|---|---|
| $1$ | $V$ | $3$ | $3 \to 2$ |
| $\tfrac32$ | $(\text{material four-vector})\otimes S$ | $12$, of which $4$ on shell | $4 \to 2$ |
| $2$ | $(V\odot V)_{\text{traceless}}$ | $5$ | $5 \to 2$ |

The massless limit takes the count to two in every case, because the gauge symmetry removes the helicities below $s$; the framework sees this as the removal of the lower-spin components that the tensor product contains, and the projector that performs the removal is the same one that defines the field. The pattern is not a derivation of the fields — their existence and their couplings are inputs — but it is a uniform account of why the higher-spin fields have the carriers, the constraints, and the counts that they do.

## What the Algebra Supplies and What It Imports

**Supplied by the algebra, and recomputed here.** The vector index as the material vector, whose spatial part is the triplet on which the adjoint action acts; the spinor index as the carrier of the Dirac article; the tensor-product decomposition $1\otimes\tfrac12=\tfrac32\oplus\tfrac12$ with $3\cdot2=4+2$; the traceless projector $(P\psi)_\mu=\psi_\mu-\tfrac14\,i\,e_\mu\Sigma(\psi)\vec e_{\nu(\mu)}$, its idempotency, its annihilation of the trace, and its rank twelve on the sixteen components, all verified with explicit frame cells; and the transversality $p\cdot\psi=0$ as a consequence of the constraint and the field equation, verified through the trace identity $\Sigma(\mathbb{D}_p\psi)=2p\cdot\psi-\mathbb{D}_p\Sigma(\psi)$.

**Imported, and left visible.** The Rarita–Schwinger equation and its antisymmetric Lagrangian origin, which belong to the classical theory of higher spins; the canonical momentum and the constraint algebra; the Dirac bracket and the quantization of second-class systems; the fermionic mode algebra and the Fock space; the spin–statistics relation, cited to the companion article on the theorem; the transverse Rarita–Schwinger projector $\Pi_{\mu\nu}$ and the completeness relation of the four polarization spinors; the propagator, its gauge-fixing dependence, and its dimensional continuation; the Faddeev–Popov ghosts of the massless case and their commuting spinor carrier; and the BRST structure, cited to the standard literature.

**Not supplied.** The value of the mass; the choice of gauge; the odd coordinates; the physical identification of the spin-$\tfrac32$ field with any observed particle; and any empirical content. The framework organizes the field and its constraints, and it does so by exhibiting them as a tensor product and a projection; it does not derive the field's existence.

## Open Questions

1. **The projector from the algebra alone.** The traceless projector is built from the frame cells. Is there a biquaternion expression of the projection — an operation on the tensor product $V\otimes S$ using only the algebra's structure — that does not pass through the frame cells, in the way the adjoint action expresses the spin-one projection without them?

2. **The massless ghosts and the sector split.** The ghosts of the massless Rarita–Schwinger field are spinor-valued and commuting. In which sector do they live, and does the sector split organize the ghost spectrum of higher-spin gauge fields in a way that differs from the vector case?

3. **The supergravity connection.** The spin-$\tfrac32$ field is the gravitino of supergravity, where it is the gauge field of local supersymmetry and the graviton is its partner. Does the biquaternion framework relate the gravitino's vector index to the material sector and its spinor index to the spinor carrier in a way that organizes the supermultiplet, or is the pairing invisible to the framework?

4. **Consistency and the supertrace.** The consistency of a higher-spin field coupled to gravity is governed by the supertrace of the theory — the difference of the numbers of bosonic and fermionic degrees of freedom. Is there a biquaternionic accounting of the supertrace for the spin-$\tfrac32$ field?

5. **The vZw and Fierz–Pauli structure.** The massless Rarita–Schwinger field has the van Dam–Veltman–Zakharov discontinuity in its massive limit, as the graviton does. Is the discontinuity visible in the framework's decomposition, as a change in the dimension of the projected carrier?

6. **Empirical content.** As everywhere, whether any of this yields a prediction distinguishing the framework from standard higher-spin theory. The transcription given here does not.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are the frame cells of the body written as single letters; they are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

$$
\gamma_\mu:=iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}\quad(\nu(t)=x,\ \nu(k)=y),
\qquad
\gamma_5:=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}},
$$

The same in the axis-free display:

$$
\gamma_\mu:=iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}\quad(\nu(t)=x,\ \nu(k)=y),
\qquad
\gamma_5:=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
$$

that is $\gamma_0=iR_{\vec e_x}^{\mathrm{pau}}$ and $\gamma_k=iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ for $k=1,2,3$. No display of the body uses the letter: there the cells are written as their two multipliers, and the letter is read once, here. A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality operator; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module. It anticommutes with each of the four frame cells and commutes with every even element, hence with the whole biquaternion image; its eigenspaces are the chiral halves of the spinor space, and it is the cell that exchanges the two lines of the chiral pair. The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The composites of the body.** The letter absorbs the imaginary unit of the cell, $i\gamma_\mu=-L_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}$, the two imaginary units multiplying to $-1$. The four composites named in the body are therefore

$$
\mathbb{D}=i\gamma\cdot\partial,
\qquad
\mathbb{D}_p=\gamma\cdot p,
\qquad
\Sigma(\psi)=\gamma\cdot\psi,
\qquad
T_{\mu\nu\rho}=i\gamma_{[\mu\nu\rho]},
$$

with $\gamma\cdot\partial$ and $\gamma\cdot p$ the metric contractions. $\mathbb{D}_p$ is $\mathbb{D}$ read at $\partial/\partial x_\mu\to-ip_\mu$, and that substitution is the single $i$ that separates the two; the triple $T$ differs from the antisymmetrized triple of frame cells by the same bookkeeping, three factors giving $(-i)^3=i$.

**The identities.** With $\varepsilon=(1,-1,-1,-1)$ and the sign vector $\varepsilon_\mu=-g_{\mu\mu}$,

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,
\qquad
\gamma_\mu^2=\varepsilon_\mu I_4,
\qquad
\gamma_\mu(\gamma\cdot p)=2p_\mu-(\gamma\cdot p)\gamma_\mu,
$$

$$
\gamma_5^2=I_4,
\qquad
\{\gamma_\mu,\gamma_5\}=0,
\qquad
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},
$$

with $\gamma_{\mu\nu}:=\tfrac12[\gamma_\mu,\gamma_\nu]$ for a pair and $\gamma_{\mu\nu\rho}:=\tfrac1{3!}\sum_{\mathrm{perms}}\pm\gamma_\mu\gamma_\nu\gamma_\rho$ for a triple. The third entry of the first display is the identity the transversality argument uses, written with the letter.

**The two Dirac equations.** The pair is one matrix equation written twice. With the chiral projectors $P_{L}:=\tfrac12(I_4-\gamma_5)$ and $P_{R}:=\tfrac12(I_4+\gamma_5)$, the two lines of the pair are the two chiral halves of $(i\gamma\cdot\partial-m)\psi_\mu=0$, the halves being $P_L\psi_\mu$ and $P_R\psi_\mu$; $\gamma_5$ anticommutes with the frame cells and exchanges the halves, so the single matrix equation carries both, and the cell equation of the body, which multiplies on both sides, is its transcription in cells.

**The displays of the body.** In the letter, the equation, the constraint, the projector and the momentum are

$$
(i\gamma\cdot\partial-m)\psi_\mu=0,
\qquad
\gamma\cdot\psi=0,
\qquad
P_{\mu\nu}=g_{\mu\nu}I_4-\tfrac14\gamma_\mu\gamma_\nu,
\qquad
\pi_\mu=i\psi^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}_\nu\,\gamma_{[\nu t\mu]},
$$

and the polarization equations, the completeness relation and the propagator are

$$
(\gamma\cdot p-m)\xi_{\mu,r}=0,
\qquad
\gamma\cdot\xi_r=0,
\qquad
p\cdot\xi_r=0,
$$

$$
\sum_{r=1}^{4}\xi_{\mu,r}\bar\xi_{\nu,r}=(\gamma\cdot p+m)\Pi_{\mu\nu},
\qquad
G_{\mu\nu}(p)=-\frac{i}{p^2-m^2}\Bigl[(\gamma\cdot p+m)\Pi_{\mu\nu}+\text{(lower-spin terms)}\Bigr].
$$

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Rarita–Schwinger field is a vector-spinor $\psi_\mu$ satisfying the chiral pair $\tilde\nabla\tilde\Psi_{\mu,R}=m\tilde\Psi_{\mu,L}$, $\tilde\nabla^{\natural}\tilde\Psi_{\mu,L}=m\tilde\Psi_{\mu,R}$ and the irreducibility constraint $\Sigma(\psi)=0$. On the spinor module the pair is the single equation $(\mathbb{D}-m)\psi_\mu=0$, the operator $\mathbb{D}$ carrying the product $i\cdot i=-1$ of its two imaginary units. The trace of the equation, taken with one use of the anticommutation relation of the cells, is $\Sigma(\mathbb{D}_p\psi)=2p\cdot\psi-\mathbb{D}_p\Sigma(\psi)$; with $\Sigma(\psi)=0$ it gives the transversality condition $p\cdot\psi=0$, verified on shell with explicit frame cells. The constraint is imposed by the projector $(P\psi)_\mu=\psi_\mu-\tfrac14\,i\,e_\mu\Sigma(\psi)\vec e_{\nu(\mu)}$, which is idempotent, annihilates the trace, and whose rank on the sixteen components of the vector-spinor is twelve, so that the constraint removes exactly a four-component spinor — all verified to machine precision.

The gauge structure differs between the two mass regimes. For $m=0$ the field has the gauge symmetry $\psi_\mu\mapsto\psi_\mu+\partial/\partial x_\mu\,\epsilon$ with a spinor parameter, the constraints are first class, the trace gauge fixing requires Faddeev–Popov commuting spinor ghosts, and the physical states are the two helicities $\pm\tfrac32$. For $m\neq0$ the gauge symmetry is absent, the constraints are second class, the quantization uses the Dirac bracket, and the physical states are the four helicities $\pm\tfrac32,\pm\tfrac12$. The canonical quantization gives a fermionic mode expansion with four polarizations, anticommutators $\{a_r(\vec p),a_s^\dagger(\vec k)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k)$, and a completeness relation whose transverse projector is built from the same frame cells.

In the biquaternion framework the field is the tensor product of the material four-vector index — whose spatial part is the adjoint-action triplet $V$ — with the spinor carrier $S$, and the tensor product decomposes as $1\otimes\tfrac12=\tfrac32\oplus\tfrac12$ with $3\cdot2=4+2$. The trace constraint removes the $\left(\tfrac12\right)$ component, and the surviving spin-$\tfrac32$ is the field. The structure is the close analogue, one tensor factor down, of the graviton's symmetric trace-free square of the material vector: in each case a lower-spin carrier is tensored with the material vector and projected onto the top component by a projector built from the algebra's invariant form. The mass, the gauge choice, the propagator's detailed form, the odd coordinates, and any empirical content are imported; the decomposition and the projection are the framework's.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\psi_\mu$ | Rarita–Schwinger vector-spinor; material vector index $\mu$, spinor index suppressed |
| $\psi\mapsto a\psi b$ | The action a display writes; a cell $L_{a}R_{b}$ is named only where the operator itself is the subject |
| $iL_{e_\mu}^{\mathrm{axf}}R_{\vec e_{\nu(\mu)}}^{\mathrm{axf}}$, $\nu(t)=x$, $\nu(k)=y$ | Frame cell of the coordinate $x_\mu$, acting as $\psi\mapsto i\,e_\mu\psi\vec e_{\nu(\mu)}$: $iR_{\vec e_x}^{\mathrm{axf}}$ for $\mu=t$, $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ for $\mu=k$ |
| $2\varepsilon_\mu\delta_{\mu\nu}$ on the identity action | The sum of the two compositions of two frame cells; their two imaginary units multiply to $-1$ |
| $\varepsilon_\mu=-g_{\mu\mu}$, $\varepsilon_0=+1$, $\varepsilon_k=-1$ | Sign vector; every contraction of two low indices carries it |
| $\tilde\nabla\tilde\Psi_{\mu,R}=m\tilde\Psi_{\mu,L}$, $\tilde\nabla^{\natural}\tilde\Psi_{\mu,L}=m\tilde\Psi_{\mu,R}$ | Field equation as the chiral pair; the two Dirac equations |
| $\mathbb{D}\psi=-\sum_\mu\varepsilon_\mu\,e_\mu(\partial\psi/\partial x_\mu)\vec e_{\nu(\mu)}$, $\mathbb{D}_p\psi=\sum_\mu\varepsilon_\mu\,i\,e_\mu\psi\vec e_{\nu(\mu)}p_\mu$ | Pair operator of the conventions article and its Fourier symbol; $\mathbb{D}^2=\Box$, $\mathbb{D}_p^2=p^2$, and the imaginary units of the cell and of the derivative are multiplied to $-1$ |
| $(\mathbb{D}-m)\psi_\mu=0$ | Cell transcription of the chiral pair |
| $\Sigma(\psi)=\sum_\mu\varepsilon_\mu\,i\,e_\mu\psi_\mu\vec e_{\nu(\mu)}=0$ | Trace spinor and irreducibility constraint; removes the $\left(\tfrac12\right)$ component |
| $p\cdot\psi=\sum_\mu\varepsilon_\mu p_\mu\psi_\mu=0$ | Transversality; follows from the constraint and the field equation |
| $\Sigma(\mathbb{D}_p\psi)=2\,p\cdot\psi-\mathbb{D}_p\Sigma(\psi)$ | Trace identity used; the trace of the operator times the field is the divergence minus the operator on the trace (verified) |
| $(P\psi)_\mu=\psi_\mu-\tfrac14\,i\,e_\mu\Sigma(\psi)\vec e_{\nu(\mu)}$, $(P\psi)_\mu=\sum_\nu\varepsilon_\nu P_{\mu\nu}\psi_\nu$ | Traceless projector; it annihilates the trace and is idempotent (verified) |
| $\mathrm{rank}\,P=12=16-4$ | Verified by Gaussian elimination over $\mathbb{C}$ |
| $V\otimes S$, $1\otimes\tfrac12=\tfrac32\oplus\tfrac12$ | Spatial part of the carrier and its decomposition; $3\cdot2=4+2$ |
| $\psi_\mu\mapsto\psi_\mu+\partial/\partial x_\mu\,\epsilon$ | Massless gauge symmetry; spinor parameter |
| $T_{\mu\nu\rho}$ | Antisymmetrized triple of three plain cells; antisymmetric, zero when two indices coincide, and $i\gamma_{[\mu\nu\rho]}$ in the gamma dictionary |
| $\pi_\mu=\sum_\lambda T_{\lambda t\mu}(\bar\psi_\lambda)$, $\bar\psi_\lambda:=\psi_\lambda^{\dagger}iR_{\vec e_x}^{\mathrm{axf}}$ | Canonical momentum, read as the triple applied to the Dirac adjoint; the triple is plain, so the $i$ of the adjoint is the only one |
| $\vec x:=x\vec e_x+y\vec e_y+z\vec e_z$ | Shorthand for the spatial point in the anticommutator and the delta function |
| $\{A,B\}_D$, $\Delta_{ab}=\{\chi_a,\chi_b\}_P$ | Dirac bracket and its constraint matrix (second-class constraints, $m\neq0$) |
| $\{a_r(\vec p),a_s^\dagger(\vec k)\}=(2\pi)^3\delta_{rs}\delta^{(3)}(\vec p-\vec k)$ | Fermionic mode algebra |
| $\xi_{\mu,r},v_{\mu,r}$, $r=1,\dots,4$ | Polarization spinors; helicities $\pm\tfrac32,\pm\tfrac12$ |
| $\Pi_{\mu\nu}$ | Transverse traceless (Rarita–Schwinger) projector; rank $8$, and $4$ on positive-energy solutions |
| $\sum_r \xi_{\mu,r}\bar\xi_{\nu,r}=(\mathbb{D}_p+m)\Pi_{\mu\nu}$ | Completeness relation, carried by the transverse projector |
| $G_{\mu\nu}(p)$ | Propagator; inverse of the quadratic form on the traceless subspace |
| $\varepsilon=(1,-1,-1,-1)$ | sign vector of the generators; the material interval is its negative |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- C. Becchi, A. Rouet and R. Stora, "Renormalization of Gauge Theories," *Annals of Physics* **98** (1976) 287–321, for the BRST symmetry that governs the gauge fixing of the massless field.
- W. Rarita and J. Schwinger, "On a Theory of Particles with Half-Integral Spin," *Physical Review* **60** (1941) 61, for the original vector-spinor equation and constraint.
- Paul A. M. Dirac, "Generalized Hamiltonian Dynamics," *Canadian Journal of Mathematics* **2** (1950) 129–148, for the constraint analysis and the quantization with constraints.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. I: Foundations* (Cambridge, 1995), for the canonical quantization of fields with constraints and the spin–statistics connection.
- Steven Weinberg, *The Quantum Theory of Fields, Vol. III: Supersymmetry* (Cambridge, 2000), for the spin-$\tfrac32$ field, its propagator, and its role as the gravitino.
- Daniel Z. Freedman and Antoine Van Proeyen, *Supergravity* (Cambridge, 2012), for the Rarita–Schwinger action, the consistency conditions, and the supertrace.
- Marc Henneaux and Claudio Teitelboim, *Quantization of Gauge Systems* (Princeton, 1992), for first-class and second-class constraints and the Dirac bracket.
- Stanley Deser, J. H. Kay and K. S. Stelle, "Renormalizability Properties of Supergravity," *Physical Review Letters* **38** (1977) 527–530, for the consistency of the spin-$\tfrac32$ field coupled to gravity.
- G. Velo and D. Zwanziger, "Propagation and Quantization of Rarita–Schwinger Waves in an External Electromagnetic Potential," *Physical Review* **186** (1969) 1337–1341, for the loss of the constraint and the superluminal modes in a background.
