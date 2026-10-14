# __The Operators of the Symmetric Quaternionic Product and the Coupling__

## Introduction

This article is the operator article of the symmetric quaternionic algebra, the band of *The Quaternion Form
as a Product: the Scalar Coupling of Two Material Operations* and *Why a Central Product Cannot Compose: the
Radical and the Isotropic Elements*, and it is the $\mathrm{SQA}$ row of the twelve operator rows. Its product
is the **symmetrised quaternionic product**

$$
\tilde P\bullet\tilde Q=\tfrac12\bigl(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P\bigr)
=\bigl[P_0Q_0+(\vec P,\vec Q)\bigr]e_0=N(\tilde P,\tilde Q)\,e_0 ,
$$

and the operators of the band attach an element to an argument:

$$
L^{\bullet}_{\tilde Q}(\tilde R)=\tilde Q\bullet\tilde R,\qquad
R^{\bullet}_{\tilde P}(\tilde R)=\tilde R\bullet\tilde P .
$$

The product is commutative, so the two operators **coincide**, $L^{\bullet}_{\tilde A}=R^{\bullet}_{\tilde A}$:
the band carries **one** family and not two. The element theory of the block, the coupling interpretation and the
radical are the two sibling articles' business; this article adds the operator layer only, and every fact of the
layer is owned by a mathematics article and cited in place.

The answer is one sentence. The form of the block is the **quaternion form**
$N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\vec P,\vec Q)$, of Gram matrix
the identity, symmetric and non-degenerate; its associate is the transpose, and the transpose of a multiplication
is **not** a multiplication: $(L^{\bullet}_{\tilde A})^{\approx}(\tilde Y)=Y_0\tilde A$. Association therefore carries
the parameter **out of the multiplier slot and into the argument's scalar slot**; it **keeps the side**, there
being only one, and it **conjugates nothing**, the quaternion form carrying no conjugation. The multiplication is
its own associate exactly at the **central** parameters, and the self-adjoint multiplications are the central
ones, the only skew-adjoint one being zero; inside the family no non-zero operator preserves the form and none is
multiplicative; the form-preserving operators are the two-sided complex-orthogonal maps, of complex dimension
six, and the product-preserving ones their subgroup fixing $e_0$, of complex dimension three, both outside the
rank-one family; and the two-sided operators are rank one and never invertible, so the group of invertible
two-sided operators — the home of the spin group — has no instance in the band. The contrast with the general
quaternionic row, whose two families are distinct and whose left family is the opposite monoid
$\mathbb{B}^{\mathrm{opp}}$, and with the ordinary row, whose association swaps the two sides, is the spine of the
article.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis
$e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, and central scalar imaginary $i$ with $i^{2}=-1$. An element
is $\tilde Q=Q_0e_0+\vec Q$; the natural conjugation is ${}^{\natural}$, the Hermitian star
${}^{*}=\bar{\cdot}\circ{}^{\natural}$, and the sectors are $\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$,
the material one $\mathbb{M}_-$. The general plain bilinear product is juxtaposition $\tilde P\tilde Q$, the quaternionic
product is $\tilde P\star\tilde Q=\tilde P^{\natural}\tilde Q$, and the **general quaternionic bilinear form** is
$N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)$, which is also the coefficient of this block; the
**general plain bilinear form** is $B(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P\tilde Q)=P_0Q_0-(\vec P,\vec Q)$,
differing from $N$ by the sign of the vector part alone. The symbol $\bullet$ is **row-relative** in this
chapter: the plain row writes it for $\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ and this block for
$\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$, a different operation; the mathematics
articles of the block write this same product $\star$ and its operator $L^{\star}$, the two notations being the
same object. The generic trace is
$T(\tilde Q)=2Q_0$ and the algebraic norm of the form is $N(\tilde Q,\tilde Q)=\sum_\mu Q_\mu^{2}$. The operator theory
is owned by four mathematics articles and is cited in place: *The Multiplication Operators of the Symmetric
Quaternionic Algebra* for the one family, its rank, its composition, its adjoint and its derivations; *The
Quaternion Form as a Product on the Symmetric Quaternionic Algebra* for the form, its Gram matrix, its
realification and its failure of invariance; *The Specificities of the Symmetric Quaternionic Algebra* for the
classification of the operators by the scalar coordinate and for the scalar law; and *The Left Multiplications of
the Quaternionic Product and the Opposite Monoid* with *The Two-Sided Operators and the Spin Group* for the parent
row and for the group of invertible two-sided operators. The crossing reader *The Operators of the Twelve
Structures: Multiplication, Adjoint and Bracket* compares the twelve and is not one of them.

## The One Family of Multiplications and Its Composition

**Definition.** The **left** and the **right multiplication operators** of the band by an element $\tilde A$ are
$L^{\bullet}_{\tilde A}(\tilde R)=\tilde A\bullet\tilde R$ and $R^{\bullet}_{\tilde A}(\tilde R)=\tilde R\bullet\tilde A$,
both $\mathbb{C}$-linear; $L_{\tilde A}$ and $R_{\tilde A}$ denote throughout the left and right multiplication
operators of the **plain** product.

**Theorem (the two families coincide).** For every $\tilde A$,

$$
L^{\bullet}_{\tilde A}=R^{\bullet}_{\tilde A},
$$

so the band carries one family and not two, and the contrast with the general quaternionic row, whose two families
are distinct and whose left family is the opposite monoid $\mathbb{B}^{\mathrm{opp}}$, is the whole operator content of
the job word **coupling**.

*Proof.* $\tilde A\bullet\tilde R=\tilde R\bullet\tilde A$ by the commutativity of the product. Commutativity is
*Introduction to the Symmetric Quaternionic Algebra of Biquaternions*; the collapse of the two families is *The
Multiplication Operators of the Symmetric Quaternionic Algebra*.

**Read as a physical statement.** The comparison of two material operations has no orientation: attaching an
operation on the left and attaching it on the right are one act, so the operator carries no side. The interpretation is
that the coupling is **order-free at the level of the operator as well as at the level of the value**; the order
the parent row carries leaves no residue in the one-sided operators.

**Theorem (the shape of the operator).** For all $\tilde A,\tilde R$,

$$
L^{\bullet}_{\tilde A}(\tilde R)=N(\tilde A,\tilde R)\,e_0 .
$$

For $\tilde A\neq0$ the operator has image the central line $\mathbb{C}e_0$, kernel the hyperplane
$N(\tilde A,\cdot)=0$ of complex dimension three, rank one, trace $\operatorname{Tr}(L^{\bullet}_{\tilde A})=A_0$
and determinant zero; it is zero exactly at $\tilde A=0$, and $\tilde A\mapsto L^{\bullet}_{\tilde A}$ is
injective.

*Proof.* The display is the governing formula of the product read as an operator identity; the form is
non-degenerate, so the functional is non-zero and its kernel a hyperplane; the trace, the determinant and the rank
are read on the matrix in the basis, whose first row is the coordinates of $\tilde A$ and whose other rows vanish.
*The Multiplication Operators of the Symmetric Quaternionic Algebra*, §*The Operators, Their Matrices and Their Ranks*, and *The
Specificities of the Symmetric Quaternionic Algebra*, §*The Left Multiplication Is Rank One*.

**Read as a physical statement.** The operator of a coupling is as small as a non-zero operator can be: a single
functional on the algebra, read with the fixed value $e_0$. Its kernel is the hyperplane of operations the
coupling does not see, and its rank-one image is the interpretation that the coupling returns **a number and not a
direction**; the faithfulness is the interpretation that the operator loses nothing of the parameter.

**Theorem (the composition law).** For all $\tilde A,\tilde B$,

$$
L^{\bullet}_{\tilde A}\circ L^{\bullet}_{\tilde B}
=L^{\bullet}_{\mathrm{Sc}(\tilde A)\tilde B}
=\mathrm{Sc}(\tilde A)\,L^{\bullet}_{\tilde B},
$$

so the composite is a multiplication, the family is closed, it is a complex vector space of dimension four, and
the assignment is **not** a representation of the algebra: the composite is not $L^{\bullet}_{\tilde A\bullet\tilde B}$.

*Proof.* Chaining the shape theorem gives $L^{\bullet}_{\tilde A}(L^{\bullet}_{\tilde B}\tilde R)=L^{\bullet}_{\tilde A}\bigl(N(\tilde B,\tilde R)e_0\bigr)=N(\tilde B,\tilde R)N(\tilde A,e_0)e_0=\mathrm{Sc}(\tilde A)L^{\bullet}_{\tilde B}\tilde R$, with $N(\tilde A,e_0)=A_0=\mathrm{Sc}(\tilde A)$; linearity in the parameter gives the first form. *The Multiplication Operators of the Symmetric Quaternionic Algebra*, §*Composition and the Algebra of Operators*.

**Corollary (a semigroup without a two-sided identity).** The composition is associative and the family is
closed; the parameters of scalar coordinate one are **left identities**; there is no right identity and no
two-sided identity; and the family is not commutative,
$L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}=\mathrm{Sc}(\tilde A)L^{\bullet}_{\tilde B}$ against
$L^{\bullet}_{\tilde B}L^{\bullet}_{\tilde A}=\mathrm{Sc}(\tilde B)L^{\bullet}_{\tilde A}$.

**Read as a physical statement.** The operator layer changes both the commutativity and the unit of the
operation: the product of two operations is commutative, but the composition of their operators is not, and while
the algebra has no unit the operator family has a hyperplane of left identities. The interpretation is that the algebra
and its operator layer are **different objects** — what the coupling cannot compose, its operators can still
multiply.

**Theorem (the operator identity, and the two failures).** For every $\tilde X$,

$$
\bigl(L^{\bullet}_{\tilde X}\bigr)^{2}=X_0\,L^{\bullet}_{\tilde X},
$$

the composition law at one element. The product is **not associative**: at $(\tilde P,\tilde Q,\tilde R)=(e_1,e_1,e_0)$
the bracketings differ, $(e_1\bullet e_1)\bullet e_0=e_0\neq0=e_1\bullet(e_1\bullet e_0)$, the general associator
being $\bigl(N(\tilde P,\tilde Q)R_0-P_0N(\tilde Q,\tilde R)\bigr)e_0$. The product is **not a Jordan product**:
at $(\tilde P,\tilde Q)=(e_1,e_1)$ the two sides of
$\tilde P\bullet(\tilde Q\bullet(\tilde P\bullet\tilde P))=(\tilde P\bullet\tilde Q)\bullet(\tilde P\bullet\tilde P)$
are $0$ and $e_0$. What holds instead, on the operators, is the **scaling law**
$L^{\bullet}_{\tilde X}L^{\bullet}_{\tilde Z}=X_0L^{\bullet}_{\tilde Z}$, whose square form is the operator
identity above.

*Proof.* The operator identity is the composition law at $\tilde A=\tilde B=\tilde X$. The associativity witness
and the general associator are *Introduction to the Symmetric Quaternionic Algebra of Biquaternions*, §*Associativity*; the Jordan witness is the same article, §*The Two Classical Identities*, and is
read physically in the sibling *Why a Central Product Cannot Compose: the Radical and the Isotropic Elements*.
The scaling law is *The Specificities of the Symmetric Quaternionic Algebra*, §*The Operator Identity*, where it
is called the exact replacement of the criterion $L^{\bullet}_{\tilde X}=L^{\bullet}_{\tilde X\bullet\tilde X}$,
which fails here.

**Read as a physical statement.** The collapse of the commutator does not imply the collapse of the associator:
forgetting the order of two operations is not making a chain of them bracketing-free. The interpretation of the scaling
law is that a chain of two couplings is **one** coupling scaled by the scalar part of the first operation, so the
block's iteration rule is a multiplication by a number and never a genuine composition; the operator identity is
the block's substitute for the Jordan identity it fails, and it is a law of scaling, not of order.

## The Adjoint of the Quaternion Form Does Not Keep the Family

**Definition (the quaternion form).** The form of the band is the coefficient of its product,

$$
N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\vec P,\vec Q),
\qquad \mathrm{Gram}=I_4 .
$$

It is $\mathbb{C}$-bilinear, symmetric, non-degenerate, of Gram matrix the identity, hence of rank four over
$\mathbb{C}$ with trivial radical; over $\mathbb{C}$ it has no signature, and after the realification it is of
signature $(4,4)$ and index four, with the material sector $\mathbb{M}_-$ carrying the interval signature
$(-,+,+,+)$. It is **not invariant** under the product, the witness $(e_1,e_1,e_0)$ giving
$N(\tilde P\bullet\tilde Q,\tilde R)=1$ against $N(\tilde P,\tilde Q\bullet\tilde R)=0$, which is the
form-theoretic face of the failure of the Jordan identity.

*Proof.* The coordinate form and the Gram matrix are read on the basis; the Gram matrix is the identity, so the
rank over $\mathbb{C}$ is four and the radical is trivial, and over $\mathbb{C}$ the form has no signature. The
realification is $\mathrm{diag}(I_4,-I_4)$, of signature $(4,4)$ and index four; on the material sector, where
$Q_0=ir_0$ and $Q_k=r_k$ with $r_\mu$ real, it reads $-r_0^{2}+r_1^{2}+r_2^{2}+r_3^{2}$ and is therefore of
signature $(-,+,+,+)$. The non-invariance is
$N(\tilde P\bullet\tilde Q,\tilde R)=N(\tilde P,\tilde Q)R_0$ against
$N(\tilde P,\tilde Q\bullet\tilde R)=P_0N(\tilde Q,\tilde R)$. *The Quaternion Form as a Product on the
Symmetric Quaternionic Algebra*, §*The Gram Matrix and the Rank*, §*The Realification and the Signature* and
§*The Invariance, and Its Failure*; the sector signature is *Norm and Invertibility in the General Quaternionic Algebra*.

**Read as a physical statement.** The form is the pairing that defines the coupling, carried by the same symbol
$N$ as its coefficient, and its non-invariance is the interpretation that the coupling cannot be transported across
itself. Its realified signature $(4,4)$ is the interpretation that the coefficient is **indefinite**, a signed
correlation and not a norm, which is why the band carries a coupling and no positivity; the boundary against the
general plain form $B$ is the sibling article's, and the discrimination of the form is *Mass, Rank and the
Positivity of the Dagger*.

**Theorem (the associate, and what it does to the parameter).** For all $\tilde A,\tilde X,\tilde Y$,

$$
N\bigl(L^{\bullet}_{\tilde A}\tilde X,\tilde Y\bigr)
=N\bigl(\tilde X,(L^{\bullet}_{\tilde A})^{\approx}\tilde Y\bigr),
\qquad
(L^{\bullet}_{\tilde A})^{\approx}(\tilde Y)=Y_0\tilde A ,
$$

and in the basis the associate is the **transpose**. It **keeps the side**, there being one; it **conjugates
nothing**; and it **does not keep the parameter in the multiplier slot**: it moves the parameter into the value,
multiplied by the scalar coordinate of the argument. The multiplication is self-associate,
$(L^{\bullet}_{\tilde A})^{\approx}=L^{\bullet}_{\tilde A}$, exactly when the parameter is **central**, $\vec A=0$,
that is when $L^{\bullet}_{\tilde A}$ is a multiple of the projection $E:\tilde Y\mapsto Y_0e_0$ onto the central
line.

*Proof.*
$N(L^{\bullet}_{\tilde A}\tilde X,\tilde Y)=N\bigl(N(\tilde A,\tilde X)e_0,\tilde Y\bigr)=N(\tilde A,\tilde X)Y_0$,
and
$N\bigl(\tilde X,Y_0\tilde A\bigr)=Y_0\bigl(X_0A_0+(\vec X,\vec A)\bigr)=Y_0N(\tilde A,\tilde X)$;
the form is non-degenerate, so the associate is unique, and it is the transpose because the Gram matrix is the
identity. Equality with $L^{\bullet}_{\tilde A}$ needs $Y_0\tilde A=N(\tilde A,\tilde Y)e_0$ for every $\tilde Y$;
at $\tilde Y=e_k$ this gives $A_ke_0=0$ for $k=1,2,3$, hence $\vec A=0$, and then it holds. *The
Multiplication Operators of the Symmetric Quaternionic Algebra*, §*The Adjoint with Respect to the Form*.

**Read as a physical statement.** The adjoint for the form of the coupling **is not a coupling**: it returns the
parameter as a value, times the argument's scalar coordinate, so the pairing of a comparison is a functional and
not the transpose of the operator back into the family. The interpretation is that the coupling is **self-paired exactly
on the central line**: only a purely scalar operation is a symmetric comparison, and a material parameter is
never one. The self-pairing has no side to keep and no conjugate to apply, because the coupling has one side and
the quaternion form carries no conjugation; the conjugation belongs to a different adjoint, the Hermitian one, and
the contrast is the crossing reader.

**Corollary (the composite is transported backwards).** $(L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B})^{\approx}=(L^{\bullet}_{\tilde B})^{\approx}(L^{\bullet}_{\tilde A})^{\approx}=\mathrm{Sc}(\tilde A)(L^{\bullet}_{\tilde B})^{\approx}$, and a composite is its own associate exactly when $A_0=0$ or $\tilde B$ is central.

**Read as a physical statement.** A chain of two comparisons is transported backwards, and only a chain whose
first operation has vanishing scalar part, or whose second parameter is central, is invisible to the reversal.
The interpretation is that the adjoint of the block reads the **pair** of parameters and not one of them alone.

## The Types of the Operators

### The Self-Adjoint and the Skew-Adjoint Criteria

**Theorem (the types for the quaternion form).** The multiplication $L^{\bullet}_{\tilde A}$ is **self-adjoint**
for $N$ if and only if $\tilde A$ is central, $\vec A=0$; the self-adjoint multiplications are therefore the
family $\{L^{\bullet}_{\lambda e_0}\}=\{\lambda E\}$ of the scalar multiples of the projection onto the central
line. The only **skew-adjoint** multiplication is the zero operator.

*Proof.* Self-adjointness is $(L^{\bullet}_{\tilde A})^{\approx}=L^{\bullet}_{\tilde A}$, which is $\vec A=0$ by the
associate theorem. Skew-adjointness is $Y_0\tilde A=-N(\tilde A,\tilde Y)e_0$ for every $\tilde Y$; the vector
part gives $Y_0\vec A=0$, so $\vec A=0$, and then the central part $Y_0A_0=-A_0Y_0$ forces $A_0=0$. *The
Multiplication Operators of the Symmetric Quaternionic Algebra*, §*The Adjoint with Respect to the Form*.

**Read as a physical statement.** The symmetric comparisons of the band are the scalars: an operation is a
symmetric pairing exactly when it is a multiple of the unit, and the projectors $X_0=1$ all carry a vector part
and are therefore **not** symmetric. The interpretation is that the coupling has no generator of its own: the only
skew-adjoint multiplication is zero, and what is infinitesimal in the block is outside the family.

### The Derivations of the Block

**Theorem (the derivations are outer and outside the family).** The **derivations** of the block, the maps $D$
with $D(\tilde X\bullet\tilde Y)=(D\tilde X)\bullet\tilde Y+\tilde X\bullet(D\tilde Y)$, are exactly the maps
with $De_0=0$ and $D^{\mathsf T}+D=0$, the antisymmetric matrices of the vector subspace, a space of complex
dimension three isomorphic to $\mathfrak{so}(3,\mathbb{C})$; they are **all outer**, the inner derivations
$\tilde X\mapsto\tilde A\bullet\tilde X-\tilde X\bullet\tilde A$ vanishing identically by commutativity. The
bracket $[L^{\bullet}_{\tilde A},L^{\bullet}_{\tilde B}]=\mathrm{Sc}(\tilde A)L^{\bullet}_{\tilde B}-\mathrm{Sc}(\tilde B)L^{\bullet}_{\tilde A}$
is **not** a derivation, so the operator layer is not a Lie algebra of derivations.

*Proof.* The derivation condition gives $De_0=\delta e_0$ with $\delta=2\delta$, hence $\delta=0$, and
$D^{\mathsf T}+D=0$; antisymmetric matrices killing $e_0$ act on the three-dimensional orthogonal complement and
form the displayed space. The inner derivations vanish by commutativity, and the bracket is checked directly not
to satisfy the derivation condition. *The Multiplication Operators of the Symmetric Quaternionic Algebra*,
§*The Derivations of the Block*.

**Read as a physical statement.** The infinitesimal structure of the band is not the commutators of the
couplings, as it is for the symmetrised plain block; it is the three-dimensional algebra of antisymmetric maps of
the material directions. The interpretation is that the coupling's symmetry data is a **rotation algebra of the vector
directions** and not a bracket of its own operators.

## The Symmetries of the Form and of the Product

### The Form-Preserving Operators

**Theorem (the form-preserving operators).** No non-zero multiplication preserves $N$, a rank-one operator being
unable to preserve a non-degenerate form; and no two-sided operator of the block does either, since every
two-sided operator $L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}=\mathrm{Sc}(\tilde A)L^{\bullet}_{\tilde B}$
is rank one. The operators preserving the form are the **complex-orthogonal maps**

$$
G_N=\{\,T\in GL(\mathbb{B}):T^{\mathsf T}T=I_4\,\},
$$

of complex dimension six, and every one of them is invertible and therefore outside the rank-one family.

*Proof.* $N(T\tilde X,T\tilde Y)=N(\tilde X,\tilde Y)$ reads $T^{\mathsf T}T=I_4$ on the coordinates; a rank-one
operator is singular, and an isometry of a non-degenerate form is invertible. *The Multiplication Operators of
the Symmetric Quaternionic Algebra*, §*The Two Groups of Linear Maps*.

**Read as a physical statement.** The coupling never preserves the pairing that defines it: it defines a metric
on pairs of operations without being a symmetry of that metric. The interpretation is that the coupling is a
**measurement of the pairing and not a motion of it**; the symmetries of the pairing are two-sided operators
outside the family.

### The Product-Preserving and the Multiplicative Operators

**Theorem (the product-preserving operators).** The operators preserving the **product** are the subgroup of
$G_N$ fixing the unit,

$$
G_{\star}=\{\,T\in G_N:T e_0=e_0\,\},
$$

of complex dimension three, which contains the eight diagonal sign maps
$\operatorname{diag}(1,u_1,u_2,u_3)$ with $u_k=\pm1$; the **structure group**, transporting the product to a
scalar multiple, is the intermediate group with $T^{\mathsf T}T=\mu I_4$ and $Te_0\in\mathbb{C}e_0$, so that
$G_{\star}=G^{\mathrm{str}}_{\star}\cap\{Te_0=e_0\}$. The Lie algebra of $G_{\star}$ is the three-dimensional
space of the derivations of the previous section.

*Proof.* The product condition $T(\tilde X\bullet\tilde Y)=(T\tilde X)\bullet(T\tilde Y)$ adds $Te_0=e_0$ to
the form condition, which removes three parameters; the diagonal sign maps satisfy both, and the first-order
form of the two conditions is $X^{\mathsf T}+X=0$ with $Xe_0=0$. *The Multiplication Operators of the Symmetric
Quaternionic Algebra*, §*The Two Groups of Linear Maps*.

**Read as a physical statement.** The transformations the coupling admits are read on the three material
directions and fix the informational unit: a change of frame of the coupling is a **rotation of the material
frame**, and the eight sign maps are the interpretation that the coupling is invariant under the independent reflection
of the three directions. The double cover of that rotation group is the spin group, cited next and not
re-derived here.

**Theorem (the multiplicative operators).** A multiplication is **multiplicative**,
$L^{\bullet}_{\tilde A}(\tilde X\bullet\tilde Y)=(L^{\bullet}_{\tilde A}\tilde X)\bullet(L^{\bullet}_{\tilde A}\tilde Y)$
for all $\tilde X,\tilde Y$, if and only if it is the zero operator; in particular the projection
$E=L^{\bullet}_{e_0}$ is not multiplicative.

*Proof.* At $\tilde X=e_0$ the condition reads $Y_0A_0e_0=A_0N(\tilde A,\tilde Y)e_0$; if $A_0\neq0$ then
$Y_0=N(\tilde A,\tilde Y)$ for every $\tilde Y$, that is $\tilde A=e_0$, which fails at
$(\tilde X,\tilde Y)=(e_1,e_1)$; if $A_0=0$ it becomes $N(\tilde A,\tilde X)N(\tilde A,\tilde Y)=0$ for all
$\tilde X,\tilde Y$, that is $\tilde A=0$. *The Specificities of the Symmetric Quaternionic Algebra*, §*The
Isolation among the Twelve*.

**Read as a physical statement.** No non-zero comparison is multiplicative: a coupling of two operations
carried through a third is not the coupling of the two images. The interpretation is that the coupling **does not
compose**, the sibling article's caution in the operator language; the only multiplicative multiplication is the
zero one, and the identity operator, which the general plain row has, is not even in the family.

## The Two-Sided Operators and the Spin Group

**Definition.** The **two-sided operator** of a pair $(\tilde A,\tilde B)$ is the composite
$L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}$, and the **sandwich** or algebraic norm two-sided operator of an element
is $\Theta^{\bullet}_{\tilde A}=L^{\bullet}_{\tilde A}R^{\bullet}_{\tilde A}=L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde A}$.
One-sided and two-sided operators are the same family here, because $L^{\bullet}=R^{\bullet}$.

**Theorem (the two-sided operators are rank one, and no spin group is realised).** Every two-sided operator of
the block is the composite $L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}=\mathrm{Sc}(\tilde A)L^{\bullet}_{\tilde B}$,
of rank one whenever $\mathrm{Sc}(\tilde A)\tilde B\neq0$, and the algebraic norm one is
$\Theta^{\bullet}_{\tilde A}=A_0L^{\bullet}_{\tilde A}$; none is invertible, so the **group of invertible
two-sided operators of the block is trivial**. In the Clifford structure of the same space, by contrast, the
invertible two-sided operators form the group of sandwiches $T_{a,b}$ with unit parameters, whose kernel is the
algebraic norm of the central units, and inside it the even versors of unit norm form the **spin group**, whose
sandwich action on the vector space is the double cover of the rotations.

*Proof.* The composite is $L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}=\mathrm{Sc}(\tilde A)L^{\bullet}_{\tilde B}$
and has rank one; composition cannot raise rank, so no composite is invertible, and the identity is not in the
family. The group of invertible sandwiches, its kernel and the spin group as a group of invertible two-sided
operators are *The Two-Sided Operators and the Spin Group* and *The Sandwich on a Clifford Algebra*, quoted and
not re-derived.

**Read as a physical statement.** The spin group is a group of **invertible** two-sided operators, and the
coupling's two-sided operators are the extreme opposite: every non-zero one is rank one. The interpretation is
therefore a boundary, not a realisation: **the symmetrisation that produces the coupling destroys invertibility,
and with it the spin group**; the double cover of the rotation group lives over the parent structure of the same
space, not over this band's product. What the band retains of that rotation data is the derivation algebra
$\mathfrak{so}(3,\mathbb{C})$, whose own double cover is the spin group of the parent, cited and not proved.

## The Operators Acting on the State Space

**Proposition (the coupling is a functional on the state space, not an endomorphism).** On the minimal left
ideal, the **state space**

$$
S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\hat\Upsilon_2\},
\qquad
\tilde\Pi_+=\tfrac12(e_0+ie_3),\quad \hat\Upsilon_2=\tfrac12(ie_1+e_2),
$$

Here $ie_3$ is a root of $+1$, $(ie_3)^2=e_0$, and $\tilde\Pi_+$ and $\tilde\Pi_-$ are its two associated idempotents.

the multiplication acts by $L^{\bullet}_{\tilde A}s=N(\tilde A,s)e_0$ for $s\in S$; its image therefore lies in
the central line $\mathbb{C}e_0$, which meets $S$ only at zero, so a non-zero multiplication is **not** an
endomorphism of the state space. On the basis it is the rank-one functional
$L^{\bullet}_{\tilde A}|_S=\bigl(N(\tilde A,\tilde\Pi_+),N(\tilde A,\hat\Upsilon_2)\bigr)\otimes e_0$, with
kernel a line of $S$ for a parameter that is not $N$-orthogonal to $S$. A **central** parameter acts by
$L^{\bullet}_{\lambda e_0}s=\lambda\,\mathrm{Sc}(s)e_0$, the scalar projection onto the central value. On the
**material** sector the coupling of two material operations is real,
$L^{\bullet}_{\tilde A}\mathbb{M}_-\subseteq\mathbb{R}e_0\subseteq\mathbb{M}_+$ for $\tilde A\in\mathbb{M}_-$.

*Proof.* The display is the shape theorem restricted to $S$; the intersection $\mathbb{C}e_0\cap S=\{0\}$
follows from the corner basis, since $e_0=\tilde\Pi_++\tilde\Pi_-$ and $\tilde\Pi_-\notin S$; the central case is
$N(\lambda e_0,s)=\lambda\mathrm{Sc}(s)$; the reality on the material sector is the anti-Hermiticity of both
parameters, $(N(\tilde A,s))^{*}=N(\tilde A,s)$. The ideal and its corner basis are *The Spinor Space as a Module
and as a Hilbert Space*; the shape theorem is *The Multiplication Operators of the Symmetric Quaternionic
Algebra*.

**Read as a physical statement.** The coupling does not move a state; it **measures** it. Its value is a number
on the central line, in the informational sector, so the coupling is a map from the material sector to the
informational scalars and carries no phase of its own because its image is central. The interpretation is that the
operator of the band is a **functional and not a transformation**: a state is contracted with the parameter and
returned as the number the comparison carries, and the material-to-informational shift of the image is the
operator form of the interpretation that a material coupling returns a scalar and not another material operation.

## The Sandwich and the Inner Automorphism

**Proposition (the sandwich collapses to a scaled projection).** The algebraic norm two-sided operator of the block is

$$
\Theta^{\bullet}_{\tilde A}(\tilde X)=A_0\,L^{\bullet}_{\tilde A}\tilde X=A_0X_0\tilde A ,
$$

of rank one for $A_0\neq0$ and the zero operator otherwise; its associate for $N$ is
$(\Theta^{\bullet}_{\tilde A})^{\approx}(\tilde Y)=A_0Y_0\tilde A$, and it is
self-adjoint exactly when $A_0=0$ or $\tilde A$ is central. It is never an automorphism.

*Proof.* The sandwich is $L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde A}=A_0L^{\bullet}_{\tilde A}$ by the
composition law; the associate is the associate theorem scaled by $A_0$, and the criterion is its self-adjointness
condition; rank one excludes invertibility and hence automorphism.

**Theorem (the sandwich against the inner automorphism and the parent sandwiches).** The inner automorphism of
the plain product,

$$
\mathrm{Ad}_{\tilde A}(\tilde X)=\tilde A\tilde X\tilde A^{-1}=L_{\tilde A}R_{\tilde A^{-1}}(\tilde X),
$$

and the invertible sandwiches $T_{a,b}$ of the parent structure of *The Two-Sided Operators and the Spin Group*
are invertible of rank four for a unit parameter; neither is reachable by the rank-one sandwich of the block,
and the block has **no inner automorphism of its own**, its product having no unit.

*Proof.* The inner automorphism is an algebra automorphism of the plain product and is therefore invertible of
rank four on $\mathbb{B}\cong\mathbb{C}^{4}$; a rank-one operator is singular, so no equality with an invertible
rank-four operator holds. The group of invertible sandwiches, its kernel and the spin group are *The Two-Sided
Operators and the Spin Group*, cited and not re-derived. The absence of a unit and the projection in place of
the identity are *Why a Central Product Cannot Compose: the Radical and the Isotropic Elements*.

**Read as a physical statement.** The coupling's two-sided operator is a scalar times a projection: it reads a
state's scalar coordinate and returns the parameter, and it is never a conjugation. The interpretation is that the band
cannot **relabel** the algebra — the interpolation between a projection and a conjugation that the symmetrised
plain block performs at a symmetry is destroyed here by the collapse $L^{\bullet}=R^{\bullet}$ — and that the
conjugation of the band is the parent structure's, two-sided and outside the family.

## A Worked Case

Take first the parameter with scalar coordinate one, $\tilde A=e_0+2e_1$, of which $N(\tilde A,\tilde A)=5$ and
$A_0=1$. Its multiplication operator on the basis $(e_0,e_1,e_2,e_3)$ is

$$
L^{\bullet}_{e_0+2e_1}=
\begin{pmatrix}1&2&0&0\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
\qquad
\operatorname{Tr}=A_0=1,\qquad
\operatorname{rank}=1,\qquad
\det=0,
$$

a **projector** because $A_0=1$, with kernel the hyperplane $X_0+2X_1=0$ and image the central line. Its
associate is the transpose,

$$
(L^{\bullet}_{e_0+2e_1})^{\approx}=
\begin{pmatrix}1&0&0&0\\2&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
\qquad
(L^{\bullet}_{e_0+2e_1})^{\approx}(e_0)=e_0+2e_1=\tilde A,\qquad
(L^{\bullet}_{e_0+2e_1})^{\approx}(e_1)=0,
$$

which is **not** a multiplication and not the operator itself: the parameter is a material direction, so by the
self-adjoint criterion the projector is not symmetric.

Take next the **isotropic** parameter $\tilde B=e_1+ie_2$, with $N(\tilde B,\tilde B)=1-1=0$. Its operator is the
one-row matrix

$$
L^{\bullet}_{e_1+ie_2}=
\begin{pmatrix}0&1&i&0\\0&0&0&0\\0&0&0&0\\0&0&0&0\end{pmatrix},
\qquad
\bigl(L^{\bullet}_{e_1+ie_2}\bigr)^{2}=0,
$$

**square-zero** because $B_0=0$, of rank one, and the operator identity reads
$L^{\bullet2}_{\tilde B}=B_0L^{\bullet}_{\tilde B}=0$. The two parameters give an order-free product and an
ordered operator composition:

$$
L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}=A_0L^{\bullet}_{\tilde B}=L^{\bullet}_{\tilde B},
\qquad
L^{\bullet}_{\tilde B}L^{\bullet}_{\tilde A}=B_0L^{\bullet}_{\tilde A}=0,
$$

so the operators of two operations the product cannot distinguish in order differ by the order of composition.

Take finally the **central** parameter $\tilde C=ie_0$, whose operator $L^{\bullet}_{ie_0}=iE$ has the algebraic norm
matrix $i\,\mathrm{diag}(1,0,0,0)$ and is self-adjoint for $N$: the scalar multiples of $E$ are exactly the
symmetric couplings, and $\tilde C\bullet\tilde X=iX_0e_0$ returns the scalar coordinate scaled by $i$. On the
state basis the first parameter acts by $L^{\bullet}_{\tilde A}\tilde\Pi_+=\tfrac12 e_0$ and
$L^{\bullet}_{\tilde A}\hat\Upsilon_2=ie_0$, both central and in neither summand of $S$: the image of the state
space is the central line. The three parameters — a material projector, an isotropic vector and a central scalar
— display the two type criteria, the two rank-one operators, the collapse of the sandwich and the functional
action on the state space.

**A numerical check.** For at most one hundred elements per loop a single script recomputed the claims outside
the repository: the product formula
$\tilde P\bullet\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)=N(\tilde P,\tilde Q)e_0$
and its centrality; the collapse $L^{\bullet}_{\tilde A}=R^{\bullet}_{\tilde A}$ and the one-row matrix, with
$\operatorname{Tr}(L^{\bullet}_{\tilde A})=A_0$ and $\det(L^{\bullet}_{\tilde A})=0$; the composition law
$L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}=A_0L^{\bullet}_{\tilde B}$ and the operator identity
$L^{\bullet2}_{\tilde X}=X_0L^{\bullet}_{\tilde X}$; the associate $(L^{\bullet}_{\tilde A})^{\approx}(\tilde Y)=Y_0\tilde A$
with the self-adjoint criterion $\vec A=0$ and the skew-adjoint criterion $\tilde A=0$; the projector and
square-zero classifications $X_0=1$ and $X_0=0$; the multiplicativity criterion $\tilde A=0$ and the absence of any
form-isometry in the family; the realified signature $(4,4)$ of $N$; the reality of the coupling on the material
sector; the derivation space $\{De_0=0,\ D^{\mathsf T}+D=0\}$ of dimension three, with all its elements
derivations and with the eight diagonal sign maps product-preserving; and the three worked parameters, including
$L^{\bullet}_{\tilde A}\tilde\Pi_+=\tfrac12e_0$ and $L^{\bullet}_{\tilde A}\hat\Upsilon_2=ie_0$. All were
confirmed on every sample, and the associativity and Jordan witnesses were recomputed element by element.

## The Bound

The article declares the boundary of its one cell in the grid of the twelve operator rows.

- **The element theory is not re-proved here.** The centrality of the value, the absence of a unit, the idempotents $0$ and $e_0$, the isotropic cone and the failure of the Jordan identity are *Introduction to the Symmetric Quaternionic Algebra of Biquaternions* and *The Radical and the Isotropic Elements of the Symmetric Quaternionic Algebra*; this article reads the operators they produce.
- **The operator theory is cited, not re-derived.** The one family, the shape, the composition, the trace, the determinant, the adjoint and the derivations are *The Multiplication Operators of the Symmetric Quaternionic Algebra*; the form, its Gram matrix, its realification, its signature and its non-invariance are *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* and *The Four Forms, the Four Algebraic Norms and the Change of Scalars*; the scalar coordinate and the scalar law are *The Specificities of the Symmetric Quaternionic Algebra*; and the parent row and the group of invertible two-sided operators are *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* and *The Two-Sided Operators and the Spin Group*.
- **The siblings', the adjoint's and the crossing reader's business.** That the operation is a scalar coupling and that it cannot compose are the two sibling articles and are not repeated; the physical adjoint is not the quaternion-form adjoint, the observables and generators being those of the Hermitian form in *Observables, Gauge Generators and the Chirality of the Internal Action*, with the positivity in *Mass, Rank and the Positivity of the Dagger*; and the comparison of the twelve adjoints is the crossing reader *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket*, not one of the twelve.

**What the framework does not claim.** The interpretation does not derive the coupling from the operator calculus; it
reads the object the band already uses and names the operator behind it. It does not identify the quaternion-form
adjoint with hermiticity, the two adjoints being different and equal only on the central line, and it does not
claim a generator algebra inside the family: the family has no non-zero skew-adjoint element, and the
infinitesimal structure is the outer derivation algebra of the vector subspace.

## The Ledger

**Proved.** The product is commutative, so $L^{\bullet}_{\tilde A}=R^{\bullet}_{\tilde A}$ and
$L^{\bullet}_{\tilde A}\tilde R=N(\tilde A,\tilde R)e_0$ with rank one, image the central line, kernel the
hyperplane $N(\tilde A,\cdot)=0$, trace $A_0$ and determinant zero for $\tilde A\neq0$, the assignment being
faithful; the composition law is
$L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}=L^{\bullet}_{\mathrm{Sc}(\tilde A)\tilde B}=\mathrm{Sc}(\tilde A)L^{\bullet}_{\tilde B}$,
the family is a complex four-dimensional semigroup with left identities the parameters of scalar coordinate one,
no two-sided identity, and non-commutative operator composition; the operator identity is
$L^{\bullet2}_{\tilde X}=X_0L^{\bullet}_{\tilde X}$, the product is neither associative (witness $e_1,e_1,e_0$)
nor a Jordan product (witness $e_1,e_1$), and the scaling law
$L^{\bullet}_{\tilde X}L^{\bullet}_{\tilde Z}=X_0L^{\bullet}_{\tilde Z}$ holds instead; the quaternion form
$N(\tilde P,\tilde Q)=P_0Q_0+(\vec P,\vec Q)$ has Gram matrix the identity, rank four over $\mathbb{C}$ and
realified signature $(4,4)$ of index four with material-sector signature $(-,+,+,+)$, is symmetric and
non-degenerate and is **not invariant**, and its associate is the
transpose, $(L^{\bullet}_{\tilde A})^{\approx}(\tilde Y)=Y_0\tilde A$, a multiplication exactly at the central
parameters; the self-adjoint multiplications are the central ones, the only skew-adjoint one is zero, and they are
the scalar multiples of the projection $E$; the derivations are the antisymmetric matrices killing $e_0$, of
complex dimension three, all outer, and the bracket of two multiplications is not a derivation; no non-zero
multiplication preserves $N$ or is multiplicative, the form-preserving operators are $G_N$ of complex dimension
six, the product-preserving ones $G_{\star}$ of complex dimension three containing the eight diagonal sign maps,
and the structure group rescales; the two-sided operators are rank one, the group of invertible two-sided
operators is trivial, and the sandwich collapses to $\Theta^{\bullet}_{\tilde A}=A_0L^{\bullet}_{\tilde A}$, a
scaled projection, self-adjoint exactly when $A_0=0$ or $\tilde A$ is central; and on the state space the
multiplication is the functional $N(\tilde A,\cdot)$ times $e_0$, with image the central line, and it is real on
the material sector.

**Interpretations.** That the coupling has **one family** and no side; that the adjoint for the quaternion form **does
not keep the family** but returns the parameter as a value times the argument's scalar coordinate, keeping the
side and conjugating nothing; that the multiplication is self-paired exactly on the **central line**; that the
band has **no generator** of its own, the infinitesimal structure being the outer derivation algebra
$\mathfrak{so}(3,\mathbb{C})$ of the material directions; that no non-zero multiplication preserves the form or is
multiplicative, so the coupling measures the pairing and does not compose; that the symmetries of the form and of
the product are **two-sided** and disjoint from the family; that the two-sided operators are rank one, so the
**spin group has no instance in the band** and its home is the parent structure; that the sandwich is a scaled
projection and not a conjugation, the block having no inner automorphism of its own; and that on the state space
the operator is a **functional**, contracting a state with the parameter and returning a central number. Each is
the framework's naming of a proved algebraic fact and is labelled as such.

## Physical Readings

The operators of the symmetric quaternionic product read as one family, and the interpretation of the collapse is the
band's job word. Where the parent row has a left family that is the opposite monoid $\mathbb{B}^{\mathrm{opp}}$ and
a right family that does not close, here the commutativity of the operation makes the two one, and the interpretation is that the
**scalar coupling carries no side**: a comparison of two material operations attaches the same operator from
either slot, and the operator content of the order is gone. The comparison itself is read on the operators as a
**rank-one functional**: the multiplication is the pairing with the parameter, read with the fixed value $e_0$, so
its kernel is the hyperplane of operations the coupling does not see and its image is the central line — the
coupling returns a number and not a direction.

The adjoint is read as the **symmetry of the comparison and not as a comparison**: for the quaternion form it
carries the multiplication to the functional $Y_0\tilde A$ that returns the parameter as a value, so association
keeps the side, conjugates nothing, and fixes the operator exactly on the central line. The interpretation is that the
symmetric comparisons of the band are the purely scalar operations and that a material direction is never one;
the conjugation of a parameter belongs to the Hermitian form, the adjoint of the physical dictionary, and not to
the quaternion form, which has none to apply. Read on the types, the interpretation is the same statement in the sector
language: the central line is the self-adjoint class, there is no non-zero skew-adjoint multiplication, and the
infinitesimal structure is the three-dimensional rotation algebra of the material directions, outer and outside
the family; what is infinitesimal in the band is not the commutators of the couplings but the rotations of the
frame they are read in.

Read on the symmetries and the two-sided operators, the form is preserved by the two-sided complex-orthogonal maps and the product by their subgroup fixing the unit, while every multiplication is rank one; the interpretation is the **separation of measurement and motion**. The two-sided operators are rank one, so the spin group is not realised in the band: the symmetrisation that makes the coupling destroys invertibility and leaves the double cover to the parent. Read on the sandwich, the algebraic norm two-sided operator is a scalar times a projection and never a conjugation, so the coupling cannot relabel the algebra. Read on the state space, the operator is a functional, contracting a state with the parameter and returning a central number, so a material coupling of material operations is read as a scalar of the informational sector carrying no phase of its own. The distinctions are labelled throughout: what is proved is the algebra, what is proposed is the naming.

## Summary

The operators of the symmetric quaternionic product are one family, because the product is commutative: the left and the right multiplication by an element coincide, $L^{\bullet}_{\tilde A}=R^{\bullet}_{\tilde A}$, and the multiplication is the rank-one operator $L^{\bullet}_{\tilde A}\tilde R=N(\tilde A,\tilde R)e_0$, of image the central line, kernel the hyperplane $N(\tilde A,\cdot)=0$, trace $A_0$ and determinant zero, faithful in the parameter. The multiplications compose by $L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}=\mathrm{Sc}(\tilde A)L^{\bullet}_{\tilde B}$, so the family is a complex four-dimensional semigroup with left identities the parameters of scalar coordinate one and no two-sided identity, its operator composition is not commutative although the product is, and the operator identity is $L^{\bullet2}_{\tilde X}=X_0L^{\bullet}_{\tilde X}$; the product is neither associative nor a Jordan product, and the scaling law holds instead. The form of the block is the quaternion form $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\vec P,\vec Q)$, of Gram matrix the identity, rank four over $\mathbb{C}$ and realified signature $(4,4)$ of index four with material-sector signature $(-,+,+,+)$, symmetric, non-degenerate and **not invariant**; its adjoint is the transpose, $(L^{\bullet}_{\tilde A})^{\approx}(\tilde Y)=Y_0\tilde A$, so association **keeps the side**, **conjugates nothing** and **does not keep the parameter in the multiplier slot**, and a multiplication is self-adjoint exactly at the central parameters, the only skew-adjoint one being zero. The derivations are the antisymmetric matrices killing $e_0$, of complex dimension three, all outer, and the bracket of two multiplications is not a derivation; no non-zero multiplication preserves the form or is multiplicative; the form-preserving operators are $G_N$ of complex dimension six, the product-preserving ones $G_{\star}$ of complex dimension three containing the eight diagonal sign maps, and the structure group rescales. The two-sided operators are rank one, so the group of invertible two-sided operators is trivial and the spin group has no instance in the band, its home being the parent; the sandwich collapses to $\Theta^{\bullet}_{\tilde A}=A_0L^{\bullet}_{\tilde A}$, a scaled projection and never a conjugation; and on the state space the multiplication is the functional $N(\tilde A,\cdot)$ times $e_0$, with image the central line and real on the material sector. The adjoint does not keep the family, the side is kept and no conjugation is applied: that one sentence is the band's operator answer.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | The biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^{2}=-e_0$, $e_1e_2=e_3$ |
| $\tilde P\bullet\tilde Q=\tfrac12(\tilde P^{\natural}\tilde Q+\tilde Q^{\natural}\tilde P)$ | The symmetrised quaternionic product, $\mathrm{SQA}$ |
| $L^{\bullet}_{\tilde A}(\tilde Q)=\tilde A\bullet\tilde Q$ | The multiplication operator; $R^{\bullet}_{\tilde A}=L^{\bullet}_{\tilde A}$ |
| $L^{\bullet}_{\tilde A}\tilde R=N(\tilde A,\tilde R)e_0$ | The rank-one shape of the operator |
| $\operatorname{Tr}(L^{\bullet}_{\tilde A})=A_0$, $\det(L^{\bullet}_{\tilde A})=0$, $\operatorname{rank}=1$ | Its invariants for $\tilde A\neq0$ |
| $L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde B}=L^{\bullet}_{\mathrm{Sc}(\tilde A)\tilde B}=\mathrm{Sc}(\tilde A)L^{\bullet}_{\tilde B}$ | The composition law |
| $L^{\bullet2}_{\tilde X}=X_0L^{\bullet}_{\tilde X}$ | The operator identity, the block's substitute for the Jordan identity |
| $L^{\bullet}_{\tilde X}L^{\bullet}_{\tilde Z}=X_0L^{\bullet}_{\tilde Z}$ | The scaling law |
| $(e_1\bullet e_1)\bullet e_0=e_0\neq0=e_1\bullet(e_1\bullet e_0)$ | The associativity witness |
| $N(\tilde P,\tilde Q)=\mathrm{Sc}(\tilde P^{\natural}\tilde Q)=P_0Q_0+(\vec P,\vec Q)$ | The quaternion form; Gram $I_4$, realified signature $(4,4)$, material-sector $(-,+,+,+)$ |
| $(L^{\bullet}_{\tilde A})^{\approx}(\tilde Y)=Y_0\tilde A$ | The associate: the transpose; it does not keep the family |
| $(L^{\bullet}_{\tilde A})^{\approx}=L^{\bullet}_{\tilde A}\iff\vec A=0$ | Self-adjoint exactly on the central line |
| self-adjoint: $\vec A=0$; skew-adjoint: $\tilde A=0$ | The types for the quaternion form |
| $E:\tilde Y\mapsto Y_0e_0$, $L^{\bullet}_{\lambda e_0}=\lambda E$ | The projection onto the central line; the symmetric couplings |
| $\{D:De_0=0,\ D^{\mathsf T}+D=0\}\cong\mathfrak{so}(3,\mathbb{C})$ | The derivations, of complex dimension three, all outer |
| $[L^{\bullet}_{\tilde A},L^{\bullet}_{\tilde B}]=\mathrm{Sc}(\tilde A)L^{\bullet}_{\tilde B}-\mathrm{Sc}(\tilde B)L^{\bullet}_{\tilde A}$ | Not a derivation |
| $G_N=\{T:T^{\mathsf T}T=I_4\}$ | Form-preserving operators, complex dimension six |
| $G_{\star}=\{T\in G_N:Te_0=e_0\}$ | Product-preserving operators, complex dimension three |
| $G^{\mathrm{str}}_{\star}$ | The structure group, transporting the product to a scalar multiple |
| $\operatorname{diag}(1,u_1,u_2,u_3)$, $u_k=\pm1$ | The eight product-preserving sign maps |
| $L^{\bullet}_{\tilde A}$ multiplicative $\iff\tilde A=0$ | The multiplicative multiplications |
| $\Theta^{\bullet}_{\tilde A}=L^{\bullet}_{\tilde A}L^{\bullet}_{\tilde A}=A_0L^{\bullet}_{\tilde A}$ | The sandwich, a scaled projection |
| $\mathrm{Ad}_{\tilde A}=L_{\tilde A}R_{\tilde A^{-1}}$, $\mathrm{Ad}_{\tilde A}\tilde X=\tilde A\tilde X\tilde A^{-1}$ | The inner automorphism of the plain product, cited |
| $T_{a,b}$ of the parent Clifford structure | The invertible sandwiches and the spin group, cited |
| $S=\mathbb{B}\tilde\Pi_+=\mathbb{C}\{\tilde\Pi_+,\hat\Upsilon_2\}$ | The state space; $L^{\bullet}_{\tilde A}s=N(\tilde A,s)e_0$ |

## Further Reading

- *The Multiplication Operators of the Symmetric Quaternionic Algebra* (`articles_maths/the-multiplication-operators-of-the-symmetric-quaternionic-algebra.md`), the owner of the one family, the rank-one shape, the composition law, the trace, the adjoint with respect to the form, the symmetries of the form and of the product, and the derivations of the block.
- *The Quaternion Form as a Product on the Symmetric Quaternionic Algebra* (`articles_maths/the-quaternion-form-as-a-product-on-the-symmetric-quaternionic-algebra.md`), for the form, its Gram matrix, its realification, its signature and the failure of its invariance.
- *The Four Forms, the Four Algebraic Norms and the Change of Scalars* (`articles_physics/the-four-forms-the-four-algebraic-norms-and-the-change-of-scalars.md`), for the realified signature, and *The Interval as the Square and the Charge of the Material Composition* (`articles_physics/the-interval-as-the-square-and-the-charge-of-the-material-composition.md`), for the interval signature $(-,+,+,+)$ of the form on the material sector, cited and not re-proved.
- *The Specificities of the Symmetric Quaternionic Algebra* (`articles_maths/the-specificities-of-the-symmetric-quaternionic-algebra.md`), for the scalar law that isolates the block among the twelve, the operator identity $L^{\bullet2}_{\tilde X}=X_0L^{\bullet}_{\tilde X}$ and the classification of the projectors and square-zero operators by the scalar coordinate.
- *The Left Multiplications of the Quaternionic Product and the Opposite Monoid* (`articles_maths/the-left-multiplications-of-the-quaternionic-product-and-the-opposite-monoid.md`), for the parent row, the reversed composition law and the opposite monoid $\mathbb{B}^{\mathrm{opp}}$ that the symmetrisation destroys.
- *The Two-Sided Operators and the Spin Group* (`articles_maths/the-two-sided-operators-and-the-spin-group.md`), for the group of invertible two-sided operators, its kernel and the spin group as a group of invertible sandwiches, cited and not re-proved.
- *The Quaternion Form as a Product: the Scalar Coupling of Two Material Operations* (`articles_physics/the-quaternion-form-as-a-product-the-scalar-coupling-of-two-material-operations.md`), the framing article of the band, for the operation, its centrality and the scalar-coupling interpretation.
- *Why a Central Product Cannot Compose: the Radical and the Isotropic Elements* (`articles_physics/why-a-central-product-cannot-compose-the-radical-and-the-isotropic-elements.md`), for the radical, the isotropic elements, the absence of a unit and the Jordan witness, which are the band's own physics and not this article's.
- *The Spinor Space as a Module and as a Hilbert Space* (`articles_physics/the-spinor-space-as-a-module-and-as-a-hilbert-space.md`), for the minimal left ideal, its corner basis $(\tilde\Pi_+,\hat\Upsilon_2)$ and the nilpotent, which are the state space of the band.
- *Observables, Gauge Generators and the Chirality of the Internal Action* (`articles_physics/observables-gauge-generators-and-the-chirality-of-the-internal-action.md`) and *Mass, Rank and the Positivity of the Dagger* (`articles_physics/mass-rank-and-the-positivity-of-the-dagger.md`), for the physical adjoint, the observables and generators, and the positivity of the Hermitian form that the quaternion form lacks.
- *The Operators of the Twelve Structures: Multiplication, Adjoint and Bracket* (`articles_physics/the-operators-of-the-twelve-structures-multiplication-adjoint-and-bracket.md`), the crossing reader of the twelve operator rows, for the comparison of the twelve adjoints.
