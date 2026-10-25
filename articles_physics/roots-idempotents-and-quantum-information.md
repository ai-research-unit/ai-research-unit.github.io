# __Roots, Idempotents and Quantum Information__

## Introduction

The Hermitian idempotents of the biquaternion algebra are the pure states of the informational sector, and the Hermitian roots of $+1$ are its involutive observables. The halving map

$$
\tilde\Pi=\tfrac12(e_t+\tilde\Xi),\qquad \tilde\Xi=2\tilde\Pi-e_t
$$

passes from one to the other. That dictionary was built in *Roots, Idempotents and Observables*. This article reads the same objects through the questions of quantum information: which observables can be measured together, what a measurement with unsharp outcomes is, what protects a state from error, which bases are mutually unbiased, and what a shared entangled state accomplishes.

Five interpretations are developed: contextuality, positive operator-valued measures, error-correcting code spaces, mutually unbiased bases, and teleportation. A sixth statement is a boundary rather than an interpretation: the defining module is the two-dimensional spin-$\tfrac12$ representation and is irreducible, so the carrier has no spin-zero ray.

The algebra is the native qubit, $\mathbb{B}\cong M_2(\mathbb{C})$, and composites are tensor powers. The article owns no theorem. The classification of idempotents, the Peirce decomposition, the plain form and the unitary group are stated in the mathematics articles linked below, and the identities that the article uses are either standard or verified in two or three lines.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The roots of $+1$, the halving map and the idempotents | [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html) |
| Orthogonality, completeness, primitivity and the Peirce decomposition | [Ideals and Peirce Decompositions of the Biquaternion Algebra](../articles_maths/ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html) |
| The positive cone, the order interval and its extreme points | [Jordan Algebras and the Positive Cone](../articles_maths/jordan-algebras-and-the-positive-cone.html) |
| The plain form and the Hilbert–Schmidt form (proportional by $1/2$) | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), [The General Plain Sesqualgebra in the $2\times2$ Matrix Element Representation](../articles_maths/the-general-plain-sesqualgebra-in-the-2x2-matrix-element-representation.html) |
| The unitary group and the matrix-unitary condition | [Unitary Operators of a Sesqualgebra](../articles_maths/the-unitary-operators-of-a-sesqualgebra.html) |
| The tensor product and the isomorphism $M_m\otimes M_n\cong M_{mn}$ | [Tensor Products of Algebras](../articles_maths/tensor-products-of-algebras.html) |

## Contexts and the Kochen–Specker Obstruction

A **context** is a maximal set of mutually commuting observables. In the algebra it is the Hermitian part of a maximal commutative $*$-subalgebra of $\mathbb{B}$, and its spectral resolution is a complete family of orthogonal idempotents:

$$
\tilde\Pi_a\tilde\Pi_b=\delta_{ab}\tilde\Pi_a,\qquad \sum_a\tilde\Pi_a=e_t .
$$

A **noncontextual value assignment** is a map $v$ from the Hermitian elements to the reals that is linear and multiplicative on every context, with $v(e_t)=1$ and $v(\tilde\Pi)\in\{0,1\}$ on idempotents. The Kochen–Specker theorem says that in dimension at least three no such assignment exists.

Two facts fix the interpretation.

- **The native qubit has no obstruction.** The defining module is two-dimensional, every context is a pair of orthogonal rank-one idempotents, and a consistent assignment is available. Fix a hidden direction $\vec u_\lambda$ and set $v_\lambda(\tilde\Pi_{\pm}(\vec u))=1$ when $\pm\vec u\cdot\vec u_\lambda>0$ and $0$ otherwise, with $\tilde\Pi_{\pm}(\vec u)=\tfrac12(e_t\pm i\vec u)$, a convention on the measure-zero equator, and linear extension. Exactly one idempotent of each antipodal pair receives $1$. No ray belongs to two distinct contexts (the identity, which belongs to all, imposes no constraint), so noncontextuality is vacuous.
- **The smallest arena is the two-qubit algebra.** $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$ has a four-dimensional module, and it carries the Mermin–Peres square.

The square uses the Pauli gates $X=i\vec e_x$, $Y=i\vec e_y$ and $Z=i\vec e_z$, with the identity written $e_t$ in each factor.

| | column 1 | column 2 | column 3 |
| --- | --- | --- | --- |
| row 1 | $X\otimes e_t$ | $e_t\otimes X$ | $X\otimes X$ |
| row 2 | $e_t\otimes Y$ | $Y\otimes e_t$ | $Y\otimes Y$ |
| row 3 | $X\otimes Y$ | $Y\otimes X$ | $Z\otimes Z$ |

Each row and each column is a commuting triple. The product of every row is $e_t\otimes e_t$, the product of the first two columns is $e_t\otimes e_t$, and the product of the third column is $-e_t\otimes e_t$, because $XYZ=i\,e_t$ and $(XYZ)\otimes(XYZ)=(i\,e_t)\otimes(i\,e_t)=-e_t\otimes e_t$. A noncontextual $\{\pm1\}$ assignment would make the product of the nine entries both $+1$ and $-1$.

**Interpretation.** A context is a measurement basis and its idempotents are the outcomes. Contextuality is the failure of one outcome table to serve every basis at once. The algebra supplies the contexts and the idempotent resolutions natively; the obstruction appears as soon as the module is large enough to share an observable between two contexts.

**Boundary.** The obstruction is not a property of the biquaternion algebra alone. It requires dimension at least three, and the native carrier has dimension two, so the interpretation lives on a composite. The magic square is the smallest instance, and its construction uses the tensor product, whose status in the framework is an open question.

## Sharp and Soft Effects: POVMs

A **sharp effect** is an idempotent: a projection whose only values are $0$ and $1$. The sharp effects are the extreme points of the operator interval

$$
[\tilde 0,e_t]=\{\tilde E\in\mathbb{M}_+:\tilde 0\le\tilde E\le e_t\},
$$

where the order is the positivity of $e_t-\tilde E$. The proposition that the extreme points are exactly the idempotents is the Jordan-algebra statement proved in the linked article.

A general effect of the qubit has a spectral resolution

$$
\tilde E=\lambda_1\tilde\Pi_1+\lambda_2\tilde\Pi_2,\qquad 0\le\lambda_1,\lambda_2\le 1,
$$

in some idempotent basis, and it is soft when one eigenvalue lies strictly between $0$ and $1$. A **POVM** is a finite family $\{\tilde E_a\}$ of effects with $\sum_a\tilde E_a=e_t$, and the Born weight of an outcome is the normalised Hermitian form $\langle\tilde{Ϛ},\tilde E_a\rangle_{*}/\langle\tilde{Ϛ},e_t\rangle_{*}=\mathrm{Sc}(\tilde{Ϛ}\tilde E_a^{*})/\mathrm{Sc}(\tilde{Ϛ})$, whose trace reading at normalisation is $\operatorname{Tr}(\tilde{Ϛ}\tilde E_a^{*})=\operatorname{Tr}(\tilde{Ϛ}\tilde E_a)$, the star being inert on $\mathbb{M}_+$ and the unstarred trace real and non-negative.

**Interpretation.** A measurement is a resolution of the identity into effects. The sharp outcomes are the idempotents, the unsharp ones are their convex combinations, and the state space is the same in both cases. Naimark's dilation theorem makes every POVM a projective measurement on a larger module, so the sharp idempotent remains the primitive object and the soft effect is a shadow of a projection on an enlarged space.

**Boundary.** The algebra supplies the effects, the order and the dilation. It does not supply the instrument, the map from outcomes to posterior states, and it does not supply the dynamics of the apparatus. A POVM is a statement about statistics, not about what the apparatus does.

## Stabilizer Codes: Idempotents and Images

A **stabilizer group** on $n$ qubits is an abelian subgroup $S$ of the Hermitian involutions of $\mathbb{B}^{\otimes n}$ that does not contain $-e_t^{\otimes n}$. The **code idempotent** is the average

$$
\tilde\Pi_S=\frac{1}{|S|}\sum_{\tilde U\in S}\tilde U .
$$

For $\tilde U\in S$ one has $\tilde U\tilde\Pi_S=\tilde\Pi_S$, so $\tilde\Pi_S^2=\tilde\Pi_S$; and $\operatorname{Tr}\tilde\Pi_S=2^n/|S|$, because the trace of a nontrivial Pauli tensor vanishes and the trace of the identity is $2^n$. The code space is the image of $\tilde\Pi_S$ on the module $(\mathbb{C}^2)^{\otimes n}$, the common $+1$ eigenspace of $S$. On the algebra side, $\tilde\Pi_S\mathbb{B}^{\otimes n}\tilde\Pi_S$ is the Peirce corner and $\tilde\Pi_S\mathbb{B}^{\otimes n}$ the corresponding left ideal.

The **Knill–Laflamme condition** for an error set $\{\tilde E_a\}$ is

$$
\boxed{\;\tilde\Pi_S\tilde E_a^{*}\tilde E_b\tilde\Pi_S=c_{ab}\tilde\Pi_S\;}
$$

for all $a,b$. It says that the errors, compressed to the code, are scalar multiples of the code idempotent, so they can be detected and reversed without distinguishing the encoded states.

The three-qubit bit-flip code is the smallest example. Its stabilizer group is

$$
S=\{e_t^{\otimes3},Z_1Z_2,Z_2Z_3,Z_1Z_3\},\qquad |S|=4,
$$

so the code idempotent has trace $8/4=2$ and the code space is two-dimensional. The same construction gives the five-qubit code, where the stabilizer group has order $16$ and the code idempotent has trace $32/16=2$.

**Interpretation.** A code is an idempotent, and its logical subspace is the image of that idempotent; the Peirce corner is its algebra-side counterpart. Encoding is the choice of the idempotent, the syndrome measurement is the family of idempotents that resolves it, and the error condition says that the errors act on the component as scalars.

**Boundary.** The algebra gives the code subspace and the exact condition. It gives no threshold, no noise model and no fault-tolerance analysis, because those are statements about a physical error process and not about the algebra.

## The Three Unbiased Bases

A **basis of the module** is a complete family of orthogonal rank-one idempotents:

$$
\tilde\Pi_i\tilde\Pi_j=\delta_{ij}\tilde\Pi_i,\qquad \sum_i\tilde\Pi_i=e_t,\qquad \operatorname{Tr}\tilde\Pi_i=1 .
$$

For the qubit the rank-one idempotents are $\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u)$ with $\vec u$ a unit vector, and the Hilbert-space overlap of two rays is the normalised Hermitian form, read through the trace:

$$
\lvert\langle\psi|\phi\rangle\rvert^2=\operatorname{Tr}\bigl(\tilde\Pi(\psi)\tilde\Pi(\phi)\bigr).
$$

Two bases are **mutually unbiased** when every overlap across them is $1/d$; for the qubit $d=2$, so every cross trace is $\tfrac12$. The three bases are the eigenbases of the three Hermitian involutions $i\vec e_x$, $i\vec e_y$ and $i\vec e_z$. The units pairwise anticommute, and the normalised Hermitian form of idempotents from different bases, read as the trace pairing, is

$$
\boxed{\;\operatorname{Tr}\bigl(\tilde\Pi_i^{(b)}\tilde\Pi_j^{(b_2)}\bigr)=\tfrac12\qquad(b\ne b_2)\;}.
$$

**Interpretation.** The three coordinate measurements are the three unbiased bases, and their completeness is the tomographic statement that three outcome probabilities determine the Bloch vector. The outcome probabilities in the basis along $\vec e_k$ are

$$
p_k(\pm)=\tfrac12(1\pm r_k),\qquad r_k=p_k(+)-p_k(-),
$$

so the three bases reconstruct the state. The algebra's three imaginary units are the three bases; mutual unbiasedness is the anticommutation of the units seen through the trace.

**Boundary.** The qubit supplies the three bases natively. The two-qubit maximum is five, and the tensor product of qubit bases gives only three. The Bell basis does not complete the three product bases to a fourth: with respect to each of the computational, $X$ and $Y$ product bases, every Bell vector is orthogonal to half of the basis vectors, so the cross overlaps are $0$ or $\tfrac12$ and not uniformly $\tfrac12$. The algebra does not supply a complete set of unbiased bases by naive tensor product.

## Teleportation: Four Idempotents and Four Unitaries

The four **Bell idempotents** of $\mathbb{B}\otimes\mathbb{B}$ are

$$
\boxed{\;\tilde\Pi_\epsilon=\tfrac14\bigl(e_t\otimes e_t+\epsilon_1\vec e_x\otimes\vec e_x
+\epsilon_2\vec e_y\otimes\vec e_y+\epsilon_3\vec e_z\otimes\vec e_z\bigr),
\qquad \epsilon_1\epsilon_2\epsilon_3=+1\;}.
$$

Each is Hermitian, idempotent and of trace one; the four are pairwise orthogonal and sum to $e_t\otimes e_t$; the partial trace of each is the maximally mixed state $\tfrac12 e_t$. The identities follow from $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$: distinct signs give a traceless product, the trace of each is $2^2/4=1$, and tracing the second factor leaves $\tfrac12e_t$. None is unitary, since $\tilde\Pi_\epsilon^{*}\tilde\Pi_\epsilon=\tilde\Pi_\epsilon\ne e_t\otimes e_t$.

The protocol uses three qubits. Alice holds the unknown state, the pair is in the state $\tilde\Pi_{\Phi^+}$, she measures the Bell basis on her two qubits, and the four outcomes occur with probability $\tfrac14$. Each outcome leaves Bob's qubit in a unitary image of the unknown state, and the correction is one of the four Pauli gates $\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$, up to a phase. With the outcome record and the correction, the net map is the identity channel; without the record, Bob's state is $\tfrac12e_t$ and nothing is transferred. Alice's two qubits are left in a Bell state, so each of her qubits is maximally mixed and no copy of the unknown state survives.

**Interpretation.** The resource and the measurement are idempotents; the corrections are unitaries. Teleportation is the clearest place where the two classes of acting element are forced apart: an idempotent is a definite outcome and is not reversible, a unitary is reversible and is not an outcome. The Bell idempotents are the canonical idempotent basis of the two-qubit algebra relative to the tensor structure, and the protocol is their operational interpretation.

**Boundary.** The two classical bits are not an element of the algebra. The protocol is the algebra plus a classical channel, and the channel is where the non-algebraic step sits. The tensor-product arena is assumed, not derived.

## The Carrier Has No Spin-Zero Ray

The defining module of $\mathbb{B}\cong M_2(\mathbb{C})$ is $\mathbb{C}^2$, and the Lorentz action on it is the spin-$\tfrac12$ representation. That representation is irreducible: a spin-zero ray would be a line fixed by every Lorentz transformation, and the only fixed vector is $0$. The algebra has no one-dimensional module either, so a scalar is not a ray of the carrier at all. The centre acts on the module by scalars, but a scalar multiple of a vector is the same ray, not a one-dimensional submodule.

**Interpretation.** Every state of the defining module is spin-$\tfrac12$. A spin-zero object can appear only as a singlet in a tensor power, not as a ray of the carrier. There is no scalar sector in the state space: a scalar field, if the framework uses one, is not a state of this module. The statement is the algebraic form of the fact that the carrier is a spinor.

**Boundary.** The statement is about the defining module of this algebra. It does not say that no spin-zero object can appear in a larger construction; it says that the native carrier does not contain one.

## Entanglement Is Not a Fifth Job

The four jobs are jobs of one product on one algebra. Entanglement is a property of the **tensor square**, not a fifth product. The tensor square $\mathbb{B}\otimes\mathbb{B}$ has no sector of its own: a vector $v\otimes w$ is not material or informational, and the form on it is the tensor square of the one-sector form. The correlations the framework can describe are therefore between the two tensor factors — between the rows, not inside one row — and the partial trace is taken over one factor and lands in the other.

The partial trace is not one of the four products. It uses the trace pairing on the factor that is traced out and the identity on the factor that remains; it is a map on the tensor square, and it has no analogue inside a single algebra. This is why entanglement is not a fifth row of the grid: the grid classifies products on $\mathbb{B}$, and the partial trace lives one level up.

**The interpretation.** A correlation is a statement about two copies, not a new operation on one. The algebra supplies the tensor square, the Bell idempotents and the partial trace; the nonlocal content is in the tensor structure, not in an additional product.

**The boundary.** The tensor product is assumed, not derived; the algebra is one-mode, and the two-qubit arena is $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$. No dynamics, no channel and no measure of entanglement are supplied. The reading does not say that entanglement is reducible to a product, only that it is not a product of the same kind.

## The Interpretations

The six interpretations share one theme: the idempotent is the native object of measurement and of the state, and the unitary is the native object of motion; entanglement adds no new object of that kind, only a property of the tensor square.

- **Contextuality** reads a context as a maximal commutative subalgebra and its outcomes as idempotents; the obstruction is the failure of one value table to serve all contexts, and it appears only on a composite.
- **POVMs** read a measurement as a resolution of the identity into effects; the sharp effects are the idempotents, and the soft ones are their convex combinations.
- **Error correction** reads a code as an idempotent and its logical subspace as the image of that idempotent, with the Peirce corner as the algebra-side counterpart.
- **Unbiased bases** read the three coordinate measurements as the three idempotent bases of the qubit, with the normalised Hermitian form as the overlap.
- **Teleportation** reads the resource and the measurement as Bell idempotents and the corrections as unitaries.
- **Entanglement** reads a correlation as a property of the tensor square, not a fifth product; the partial trace is taken over one factor, and the correlations live between the rows, not inside one.

The theme is not an analogy. In the first five cases the object that the information-theoretic construction names is an element of the algebra, and the operation it names is one of the algebra's own operations: commutation for a context, the order interval for an effect, the Peirce corner for a code, the normalised Hermitian form for an overlap, the tensor product for a shared state. Entanglement is the exception that proves the rule: its object is the tensor square, and its operation, the partial trace, lives one level up. What the algebra adds is the exactness of the statement and the boundary where it stops.

## Limits

- **The obstruction needs a composite.** The native qubit has no Kochen–Specker obstruction; the magic square lives in $\mathbb{B}\otimes\mathbb{B}$.
- **The tensor product is assumed.** The two-qubit algebra is used as $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$; whether the tensor product is canonical for the framework is an open question inherited from the companion articles.
- **No classical channel.** The algebra represents the outcome label and the correction, not the transmission of the label.
- **No thresholds and no error models.** The code condition is exact; the fault-tolerance analysis is not in the algebra.
- **No dynamics.** Every interpretation is a statement about states, effects and bases; none supplies an equation of motion.
- **The Bell basis is relative to the tensor structure.** It is canonical once the tensor product is fixed, and it is not claimed to be canonical without it.
- **Three standard results are cited, not proved.** The Kochen–Specker theorem, Naimark's dilation theorem and the maximum of five mutually unbiased bases in dimension four are named as standard results; the mathematics corpus does not own them, and the article does not derive them.

## Summary

The Hermitian idempotents are the pure states and the Hermitian roots of $+1$ are the involutive observables; the halving map is the dictionary between them. Six information-theoretic constructions are read here. A context is a maximal commutative subalgebra, its outcomes are a complete family of orthogonal idempotents, and the Kochen–Specker obstruction is the failure of a single value assignment to serve every context; on the native qubit there is no obstruction, and the smallest arena is the two-qubit algebra with the Mermin–Peres square. A POVM is a resolution of the identity into effects; the sharp effects are the idempotents, the extreme points of the order interval, and the soft ones are their convex combinations. A stabilizer code is an idempotent, its code space the image of that idempotent, and the Knill–Laflamme condition the exact statement that the errors act on it as scalars. The three unbiased bases of the qubit are the eigenbases of the three imaginary units, and the normalised Hermitian form is the overlap, read as the trace pairing. Teleportation forces apart the two classes of acting element: the resource and the measurement are Bell idempotents, the corrections are unitaries. Entanglement is not a fifth job: a correlation is a property of the tensor square, and the partial trace is taken over one factor rather than inside a row. The carrier itself has no spin-zero ray, because the defining module is the irreducible spin-$\tfrac12$ representation. Each interpretation names an element or an operation of the algebra, or a property of its tensor square, and each has a boundary: the obstruction needs a composite, the protocols need a classical channel, and none of them is a dynamics.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| $\mathbb{M}_+$ | The Hermitian (informational) sector |
| $\tilde\Pi$ | An idempotent; a rank-one idempotent is a pure state |
| $\tilde\Pi_\pm(\vec u)=\tfrac12(e_t\pm i\vec u)$ | The two rank-one idempotents along a unit vector $\vec u$ |
| $\tilde\Xi$ | A root of $+1$; $\tilde\Pi=\tfrac12(e_t+\tilde\Xi)$ |
| $\operatorname{Tr}$ | The trace, with $\operatorname{Tr}e_t=2$ |
| $[\tilde 0,e_t]$ | The order interval of effects |
| $\tilde\Pi_\epsilon$ | A Bell idempotent of $\mathbb{B}\otimes\mathbb{B}$ |
| $X,Y,Z$ | The Pauli gates $i\vec e_x$, $i\vec e_y$, $i\vec e_z$ |
| $S$ | A stabilizer group, and $\tilde\Pi_S$ its code idempotent |

## Further Reading

- [Square Roots of One and the Idempotents of the Biquaternion Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the classification, the halving map and the pair map.
- [Ideals and Peirce Decompositions of the Biquaternion Algebra](../articles_maths/ideals-and-peirce-decompositions-of-the-biquaternion-algebra.html), for orthogonality, primitivity and the Peirce components.
- [Jordan Algebras and the Positive Cone](../articles_maths/jordan-algebras-and-the-positive-cone.html), for the order interval and its extreme points.
- [Unitary Operators of a Sesqualgebra](../articles_maths/the-unitary-operators-of-a-sesqualgebra.html), for the unitary group and the matrix-unitary condition.
- [Tensor Products of Algebras](../articles_maths/tensor-products-of-algebras.html), for $\mathbb{B}\otimes\mathbb{B}\cong M_4(\mathbb{C})$.
- [Roots, Idempotents and Observables](roots-idempotents-and-observables.html), for the state-observable dictionary read at length.
- [Contextuality and the Kochen–Specker Theorem in Biquaternionic Form](contextuality-and-the-kochen-specker-theorem-in-biquaternionic-form.html), for the magic square and the value assignments.
- [Quantum Error Correction and the Stabilizer Formalism in Biquaternionic Form](quantum-error-correction-and-the-stabilizer-formalism-in-biquaternionic-form.html), for the codes and the Knill–Laflamme condition.
- [Mutually Unbiased Bases and the Biquaternion Algebra](mutually-unbiased-bases-and-the-biquaternion-algebra.html), for the three bases and the reconstruction.
- [Quantum Teleportation in Biquaternionic Form](quantum-teleportation-in-biquaternionic-form.html), for the protocol and its channel-theoretic interpretation.
- [The Bell Basis as the Idempotent Basis of B⊗B](the-bell-basis-as-the-idempotent-basis-of-b-tensor-b.html), for the Bell idempotents and the partial traces.
