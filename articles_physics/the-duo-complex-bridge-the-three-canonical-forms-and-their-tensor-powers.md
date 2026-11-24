# __The Duo-Complex Bridge: The Three Canonical Forms and Their Tensor Powers__

## Introduction

The pair of systems has a positive theory, and it was in the corpus all along. The two previous articles prove what the material/informational split cannot do under composition: it cannot label a subsystem, and it collapses two corners into one. This article proves what the duo-complex space can do. It carries three canonical forms, each tensors, and the three tensor powers are the three structures of the $n$-qubit theory: the inner product, the norm, and the entanglement pairing.

The claim, in one sentence. The concurrence of two qubits is the modulus of the tensor square of the alternating form of $\mathbb{C}^2$, evaluated on the state, with no factor left to adjust; so the entanglement measure the corpus already uses is one of its own three canonical forms, applied to both factors.

Why this is a bridge and not an analogy. A bridge has to carry traffic in both directions. In one direction: a form on the one-qubit space produces an invariant of the two-qubit space, by tensoring. In the other: an invariant the corpus already computes — the concurrence — is exhibited as such a tensor, so the one-qubit form was there before the two-qubit computation was made. Neither direction is a metaphor; both are identities, and both are checked below.

The structure of the article. *The space and its three forms* fixes $\mathbb{C}^2$ and the three forms, with the point that two of them share a Gram matrix and are nevertheless different. *The tensor square and why it splits* records the $3\oplus1$ decomposition that the corpus already proves. *The three tensor powers* states what each form gives at $n$ factors. *The two-qubit identity* proves that the alternating tensor square is the determinant, hence the concurrence, with the inertia that the Bell basis exhibits. *The norm and the determinant are different* separates the two quadratic forms of the pair by their zero sets. *Which group preserves which* corrects a natural but false claim about a two-dimensional space of invariant forms. *The parity boundary* proves that odd $n$ kills the alternating form identically, which is why the three-qubit measures are quartic. *Charge conjugation as the same pairing* shows that the corpus's charge conjugation is the same object, and that two antilinear maps compose to the bilinear one. *Bilinearity as the criterion* states the rule that decides both this article and the previous one. *The Peirce route does not give a second qubit* removes the tempting wrong reading. *The conjugation trap* records an error that this work made and corrected.

The article uses the mathematics corpus for the forms themselves: [The Three Canonical Forms on $\mathbb{C}^2$](../articles_maths/the-three-canonical-forms-on-c2.html) for the definitions and the proof that they are not proportional, [The Tensor Square of $\mathbb{C}^2$](../articles_maths/the-tensor-square-of-c2.html) for the $3\oplus1$ splitting, [The Realification of $\mathbb{C}^2$](../articles_maths/the-realification-of-c2.html) for the real and imaginary parts of the Hermitian form, and [Duo-Complex Numbers](../articles_maths/duo-complex-numbers.html) for the space itself. In this category, [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html) supplies the obstruction that this article answers, [The Multi-Qubit Split, II](the-multi-qubit-split-ii-the-sign-condition-the-concurrence-form-and-the-central-bit.html) supplies the second quadratic form, and [The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$](the-bell-basis-as-the-idempotent-basis-of-b-tensor-b.html) supplies the coefficient array and the four idempotents.

## The Space and Its Three Forms

The space. A duo-complex number is a pair of complex numbers,

$$
Q=(Q_{\blacktriangle},Q_{\blacktriangledown})\in\mathbb{C}^2 ,
$$

of complex dimension two and real dimension four. The two scalar structures the corpus names are the ordinary complex structure and the one twisted by the quaternion conjugation; the space carries both, which is why it is called duo-complex and why a real four-dimensional space with two commuting complex structures is the same object as a complex two-dimensional space.

The Hermitian form.

$$
H(Q_1,Q_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}} .
$$

It is linear in the first slot, conjugate-linear in the second, Hermitian, and positive definite, with Gram matrix the identity, $\bigl(H(e_j,e_{\imath})\bigr)=\mathrm I_2$. Its real and imaginary parts are the Euclidean metric $g$ of inertia $(4,0)$ and, up to sign, the symplectic form $\Omega$ of the realification: $H=g-i\Omega$, with $\Omega(Q_1,Q_2)=g(JQ_1,Q_2)$. It is the only one of the three forms whose isotropic set is the origin.

The complex bilinear form.

$$
B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown} .
$$

It is $\mathbb{C}$-bilinear and symmetric, with Gram matrix the identity as well, nondegenerate, and complex-valued. The letter $B$ is the maths corpus's name for this form, fixed in [The Three Canonical Forms on $\mathbb{C}^2$](../articles_maths/the-three-canonical-forms-on-c2.html) and used in every article of the $\mathbb{C}^2$ category; it is kept here for that reason. It is not the $B$ of the biquaternion layer, which is the complex modulus of the vector part, $B^{2}=\sum_{\imath\in\{x,y,z\}}Q_{\imath}^{2}$ of [Algebra and Element Conventions](../articles_maths/algebra-and-element-conventions.html), and it is not the algebra $\mathbb{B}$; the three are different objects on different spaces. The collision is confined to this article, where only the form on $\mathbb{C}^2$ occurs, and the notation table names it. Written out on real coordinates $Q_\blacktriangle=u+iv$, $Q_\blacktriangledown=w+iz$ its quadratic form is

$$
B(Q,Q)=\bigl(u^{2}-v^{2}+2iuv\bigr)+\bigl(w^{2}-z^{2}+2iwz\bigr),
$$

whose real part has inertia $(2,2)$: the form grows in two directions and decreases in two. Its isotropic cone is the union of the two complex lines $Q_\blacktriangle=\pm iQ_\blacktriangledown$, meeting only at the origin.

The alternating form.

$$
\omega(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangledown}-Q_{1\blacktriangledown}Q_{2\blacktriangle},\qquad
\bigl(\omega(e_j,e_{\imath})\bigr)=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

It is $\mathbb{C}$-bilinear and alternating, nondegenerate, and its Gram matrix is the standard symplectic matrix. It is the determinant form of the two-dimensional space, in the precise sense that $\omega(Q_1,Q_2)$ is the determinant of the matrix whose columns are $Q_1$ and $Q_2$.

Two of the three have the same Gram matrix, and this is the point a reader trips on. The Gram matrix records the values of a form on pairs of basis vectors. The basis $e_1=(1,0)$, $e_2=(0,1)$ is real, and conjugation does nothing to a real number, so $H(e_j,e_{\imath})=B(e_j,e_{\imath})=\delta_{j\imath}$ and both matrices are the identity. A real basis cannot show where the conjugation sits.

The discriminator. Take $Q=(1,i)$, which lies on the isotropic cone of $B$:

$$
H(Q,Q)=1+\lvert i\rvert^{2}=2,\qquad B(Q,Q)=1+i^{2}=0 .
$$

Same matrix, opposite outcomes. The rule is that a Gram matrix is not the form: for a sesquilinear form the reconstruction is $H(Q_1,Q_2)=Q_1^{\mathsf T}G\,\overline{Q_2}$, and for a bilinear form it is $B(Q_1,Q_2)=Q_1^{\mathsf T}G\,Q_2$. The same $G$, a different formula, and the bar is the whole of the difference.

**The three are not proportional.** The corpus proves it, and the discriminator above shows one instance: proportional forms have the same isotropic set, and $H$ has none while $B$ has a cone.

A caution on the alternating form and the imaginary part of $H$. The forms $\omega$ and $\operatorname{Im}H$ are both alternating and both nondegenerate, and they are not the same form. They are distinguished by their symmetry groups, which is the subject of a later section: $g^{\mathsf T}\omega\,g=(\det g)\,\omega$, so $\omega$ is preserved by $SL_2(\mathbb{C})$ and only by it, while $\operatorname{Im}H$ is preserved by $U(2)$ because $H$ is. A reader who takes "symplectic form of the space" as a single object will conflate them.

Three levels of equivalence, so that "no equivalent" is not read into the correspondence. The three statements are different and all three are needed.

- On $\mathbb{R}^4$, $\omega$, $\operatorname{Re}\omega$ and $\operatorname{Im}H$ are all equivalent. Each is an alternating real $2$-form of full rank $4$, and the linear symplectic group acts transitively on symplectic forms of a given rank on $\mathbb{R}^4$. So no invariant of the real form separates them; only the complex-linear symmetry group does, and that is the discriminator above.
- On $\mathbb{C}^2$ they are not proportional. $\omega$ is $\mathbb{C}$-bilinear of type $(2,0)$, $\operatorname{Im}H$ is real of type $(1,1)$; $\omega$ vanishes on every complex line and $\operatorname{Im}H$ does not; and the Lagrange identity of [The Three Canonical Forms on $\mathbb{C}^2$](../articles_maths/the-three-canonical-forms-on-c2.html) ties them together as $B^{2}+\omega^{2}=B(Q_1,Q_1)B(Q_2,Q_2)$ and $\omega\wedge\overline{\omega}=2\Omega^{2}$.
- On the algebra $\mathbb{B}$ the corpus does carry alternating forms. They are $\omega_{*}=\operatorname{Im}\langle\cdot,\cdot\rangle_{*}$ and $\omega_{\natural*}=\operatorname{Im}\langle\cdot,\cdot\rangle_{\natural*}$, defined in [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), §*The Alternating Forms on the Whole Space*, where they are nondegenerate of rank $8$ on a space of real dimension $8$, with isometry groups $Sp(8,\mathbb{R})$ and $U(4)$, $U(1,3)$ for the complex-linear ones. So the alternating object is not missing from the four-form inventory; it is the imaginary part of a Hermitian form, and the inventory lists scalar parts, which are symmetric by construction.

Why the $\mathbb{C}^2$ form is still a third object. $\omega$ lives on the spinor module of real dimension $4$, is $\mathbb{C}$-valued, and is preserved by $SL_2(\mathbb{C})$; the two forms of the algebra live on real dimension $8$, are $\mathbb{R}$-valued, and are preserved by the $*$-unitary groups. Rank and field separate them, so neither is a restriction of the other. What the three share is that each is *the* alternating form of its space, unique up to scale once the symmetry group is fixed.

## The Tensor Square and Why It Splits

The decomposition. The swap $\tau(Q_1\otimes Q_2)=Q_2\otimes Q_1$ is an involution of $\mathbb{C}^2\otimes\mathbb{C}^2$, so its eigenspaces give

$$
\mathbb{C}^2\otimes\mathbb{C}^2=\operatorname{sym}^{2}\mathbb{C}^2\oplus\Lambda^{2}\mathbb{C}^2\cong 3\oplus1 ,
$$

of complex dimension three and one. The corpus proves this from the swap alone, with no form and no choice.

What the one-dimensional summand is. $\Lambda^2\mathbb{C}^2$ is spanned by $e_1\wedge e_2$, and the pairing with $e_1\wedge e_2$ is the alternating form: $\omega(Q_1,Q_2)$ is the coefficient of $e_1\wedge e_2$ in $Q_1\wedge Q_2$. So the one-dimensional summand is the $\omega$-direction, and the splitting is the statement that a two-vector has a part proportional to the symplectic area and a part orthogonal to it.

Read as spins, it is the singlet. The antisymmetric summand is the spin-zero state of two spin-$\tfrac12$; the symmetric summand is the triplet. Read as two qubits, the antisymmetric summand contains the Bell state $\tfrac{1}{\sqrt2}(e_1\otimes e_2-e_2\otimes e_1)$, which is the singlet. The two readings are of one decomposition.

Read as a tensor product of forms, it is the determinant. The reason the antisymmetric summand is one-dimensional is that there is exactly one alternating form on $\mathbb{C}^2$ up to scale. The tensor square of that form is therefore the only bilinear pairing on the tensor square that is antisymmetric in each factor separately, which is the next section's identity.

## The Three Tensor Powers

The Hermitian power. $H^{\otimes n}$ is a Hermitian form on $(\mathbb{C}^2)^{\otimes n}$: conjugate-linear in the second slot, positive definite, of Gram matrix the identity in the product basis. It gives the inner product and the Born weights,

$$
\langleΞ_{\mathrm{wfn}}\rvert\tilde A\lvertΞ_{\mathrm{wfn}}\rangle=\bigl(H^{\otimes n}\bigr)(Ξ_{\mathrm{wfn}},\tilde AΞ_{\mathrm{wfn}}),
$$

for a Hermitian $\tilde A$. This is the metric of the $n$-qubit space and the reason the space is a Hilbert space and not only a vector space.

The bilinear power. $B^{\otimes n}$ is a complex bilinear symmetric form. At $n=2$ its quadratic form on a state with coefficient array $c$ is

$$
B^{\otimes2}(Ξ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}})=\sum_{i,j}c_{ij}^{2},
$$

because $B(e_i,e_j)=\delta_{ij}$. The four coefficients are the components of one element $\tilde Q$ of the algebra under the basis order $\lvert00\rangle\mapsto e_t$, $\lvert01\rangle\mapsto\vec e_x$, $\lvert10\rangle\mapsto\vec e_y$, $\lvert11\rangle\mapsto\vec e_z$ of [The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$](the-bell-basis-as-the-idempotent-basis-of-b-tensor-b.html), so the value is $\sum_{\imath} Q_{\imath}^{2}=N(\tilde Q)$, the quaternionic algebraic norm of [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), which is the corpus's interval form. It is complex-valued, of Gram matrix $\mathrm I_4$, of inertia $(4,0)$ on real amplitudes and $(4,4)$ over $\mathbb{R}$, and it vanishes on products of isotropic vectors. **This norm is not the concurrence**: its zero set is the zero-divisor cone, not the set of product states, and the section *The Norm and the Determinant Are Different* gives the two counterexamples that separate them.

The alternating power. $\omega^{\otimes n}$ is a complex bilinear form that is alternating in each slot separately. Its quadratic form is where the entanglement lives, and its behaviour depends on the parity of $n$ in a way that the next two sections make exact.

The three, side by side. Each form tensors, and each power answers one question about $n$ qubits. The table names the form, its power, the object the power produces, and the place in the corpus where that object is used.

| form | tensor power | what the power gives at $n$ factors | where the corpus uses it |
| --- | --- | --- | --- |
| $H$ | $H^{\otimes n}$ | the inner product, hence the Born weights | positivity, the Born rule |
| $B$ | $B^{\otimes n}$ | the biquaternion norm, hence the interval | the metric and the light cone |
| $\omega$ | $\omega^{\otimes n}$ | the antisymmetric pairing, hence the entanglement measures | the concurrence, the charge conjugation, the Bell basis |

**No fourth form is needed and none is available.** The space of invariant quadratic forms on $\mathbb{C}^4$ under the group that preserves all three is two-dimensional, which the section on groups makes precise.

## The Two-Qubit Identity

**The identity.** Let $Ξ_{\mathrm{wfn}}=\sum_{i,j}c_{ij}\,e_i\otimes e_j$ be a two-qubit state and $c$ its $2\times2$ coefficient array. Then

$$
\boxed{\;\omega\otimes\omega(Ξ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}})=\sum_{i,j,\imath,l}\omega_{ij}\,\omega_{\imath l}\,c_{i\imath}\,c_{jl}=2\bigl(c_{00}c_{11}-c_{01}c_{10}\bigr)=2\det c\;}
$$

Both sides are objects the corpus already had: on the left the alternating form of the one-qubit space, applied twice; on the right the determinant of the coefficient array of the pair. The box is a statement that the two are one number, not the introduction of a third.

The proof. The only nonzero entries of $\omega$ are $\omega_{01}=1$ and $\omega_{10}=-1$, in each index family. Expanding the four surviving terms,

$$
\omega\otimes\omega(Ξ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}})=c_{00}c_{11}-c_{01}c_{10}-c_{10}c_{01}+c_{11}c_{00}=2\bigl(c_{00}c_{11}-c_{01}c_{10}\bigr),
$$

and the last bracket is $\det c$.

The factor of two is the two orderings. The determinant of a $2\times2$ matrix is $\omega$ applied to its two rows: $\det c=\omega(r_0,r_1)$ with $r_0=(c_{00},c_{01})$ and $r_1=(c_{10},c_{11})$. The tensor square applies $\omega$ to both index families at once, so it counts the two orderings separately and doubles. The modulus is unaffected, and the modulus is the concurrence:

$$
C=2\lvert\det c\rvert=\bigl\lvert\omega\otimes\omega(Ξ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}})\bigr\rvert,\qquad \text{for a normalised state.}
$$

The check. The identity was verified on two hundred random normalised states, with zero failures, comparing $\omega\otimes\omega(Ξ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}})$ against $2\det c$ and the modulus against the Wootters concurrence. On the four Bell states the value is $\pm2$ in modulus before normalisation, that is $\pm1$ for the normalised concurrence.

The inertia, and why the Bell basis has two signs of each. In the Bell basis the symmetric matrix of $\omega\otimes\omega$ has eigenvalues $\pm1$ with multiplicity two each, so the form has inertia $(2,2)$: two positive and two negative directions. That is exactly the pattern [The Bell Basis](the-bell-basis-as-the-idempotent-basis-of-b-tensor-b.html) records, where $2D=b_1^{2}-b_2^{2}-b_3^{2}+b_4^{2}$ has two signs of each. The inertia is not an accident of the basis: it is computed from the eigenvalues of the matrix of the form, which are $\pm1$ with multiplicity two each.

What the identity says about the corpus's two forms. The two-qubit module carries two independent quadratic forms of the same degree, the norm $B^{\otimes2}$, of inertia $(4,0)$, and the concurrence form $\omega\otimes\omega$, of inertia $(2,2)$. They are the two independent invariants, and the second is the one that measures entanglement. So the corpus does not need a higher-degree replacement at two qubits; it needs to notice that it already had the second quadratic form, on the one-qubit space, and that tensoring it is the whole construction.

## The Norm and the Determinant Are Different

Two quadratic forms of one degree, and two different zero sets. On a normalised two-qubit state the two quantities are

$$
N(Ξ_{\mathrm{wfn}})=\sum_{i,j}c_{ij}^{2},\qquad D(Ξ_{\mathrm{wfn}})=\det c=c_{00}c_{11}-c_{01}c_{10},\qquad C=2\lvert D\rvert .
$$

$N$ is the quaternionic algebraic norm of the element $\tilde Q$ that the state vector names, and $D$ is the concurrence amplitude. They are both quadratic in the amplitudes and they are not multiples of one another, because they vanish on different sets. $N$ vanishes exactly on the zero divisors of the algebra: it is the reduced norm, $\det\mathsf M_2(\tilde Q)=N(\tilde Q)$, it is multiplicative, and its vanishing is the invertibility test of [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html). $D$ vanishes exactly on the product states, by the rank-one condition on $c$. Neither vanishing implies the other.

The two counterexamples, both checked. The product state $\lvert00\rangle$ has $c=\left(\begin{smallmatrix}1&0\\0&0\end{smallmatrix}\right)$, so $N=1$ and $D=0$: a product state of unit norm. The normalised state

$$
c=\tfrac12\begin{pmatrix}1&i\\ i&1\end{pmatrix}
$$

has $N=\tfrac14\bigl(1+i^{2}+i^{2}+1\bigr)=0$ and $D=\tfrac14\bigl(1-i^{2}\bigr)=\tfrac12$, so $C=1$: a maximally entangled state whose biquaternion norm vanishes. Its coefficient array is not rank one, since $\det c\neq0$, and the element it names is a zero divisor. Both computations were checked numerically on random normalised states and on these two.

**Why the abbreviation $C=2\lvert N\rvert$ is wrong.** It reads the vector-space identification $\mathbb{C}^4\cong\mathbb{B}$ of [The Bell Basis](the-bell-basis-as-the-idempotent-basis-of-b-tensor-b.html) as an algebra statement, and it is not one: the algebra product on $\mathbb{B}$ does not act as the two-qubit operator product on the state. $N$ is a function of the element alone and multiplies under the algebra product; $D$ is a function of the coefficient array and needs the tensor structure, which is why it is not the expectation of an algebra element. The two forms are independent, and the independence is the whole reason the concurrence can measure entanglement while the interval form cannot.

The one identity that does hold. $\det\mathsf M_2(\tilde Q)=N(\tilde Q)$ is the bridge from the algebra to the norm, and it is the identity of the four-forms article's multiplicative proposition. It relates $N$ to the *Pauli matrix image* of $\tilde Q$, not to the coefficient array $c$. Writing $\mathsf M_2$ for the two would give $\det c=N$ and the counterexamples above refute it.

## Which Group Preserves Which

The alternating form is preserved exactly by the unimodular group. For $g\in GL_2(\mathbb{C})$,

$$
g^{\mathsf T}\omega\,g=(\det g)\,\omega ,
$$

which is the two-dimensional instance of the transformation rule for an alternating form. So $\omega$ is invariant exactly when $\det g=1$, that is under $SL_2(\mathbb{C})$, and under no larger group.

The bilinear form is preserved by the orthogonal group. $g^{\mathsf T}\mathrm I\,g=g^{\mathsf T}g$, so $B$ is invariant exactly when $g^{\mathsf T}g=\mathrm I$, that is under $O(2,\mathbb{C})$, and under $SO(2,\mathbb{C})$ among the unimodular elements.

The Hermitian form is preserved by the unitary group. $H$ is invariant exactly when $g$ is unitary, that is under $U(2)$.

The consequence for the tensored forms. $\omega\otimes\omega$ is invariant under $SL_2(\mathbb{C})\times SL_2(\mathbb{C})$, which is the local-unitary group of two qubits up to the determinants. $B\otimes B$ is invariant under $SO(2,\mathbb{C})\times SO(2,\mathbb{C})$, which is much smaller. So the two forms are preserved by different groups, and neither is preserved by the other's group.

The false claim, and its correction. It is tempting to say that the symmetric square of the defining module contains exactly two trivial summands under $SL_2\times SL_2$, hence that the space of invariant quadratic forms on $\mathbb{C}^4$ is two-dimensional. The first half is false: under $SL_2(\mathbb{C})\times SL_2(\mathbb{C})$ the invariant quadratic forms on $\mathbb{C}^2\otimes\mathbb{C}^2$ are one-dimensional, spanned by $\omega\otimes\omega$, because $g^{\mathsf T}g\neq\mathrm I$ for a general unimodular $g$ and $B\otimes B$ is therefore not invariant. The computation of the dimension was done twice: the space of invariant quadratic forms is one-dimensional under $\mathfrak{sl}_2\oplus\mathfrak{sl}_2$ and two-dimensional under $\mathfrak{so}_2\oplus\mathfrak{so}_2$.

The correct statement. The two-qubit space carries two independent quadratic forms, $B\otimes B$ and $\omega\otimes\omega$. They are independent because $B$ and $\omega$ are not proportional — one is symmetric, the other alternating, and on a two-dimensional space that is already decisive. Each is invariant under its own group, and the two-dimensional invariance holds only under the smaller orthogonal product.

Why the correction matters for the physics. The concurrence is the modulus of the unique quadratic invariant under local unitary operations, which is why it is *the* two-qubit entanglement measure of degree two and not one of a pair. The norm is invariant only under a subgroup, which is why it is a property of the algebra and not of the entanglement. The two facts are one computation, and stating them with the wrong group would make the concurrence look accidental.

The scaling of the concurrence under local operations. For local operators with determinants $d_1,d_2$, the form $\omega\otimes\omega$ scales by $d_1d_2$. So the concurrence is invariant under $SL_2\times SL_2$ and scales by the product of the determinants otherwise. That is the exact statement of what "local unitary invariance" means for this measure, and it is the reason the normalisation by $\sum\lvert c\rvert^{2}$ is needed for states that are not normalised.

## The Parity Boundary

The parity rule. For a tensor product of matrices, $(A\otimes B)^{\mathsf T}=A^{\mathsf T}\otimes B^{\mathsf T}$, and $\omega^{\mathsf T}=-\omega$. Hence

$$
\boxed{\;\bigl(\omega^{\otimes n}\bigr)^{\mathsf T}=\bigl(-\omega\bigr)^{\otimes n}=(-1)^{n}\,\omega^{\otimes n}\;}
$$

The consequence at each $n$. At $n=1$ the form is alternating and vanishes on the diagonal identically: $\omega(Q,Q)=0$ for every $Q$. At $n=2$ it is symmetric and nontrivial, and its diagonal value is $2\det c$, which is the concurrence. At $n=3$ it is alternating again, so

$$
\omega^{\otimes3}(Ξ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}})=0\quad\text{for every }Ξ_{\mathrm{wfn}}\in(\mathbb{C}^2)^{\otimes3}.
$$

At $n=4$ it is symmetric again and nontrivial.

The check at $n=3$. The identity was verified on fifty random three-fold product states and on the two standard entangled states. On the GHZ state and on the $W$ state the value is zero, to machine precision, and on every random product state it is zero as well.

Why this is the right explanation of a familiar fact. The three-qubit measures that exist are quartic: the three-tangle is a degree-four expression in the amplitudes, and Cayley's hyperdeterminant is quartic in the eight coefficients. A reader who has met them may have been told that quadratic invariants "do not suffice" at three qubits. The parity rule says why: **the only quadratic invariant that the canonical forms can produce at three factors is identically zero.** The vanishing is not a failure of inventiveness; it is a theorem about alternating forms.

The general form of the statement. If $F$ is a bilinear form of homogeneity $\sigma\in\{\pm1\}$ in the sense that $F^{\mathsf T}=\sigma F$, then $F^{\otimes n}$ has homogeneity $\sigma^{n}$. The diagonal evaluation of an alternating form is zero. So quadratic invariants from a single canonical form exist only when $\sigma^{n}=+1$, that is when either the form is symmetric and $n$ is anything, or the form is alternating and $n$ is even.

**What the parity rule does not say.** It does not say that no quadratic invariant exists at three qubits; the norm $B^{\otimes3}$ is one, and it is nontrivial. It says that the *entanglement* invariant of degree two does not exist, because the entanglement invariant is the alternating one and its third power vanishes.

## Charge Conjugation as the Same Pairing

The corpus's charge conjugation. On the module the corpus defines

$$
\mathcal{C}[\tilde\Xi]=-\vec e_y\,\tilde\Xi^{*}\,\vec e_y ,
$$

an antilinear involution, $\mathcal{C}^{2}=1$, whose fixed space is the Majorana space of real dimension four. In the Pauli model its matrix on the coefficient column is the alternating matrix composed with conjugation, up to a phase: $\mathcal{C}$ is $\omega$ followed by complex conjugation.

**Two antilinear maps compose to a bilinear one.** $\mathcal{C}$ alone does not descend to a bilinear pairing, for the reason given in [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html): an antilinear map reverses the central scalar. But the tensor square $\mathcal{C}\otimes\mathcal{C}$ is bilinear, and it is available on the two-qubit space. Its diagonal pairing is

$$
\bigl\lvert\langleΞ_{\mathrm{wfn}}\rvert\,\mathcal{C}\otimes\mathcal{C}\,\lvertΞ_{\mathrm{wfn}}^{*}\rangle\bigr\rvert=2\bigl\lvert c_{00}c_{11}-c_{01}c_{10}\bigr\rvert=2\lvert\det c\rvert ,
$$

verified against the determinant on random states.

The corpus half-says this already. [The Native Qubit and the Defining Module of the Biquaternion Algebra](the-native-qubit-and-the-defining-module-of-the-biquaternion-algebra.html) remarks that the concurrence carries no separate glyph because $\mathcal{C}$ is already the name of charge conjugation. That remark is not a notational convenience. The concurrence *is* the charge-conjugation pairing of the two-spinor space, and the same pairing is what separates the Dirac from the Majorana mass in [Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form](antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html), where the Dirac mass is linear and pairs no field with its conjugate and the Majorana mass is antilinear and pairs a field with its own.

One bilinear form, three readings. As a mass pairing it decides whether a fermion can carry a Majorana term. As a spin flip it is the operation that reverses both spins. As an entanglement measure it is the concurrence. The three readings are of $\omega$, and the reason they coincide is that all three are statements about the antisymmetric two-form of a two-dimensional complex space.

The consequence for the naming. The corpus's avoidance of a new symbol for the concurrence is vindicated in a stronger sense than the article that made it intended: the object is the same object, and a new symbol would have hidden that.

## Bilinearity as the Criterion

The rule. A bilinear form passes through a tensor product untouched: $F\otimes F$ is defined, its diagonal evaluation is a quadratic function of the joint state, and its invariance group is the product of the groups. An antilinear involution does not: it reverses the central scalar, and a tensor product that identifies the scalars of the factors has no room for a map that distinguishes them.

The two halves of the group of articles are one half. In this category, [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html) proves that the sector split does not descend; that is the antilinear half. This article proves that the alternating form does; that is the bilinear half. The criterion that decides both is the same property, and it is worth stating as a single sentence: **bilinearity is what survives composition, and antilinearity is what does not.**

The consequence that is easy to miss. The reason there is no per-subsystem sector label is the same reason there is a concurrence. If the split had descended, the two-qubit algebra would have had four labelled sectors and the alternating form would have been one more structure among many. Because it does not descend, the algebra has two spaces, and the alternating form is the only degree-two invariant that the local group preserves. The loss and the gain are the same fact.

Why the criterion is not circular. It would be circular to say that bilinear forms survive because they are bilinear. The content is that the obstruction is *exactly* antilinearity and nothing else: the total star, which is antilinear, does descend, because its two sign changes cancel. So the criterion is finer than "linear versus antilinear" — it is whether the map respects the relation that the quotient imposes, and for a tensor product of forms the answer is decided by whether the form needs a conjugation at each slot.

## The Peirce Route Does Not Give a Second Qubit

The tempting reading. A Peirce decomposition of $\mathbb{B}$ exhibits two minimal left ideals, each isomorphic to $S=\mathbb{C}^2$, and the regular module splits as $\mathbb{B}\cong S\oplus S$. Since $S$ is the duo-complex space and the spinor module, one might conclude that the two ideals are two qubits, and that the algebra already contains a pair.

**Why it is wrong.** The two ideals are the same qubit twice. The regular module of a $2\times2$ matrix algebra is the direct sum of two copies of its simple module, and the multiplicity two is the length of the algebra as a module over itself. It is bookkeeping about the algebra, not a physical doubling: the two summands are isomorphic, no observable distinguishes them, and the corpus's own article on the polarized module calls the pair a copy index and not a chirality.

The consequence for this article. The bridge is not built on the Peirce decomposition. It is built on the tensor product: two qubits are $S\otimes S$, which is $\mathbb{C}^4$ and not $\mathbb{C}^2\oplus\mathbb{C}^2$. The two spaces have the same dimension over $\mathbb{C}$, and they are not the same object: $\mathbb{C}^2\oplus\mathbb{C}^2$ carries two copies of the three forms and no cross terms, while $\mathbb{C}^4$ carries the tensor products and all the cross terms. The concurrence lives in the cross terms.

The third statement of one fact. The corpus now says the same thing three ways. In the dimension count, four parameters cannot hold fifteen. In the non-descent, the partial star does not pass to the quotient. In the module theory, the regular module's doubling is multiplicity. All three say that the algebra does not contain a second qubit, and all three are needed, because each is convincing to a different reader.

## The Conjugation Trap

Two maps that look alike. On $\mathbb{B}$ there are two antilinear involutions that a reader may take for one another.

- Coefficient conjugation $\sigma$, the corpus's $\mathrm{conj}\otimes\mathrm{id}$: it sends $i\mapsto-i$ and fixes every quaternion unit. In the Pauli model $e_t=\mathrm I$ and $\vec e_{\imath}=i\sigma_{\imath}$, so $\sigma$ flips the sign of the coefficient of each $\vec e_{\imath}$ and leaves the coefficient of $e_t$ alone.
- Entrywise conjugation $\kappa$: it sends every matrix entry to its complex conjugate. In the Pauli model it flips both $i$ and $\sigma_{\imath}$, hence it fixes each $\vec e_{\imath}=i\sigma_{\imath}$ as a matrix and only conjugates the coefficients differently.

They act differently on the projective line. On the lattice of minimal left ideals, parametrised by the kernel line $[\zeta]$ with chart $z=\zeta_1/\zeta_2$:

- $\sigma$ acts as $z\mapsto-1/\bar z$, an antiholomorphic involution. It has no fixed point, because $z=-1/\bar z$ gives $\lvert z\rvert^{2}=-1$; and on the real circle $z=t\in\mathbb{R}$ it acts as $t\mapsto-1/t$, the antipodal map. **So no minimal left ideal is stable under coefficient conjugation**, which is exactly what the corpus states.
- $\kappa$ acts as $z\mapsto\bar z$, whose fixed set is the real circle. So every ideal with a real kernel line is fixed.

**The error this produced, recorded because it is instructive.** Reading a matrix display, one takes the obvious conjugation to be $\kappa$, and then one concludes that the corpus is wrong when it says no ideal is stable. That conclusion is false. The corpus is right, and the trap is the display's: the map that flips the sign of the imaginary unit of the algebra is not the map that conjugates the entries of its matrix.

Why the two maps are not inner-equivalent. Both are homomorphisms, verified on random products; both are involutions. They differ because the algebra has a real form that does not commute with entrywise conjugation: $\sigma$ is the conjugation that respects the decomposition into quaternion and central parts, and $\kappa$ is the one that respects the Pauli display. Only the first is an automorphism of the biquaternion algebra as presented.

The lesson for this article. Any statement about how the forms behave under conjugation must say which conjugation. $H$ uses the conjugate slot; $\sigma$ is the conjugation that fixes the units; $\kappa$ is a different map with a different fixed set. Three names, three objects.

## What This Article Does and Does Not Claim

It does claim that the concurrence is the modulus of the tensor square of the alternating form evaluated on the state, so that the one-qubit canonical form produces the two-qubit measure; that the parity rule explains why the three-qubit measures are quartic; that the two-qubit space carries exactly two independent quadratic forms, of inertia $(4,0)$ and $(2,2)$, invariant under different groups; that the corpus's charge conjugation is the same pairing as the concurrence; and that bilinearity is the criterion that decides both what composes and what measures.

It does not claim that a new invariant has been found. Every object here is in the corpus: the three forms, the $3\oplus1$ splitting, the concurrence, the charge conjugation. What is new is the composition, and the correction of one invariance claim.

It does not claim that the duo-complex numbers are two qubits. They are one qubit, and the tensor square of the space is two.

It does not claim that $H^{\otimes n}$ is a bilinear form. It is Hermitian, it needs a conjugate slot, and its tensor powers give the Born weights rather than the invariants.

It does not claim that the concurrence is the biquaternion norm, nor that $C=2\lvert N\rvert$. The norm $N=\sum_{ij}c_{ij}^{2}$ and the concurrence amplitude $D=\det c$ vanish on different sets: $\lvert00\rangle$ has $N=1$ and $C=0$, and $\tfrac12\left(\begin{smallmatrix}1&i\\ i&1\end{smallmatrix}\right)$ has $N=0$ and $C=1$. The norm is the zero-divisor test; the determinant is the product-state test.

It does not claim that the parity rule exhausts the invariant theory at odd $n$. It says that the alternating route gives nothing there, which is one statement and not a classification.

## Summary

The duo-complex space $\mathbb{C}^2$ carries three canonical forms: the Hermitian $H$, the symmetric bilinear $B$ and the alternating $\omega$, with Gram matrices $\mathrm I$, $\mathrm I$ and $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$. The first two share a Gram matrix because the basis is real, and differ on $Q=(1,i)$, where $H(Q,Q)=2$ and $B(Q,Q)=0$. Each tensors, and the three tensor powers are the three structures of the $n$-qubit theory: $H^{\otimes n}$ the Born weights, $B^{\otimes n}$ the biquaternion norm and interval, $\omega^{\otimes n}$ the entanglement pairing. At $n=2$, $\omega\otimes\omega(Ξ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}})=2(c_{00}c_{11}-c_{01}c_{10})=2\det c$, so $2\lvert\det c\rvert$ is the concurrence, with inertia $(2,2)$ matching the Bell-basis diagonalisation; and this is the $n=2$ formula, not a general one. The other quadratic form of the pair is the norm, $B^{\otimes2}(Ξ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}})=\sum_{ij}c_{ij}^{2}=N(\tilde Q)$, the quaternionic algebraic norm in the basis order of the Bell article; it vanishes on the zero divisors and not on the product states, so the concurrence is not twice its modulus, and $\lvert00\rangle$ with $N=1$, $C=0$ against $\tfrac12(1,i;i,1)$ with $N=0$, $C=1$ is the pair that shows it. $\omega\otimes\omega$ is invariant under $SL_2\times SL_2$ and $B\otimes B$ under $SO_2\times SO_2$, so they are independent forms invariant under different groups and not a two-dimensional space of local-unitary invariants. The parity rule $(\omega^{\otimes n})^{\mathsf T}=(-1)^{n}\omega^{\otimes n}$ makes $\omega^{\otimes3}$ alternating, hence identically zero on the diagonal, which is why no degree-two entanglement invariant exists at three qubits and the three-qubit measures are quartic. The corpus's charge conjugation $\mathcal{C}$ is $\omega$ composed with conjugation, and $\mathcal{C}\otimes\mathcal{C}$ is the bilinear pairing whose modulus is the concurrence: mass pairing, spin flip and entanglement measure are one form. Bilinearity is the criterion that survives composition; antilinearity is what does not, and the same property that produces the concurrence destroys the per-subsystem label.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbb{C}^2$, $Q=(Q_\blacktriangle,Q_\blacktriangledown)$ | the duo-complex space and a duo-complex number |
| $H$ | the Hermitian form; Gram matrix $\mathrm I$; inertia $(4,0)$ over $\mathbb{R}$ |
| $B$ | the symmetric complex bilinear form on $\mathbb{C}^2$; Gram matrix $\mathrm I$; isotropic cone of two lines. Not the vector modulus $B$ of the algebra, not $\mathbb{B}$ |
| $\omega_*=\operatorname{Im}\langle\cdot,\cdot\rangle_*$, $\omega_{\natural*}$ | the alternating forms on $\mathbb{B}$, rank $8$; the algebra-level analogue of $\omega$, distinct from it by field and rank |
| $\omega$ | the alternating form; Gram matrix $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$; $g^{\mathsf T}\omega g=(\det g)\omega$ |
| $\operatorname{sym}^2\oplus\Lambda^2\cong3\oplus1$ | the swap splitting of the tensor square |
| $H^{\otimes n}$, $B^{\otimes n}$, $\omega^{\otimes n}$ | the three tensor powers: weights, norm, entanglement |
| $2\det c=\omega\otimes\omega(Ξ_{\mathrm{wfn}},Ξ_{\mathrm{wfn}})$ | the concurrence identity: the tensor square of $\omega$ is twice the determinant; $C=2\lvert\det c\rvert$ |
| $N(\tilde Q)=\sum_{\imath} Q_{\imath}^{2}$ | the quaternionic algebraic norm; $N(Ξ_{\mathrm{wfn}})=\sum_{ij}c_{ij}^{2}$ in the basis order; zero exactly on the zero divisors; not $C/2$ |
| $(2,2)$ | the inertia of the concurrence form on real amplitudes |
| $(-1)^{n}\omega^{\otimes n}$ | the parity rule: $\omega^{\otimes n}$ is symmetric at even $n$ and alternating at odd $n$ |
| $\mathcal{C}[\tilde\Xi]=-\vec e_y\tilde\Xi^{*}\vec e_y$ | charge conjugation on the module, $\omega$ composed with conjugation |
| $\sigma$, $\kappa$ | coefficient conjugation and entrywise conjugation; $z\mapsto-1/\bar z$ against $z\mapsto\bar z$ |

## Further Reading

In the mathematics corpus. [The Three Canonical Forms on $\mathbb{C}^2$](../articles_maths/the-three-canonical-forms-on-c2.html) defines $H$, $B$ and $\omega$ and proves them not proportional. [The Tensor Square of $\mathbb{C}^2$](../articles_maths/the-tensor-square-of-c2.html) proves the $3\oplus1$ splitting from the swap. [The Realification of $\mathbb{C}^2$](../articles_maths/the-realification-of-c2.html) gives the real and imaginary parts of $H$ and the symplectic structure of the real four-space. [Duo-Complex Numbers](../articles_maths/duo-complex-numbers.html) is the space and its two scalar structures. [The Category of Modules in the Biquaternion Algebra](../articles_maths/the-category-of-modules-in-the-biquaternion-algebra.html) proves that the regular module is $S\oplus S$ and that the doubling is multiplicity. [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html) carries the alternating forms of the algebra, $\omega_*$ and $\omega_{\natural*}$, the analogue of $\omega$ one dimension up. [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) is the inventory of the four forms and the four norms, and the source of $N$.

In this category. [The Multi-Qubit Split, I](the-multi-qubit-split-i-the-antilinear-obstruction-and-the-corner-collapse.html) is the antilinear half of the criterion. [The Multi-Qubit Split, II](the-multi-qubit-split-ii-the-sign-condition-the-concurrence-form-and-the-central-bit.html) computes the concurrence form and proves it is not an expectation. [The Bell Basis as the Idempotent Basis of $\mathbb{B}\otimes\mathbb{B}$](the-bell-basis-as-the-idempotent-basis-of-b-tensor-b.html) gives the coefficient array and the Bell diagonalisation. [Multi-Partite Entanglement: GHZ, W and the Three-Qubit Classification](multi-partite-entanglement-ghz-w-and-the-three-qubit-classification.html) uses the parity boundary at $n=3$. [Entanglement Monogamy and the CKW Inequality](entanglement-monogamy-and-the-ckw-inequality.html) uses the three pairings on the three bipartitions.
