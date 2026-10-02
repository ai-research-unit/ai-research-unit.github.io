
# __Positive Definite Forms and the Order__

## Introduction

A **positive definite form** on an ordered involutive algebra is the Hermitian form attached to a positive functional,

$$
\langle a,b\rangle_\varphi = \varphi(b^{*}a) ,
$$

which is positive semidefinite by the definition of $\varphi$, and positive definite after the quotient by the radical $\{a : \langle a,a\rangle_\varphi = 0\}$; the construction that turns it into a Hilbert space and a representation is the **Gelfand–Naimark–Segal** construction. The forms are not a side structure: they **are** the order. A Hermitian element is positive if and only if every positive definite form takes a nonnegative value on it,

$$
a\geq0 \iff \varphi(a)\geq0 \ \text{ for every positive functional } \varphi ,
$$

so the positive cone is the intersection of the half-spaces cut by the forms, and the order of the algebra is completely determined by the convex set of its positive definite forms. The article states this duality, shows that the forms organise into the dual cone, and describes the three equivalent ways of presenting the order — by the cone of the algebra, by its positive functionals, and by the representations on Hilbert space — together with the order-preserving correspondences among them.

The forms are the inner products in which the order becomes geometric: the **Cauchy–Schwarz** inequality of a form is the inequality of the positive functional, the **radical** of a form is the left ideal of the GNS construction, and the **order** of the algebra is the order of the operators in every associated representation. The article is thus the form-theoretic companion of *The Cone of Positive Functionals*, and it prepares the **Hilbert cone** of an involutive algebra, which is the same cone for the algebra that carries a form intrinsically.

The positive cone and the positive functionals are *The Positive Cone of an Involutive Algebra* and *The Cone of Positive Functionals*; the Hermitian elements and the order unit are *Hermitian Elements and the Order Unit*; the order and the order unit are *Ordered Vector Spaces and the Order Unit*; the ordered involutive algebra is *Ordered Involutive Algebras*; the Hilbert cone is *The Hilbert Cone of an Involutive Algebra*; the Jordan order is *The Jordan Algebra of Self-Adjoint Elements*; the forms on an ordered space are *Positive Definite Forms on an Ordered Space*; and the GNS representation and the Hilbert algebras are *Hilbert Algebras* and *Operator Algebras* of Part II.

## Positive Definite Forms

**Definition.** A **positive definite form** (or a **semidefinite form**) on the involutive algebra is a Hermitian form $\langle\cdot,\cdot\rangle : A\times A\to\mathbb{C}$ with

$$
\langle a,a\rangle\geq0 \ \text{ for every } a , \qquad \langle a,b\rangle = \overline{\langle b,a\rangle} , \qquad \langle \alpha a + \beta b, c\rangle = \alpha\langle a,c\rangle + \beta\langle b,c\rangle ;
$$

it is **definite** when $\langle a,a\rangle = 0$ implies $a = 0$, and its **radical** is the subspace $N = \{a : \langle a,a\rangle = 0\}$.

**Proposition (the forms are the positive functionals).** A positive definite form is of the form $\langle a,b\rangle = \varphi(b^{*}a)$ for a unique positive functional $\varphi$ when it is **invariant**, $\langle ca,b\rangle = \langle a,c^{*}b\rangle$, that is, when it is compatible with the multiplication; without the invariance it is the general positive semidefinite Hermitian form on the underlying vector space. The invariant forms are exactly the positive functionals, and the map $\varphi\mapsto\langle\cdot,\cdot\rangle_\varphi$ is a linear isomorphism of the dual cone onto the cone of the invariant positive definite forms.

*Proof.* For a positive functional $\varphi$ the form $\langle a,b\rangle = \varphi(b^{*}a)$ is Hermitian by the Hermitian-ness of $\varphi$, positive by the definition, and invariant because $\langle ca,b\rangle = \varphi(b^{*}ca) = \varphi((c^{*}b)^{*}a) = \langle a,c^{*}b\rangle$. Conversely an invariant positive definite form gives the functional $\varphi(x) = \langle 1,x\rangle$, which is linear and positive because $\varphi(x^{*}x) = \langle 1,x^{*}x\rangle = \langle x,x\rangle\geq0$ by the invariance, and which recovers the form because $\langle a,b\rangle = \varphi(b^{*}a)$ by the invariance and the Hermitian symmetry. The correspondence is linear and preserves the cones in both directions.

**Proposition (Cauchy–Schwarz and the radical).** Every positive definite form satisfies

$$
\lvert\langle a,b\rangle\rvert^{2}\leq\langle a,a\rangle\langle b,b\rangle ,
$$

its radical $N$ is a subspace on which the form vanishes, the quotient $A/N$ carries a definite form, and the completion of the quotient is a Hilbert space $\mathcal{H}_\varphi$.

*Proof.* The Cauchy–Schwarz inequality is that of the positive functional; the radical is a subspace by the inequality (the equality case of the Cauchy–Schwarz inequality); the quotient form is definite by construction, and the completion is a Hilbert space.

## The Order from the Forms

**Theorem (the order is the intersection of the forms).** For Hermitian $h$,

$$
h\geq0 \iff \langle h\, a, a\rangle_\varphi\geq0 \ \text{ for every } a \text{ and every positive functional } \varphi \iff \varphi(h)\geq0 \ \text{ for every positive functional } \varphi ,
$$

equivalently $h$ is positive exactly when it is a positive operator in every representation associated with a positive definite form; hence the order of the Hermitian part is recovered from the cone of the forms, and the cone is the intersection of the half-spaces cut by the positive functionals.

*Proof.* If $h\geq0$ the invariance gives $\varphi(a^{*}ha)\geq0$ because $a^{*}ha$ is a congruence of a positive element; conversely, if $h$ is not positive then by the Hahn–Banach theorem some positive functional is negative at $h$, as in the separation theorem of *The Cone of Positive Functionals*. The representation statement is the GNS construction applied to the form, in which the order is the operator order.

**Corollary (the order is an order of representations).** The order-theoretic structure of the involutive algebra is the same as the order-theoretic structure of its **universal representation**: the direct sum of the GNS representations over all the positive functionals is faithful, and $h\geq0$ if and only if the image of $h$ is a positive operator in it. Consequently every order statement has a concrete operator form.

*Proof.* The universal representation is the direct sum of the GNS representations, and it is faithful because the positive functionals separate the Hermitian elements; the positivity of $h$ in the universal representation is the positivity in every GNS representation, which is the theorem above.

**Proposition (the order unit and the forms).** In a unital reduced algebra the identity is positive, every state takes the value $1$ at it, and the order-unit norm is the norm in the universal representation; the positive definite forms with $\varphi(1) = 1$ are the **states**, and the order interval $[-1,1]$ is the set of the Hermitian elements that are contractions in every associated form.

*Proof.* The positivity of $1$ and the normalisation of the states are the definitions; the norm statement is the coincidence of the order-unit norm with the $\ast$-norm in the universal representation; the interval statement is the definition of the order unit.

## Worked Cases

### The Matrix Algebra

Let $A = M_n(\mathbb{C})$ with the trace form $\langle a,b\rangle = \operatorname{tr}(b^{*}a)$, which is definite and invariant. The order is the Loewner order, the positive definite forms are the maps $a\mapsto\operatorname{tr}(\rho a)$ for positive semidefinite $\rho$, and the GNS construction with a rank-one $\rho$ gives the natural module $\mathbb{C}^{n}$; the order is the operator order in that representation, and the universal representation is the direct sum over all the density matrices. This is the finite-dimensional model in which every statement of the article is a matrix identity.

### The Continuous Functions

Let $A = C(X,\mathbb{C})$ with the form $\langle a,b\rangle = \int b^{*}a\,\mathrm{d}\mu$ for a positive measure $\mu$. The form is invariant, the order is the pointwise order, and a function is positive exactly when it is nonnegative on the support of every positive measure; the GNS construction gives the representation of $A$ on $L^{2}(\mu)$, in which the order is again the operator order. The commutative case shows that the forms and the order carry the same information as the measure-theoretic positivity.

## Summary

A **positive definite form** on an involutive algebra is a positive semidefinite Hermitian form; it is **invariant** when it is compatible with the multiplication, and then it is exactly $\langle a,b\rangle = \varphi(b^{*}a)$ for a unique **positive functional** $\varphi$, so the invariant forms are the positive functionals and the map is a linear isomorphism on the cones. Every form satisfies the **Cauchy–Schwarz inequality**, its **radical** is a subspace and the completion of the quotient is the Hilbert space of the **GNS** construction. The **order** is the intersection of the forms: a Hermitian element is positive if and only if every positive functional takes a nonnegative value on it, equivalently if and only if it is a positive operator in every GNS representation; hence the order is recovered from the cone of the forms and coincides with the operator order in the **universal representation**. In the unital reduced algebra the identity is positive, the states are the forms with $\varphi(1) = 1$, the order-unit norm is the norm of the universal representation, and the order interval $[-1,1]$ is the set of the Hermitian contractions. The positive cone and functionals are *The Positive Cone of an Involutive Algebra* and *The Cone of Positive Functionals*; the Hermitian elements are *Hermitian Elements and the Order Unit*; the order is *Ordered Vector Spaces and the Order Unit*; the ordered involution is *Ordered Involutive Algebras*; the Hilbert cone is *The Hilbert Cone of an Involutive Algebra*; the Jordan order is *The Jordan Algebra of Self-Adjoint Elements*; the forms on an ordered space are *Positive Definite Forms on an Ordered Space*; and the GNS theory is *Hilbert Algebras* and *Operator Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle a,b\rangle = \varphi(b^{*}a)$ | Positive definite form attached to $\varphi$ |
| $\langle ca,b\rangle = \langle a,c^{*}b\rangle$ | Invariance; the invariant forms are the positive functionals |
| $\lvert\langle a,b\rangle\rvert^{2}\leq\langle a,a\rangle\langle b,b\rangle$ | Cauchy–Schwarz inequality |
| $N = \{a : \langle a,a\rangle = 0\}$ | Radical of the form |
| $h\geq0\iff\varphi(h)\geq0$ | The order is the intersection of the forms |
| $\mathcal{H}_\varphi$ | Hilbert space of the GNS construction |
| $\varphi(1) = 1$ | The state forms |

## Further Reading

- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the GNS construction, the positive forms and the universal representation.
- Gert K. Pedersen, *C\*-Algebras and their Automorphism Groups* (Academic Press, 1979), for the positive definite forms and the order of a C*-algebra.
- Jacques Dixmier, *Les algèbres d'opérateurs dans l'espace hilbertien* (Gauthier-Villars, 1969), for the forms, the states and the universal representation of a von Neumann algebra.
- Shoichiro Sakai, *C\*-Algebras and W\*-Algebras* (Springer, 1971), for the positive forms, the order and the representation theory.
- Charalambos D. Aliprantis and Owen Burkinshaw, *Positive Operators* (Academic Press, 1985), for the positive forms and the order of an ordered vector space.
