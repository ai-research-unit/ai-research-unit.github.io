
# __The Left and Right Multiplication Operators on a Complex Vector Space__

## Introduction

Let $V$ be a complex vector space and $E = \operatorname{End}_{\mathbb C}(V)$ its algebra of $\mathbb{C}$-linear endomorphisms. The two **one-sided multiplications** are the operators on $E$
$$
L_A(X) = AX, \qquad R_B(X) = XB \qquad (A, B \in E),
$$
the left and the right multiplication of the algebra, and they are the basic operators of the operator layer of the category. They commute, $L_A R_B = R_B L_A$, and they carry the **complex structure**: on $E$ the scalar $i$ may be multiplied on the left or on the right, and because $i$ is central the two multiplications agree, so the complex structure of $E$ is a single operator $J_E = L_i = R_i$ that commutes with every one-sided multiplication. When a Hermitian form $h$ is chosen on $V$ the endomorphism algebra $E$ inherits the Hermitian trace form $\langle X, Y\rangle = \operatorname{tr}(X^{\dagger}Y)$ and the conjugate-linear involution $A \mapsto A^{\dagger}$; the two one-sided multiplications by a **unitary** endomorphism are isometries of the trace form, and the operators $U \mapsto L_U$ and $U \mapsto R_U$ are the two commuting representations of the unitary group by which the group acts on the operator algebra.

The article has three sections: the one-sided multiplications and the algebra they generate; the trace form of the operator algebra and the unitary one-sided operators; and the complex structure of the operator algebra and the complex-linear operators. The algebra of endomorphisms, the double centraliser theorem and the trace are *Algebras of Endomorphisms*; the Hermitian form, the unitary group and the involution are *The Unitary and Symplectic Groups* and *Hermitian Geometry and the Unitary Group*; the complex structure of a linear space is *The Involution on a Complex Vector Space*, later in this category. The adjoints of the one-sided multiplications for the trace form are *The Adjoint of the Left Multiplication on a Complex Vector Space*, in the `* Operator Theory` group. The signed variants are *The Signed Sandwich on a Complex Vector Space* and *The Signed Left Multiplication on a Complex Vector Space*, and the module-level variant is *The Graded Action on a Module over a Complex Vector Space*, the other articles of this group.

Throughout, $V$ is a finite-dimensional complex vector space of dimension $n$ with a positive-definite Hermitian form $h$, $E = \operatorname{End}_{\mathbb C}(V)$ is its endomorphism algebra of complex dimension $n^2$, $A^\dagger$ is the adjoint of $A$ for $h$, $J$ is the complex structure of $V$ (multiplication by $i$), $L_A, R_B$ are the one-sided multiplications on $E$, and $\langle X, Y\rangle = \operatorname{tr}(X^{\dagger}Y)$ is the Hermitian trace form of $E$.

## The One-Sided Multiplications and the Algebra They Generate

**Definition.** For $A \in E$ the **left multiplication** and for $B \in E$ the **right multiplication** are the operators on $E$
$$
L_A(X) = AX, \qquad R_B(X) = XB .
$$
The left and right multiplication maps are $L : E \to \operatorname{End}(E)$, $A \mapsto L_A$ and $R : E \to \operatorname{End}(E)$, $B \mapsto R_B$.

**Proposition (composition).** For all $A, B \in E$,
$$
L_A L_B = L_{AB}, \qquad R_A R_B = R_{AB}, \qquad L_A R_B = R_B L_A , \qquad L_A + R_B = R_B + L_A .
$$
In particular $L$ is a representation of the algebra $E$ on itself, $R$ is a representation of the opposite algebra $E^{\mathrm{op}}$, and the left and right images commute; the composite action $A \otimes B \mapsto L_A R_B$ is a representation of $E \otimes_{\mathbb C} E^{\mathrm{op}}$.

**Proof.** $L_AL_B(X) = A(BX) = (AB)X = L_{AB}(X)$ by the associativity of composition; $R_AR_B(X) = (XB)A = X(BA) = R_{BA}(X)$, which is the representation of the opposite product; and $L_AR_B(X) = A(XB) = (AX)B = R_BL_A(X)$ by associativity. The last assertion is the associativity of the action.

**Proposition (the images are the two copies).** The maps $L$ and $R$ are injective, $\ker L = \ker R = 0$, and $L(E)$ and $R(E)$ are subalgebras of $\operatorname{End}(E)$ isomorphic to $E$ and $E^{\mathrm{op}}$.

**Proof.** $L_A = 0$ forces $AX = 0$ for all $X$; taking $X = \mathrm{id}$ gives $A = 0$. The image $L(E)$ is closed under composition and contains $L_{\mathrm{id}} = \mathrm{id}$, hence is a subalgebra isomorphic to $E$ by injectivity; the same holds for $R$.

**Theorem (the double centraliser).** The commutant of $L(E)$ in $\operatorname{End}(E)$ is $R(E)$, and the commutant of $R(E)$ is $L(E)$; moreover
$$
\operatorname{End}(E) = L(E)\,R(E) \cong E \otimes_{\mathbb C} E^{\mathrm{op}} ,
$$
so every $\mathbb{C}$-linear operator on $E$ is a sum of two-sided multiplications.

**Proof.** A map $T$ commuting with every $L_A$ is determined by $\Phi = T(\mathrm{id})$, since $T(X) = T(L_X\,\mathrm{id}) = L_X T(\mathrm{id}) = X\Phi = R_\Phi(X)$; this gives the commutant of $L(E)$ as $R(E)$, and symmetrically. For the spanning statement, both spaces have complex dimension $n^4 = \dim E \otimes E$ — indeed $\dim\operatorname{End}(E) = (n^2)^2 = n^4 = \dim E \cdot \dim E$ — and the map $A \otimes B \mapsto L_A R_B$ is injective because it sends the basis $E_{ij} \otimes E_{kl}$ to the operator $X \mapsto E_{ij}XE_{kl}$, whose matrix units are independent; an injective linear map between spaces of the same finite dimension is an isomorphism. This is the double centraliser theorem of *Algebras of Endomorphisms*.

**Corollary (the centre and the scalars).** The centre of $E$ is $\mathbb{C}\cdot\mathrm{id}$, and for a scalar $Z \in \mathbb{C}$ the two one-sided multiplications coincide, $L_{Z\,\mathrm{id}} = R_{Z\,\mathrm{id}}$; for a general $A \in E$ the two differ unless $A$ is central.

**Proof.** The centre statement is *Algebras of Endomorphisms*; $L_Z(X) = ZX = XZ = R_Z(X)$ for $Z$ central, and $L_A \neq R_A$ for noncentral $A$ because $L_A(\mathrm{id}) = A$ while $R_A(\mathrm{id}) = A$ — the difference is visible on a non-central element $X$ with $AX \neq XA$.

## The Hermitian Trace Form and the Unitary Operators

**Definition.** The **Hermitian trace form** of $E$ is
$$
\langle X, Y\rangle = \operatorname{tr}(X^{\dagger}Y) \qquad (X, Y \in E),
$$
where $A^{\dagger}$ is the adjoint of $A$ for $h$, $h(Au,v) = h(u,A^{\dagger}v)$.

**Proposition (the trace form is a Hermitian form).** The trace form is Hermitian and positive definite, $\langle X, Y\rangle = \overline{\langle Y, X\rangle}$ and $\langle X, X\rangle = \operatorname{tr}(X^{\dagger}X) > 0$ for $X \neq 0$, and therefore makes $E$ a Hermitian space of dimension $n^2$.

**Proof.** $\langle X,Y\rangle = \operatorname{tr}(X^\dagger Y)$ and $\overline{\langle Y,X\rangle} = \overline{\operatorname{tr}(Y^\dagger X)} = \operatorname{tr}((Y^\dagger X)^\dagger) = \operatorname{tr}(X^\dagger Y)$, using $(Y^\dagger X)^\dagger = X^\dagger Y$; the diagonal is the sum of the diagonal entries of $X^\dagger X$, which in an orthonormal basis of $V$ is $\sum_{i,j}|X_{ij}|^2 > 0$ for $X\neq0$. This is the Hilbert–Schmidt form of *Hilbert Algebras*.

**Proposition (the unitary one-sided multiplications are isometries).** Let $U \in E$ be unitary for $h$, $U^{\dagger}U = UU^{\dagger} = \mathrm{id}$. Then $L_U$ and $R_U$ are isometries of the trace form,
$$
\langle L_U X, L_U Y\rangle = \langle X, Y\rangle, \qquad \langle R_U X, R_U Y\rangle = \langle X, Y\rangle ,
$$
and the maps $U \mapsto L_U$ and $U \mapsto R_U$ are commuting unitary representations of the unitary group $U(V,h)$ on the Hermitian space $E$.

**Proof.** $\langle L_UX,L_UY\rangle = \operatorname{tr}((UX)^\dagger UY) = \operatorname{tr}(X^\dagger U^\dagger U Y) = \operatorname{tr}(X^\dagger Y)$, and likewise on the right with $U^\dagger U$ placed on the other side; the representation property is the composition law, and the commutativity of the two images is the proposition above. The unitary group and the involution are *The Unitary and Symplectic Groups* and *Hermitian Geometry and the Unitary Group*.

**Remark (the form of the category).** The chosen form is the Hermitian form $h$ on $V$; it induces two forms on the operator algebra, the Hermitian trace form $\langle X,Y\rangle = \operatorname{tr}(X^\dagger Y)$ used here and the bilinear trace pairing $\operatorname{tr}(XY)$ obtained by dropping the involution. The two agree in their real part on the self-adjoint part and differ in general; it is the Hermitian trace form that the one-sided operators are measured against in this category, and it is the form with respect to which the adjoints are computed.

## The Complex Structure and the Complex-Linear Operators

**Definition.** The **complex structure** of the vector space $E$ is the operator $J_E(X) = iX$; the complex structure of $V$ is $J(v) = iv$.

**Proposition (the complex structure is the central one-sided multiplication).** $J_E = L_i = R_i$, and it commutes with every one-sided multiplication,
$$
J_E L_A = L_A J_E = L_{iA}, \qquad J_E R_B = R_B J_E = R_{iB} ;
$$
the complex structure of $E$ is thus the one-sided multiplication by the central scalar $i$, and it is a complex-linear operator of $E$ on itself. On $V$ the complex structure is $J$, and $J$ is skew-adjoint and unitary for $h$, $J^\dagger = -J$, $J^2 = -\mathrm{id}$, so $J \in E$ is an element of the operator algebra; left multiplication by $i$ and the operator $J$ are related by $L_i = i\,\mathrm{id}_{\operatorname{End}(E)}$, while $J$ acts on $V$ and not on $E$.

**Proof.** $J_E(X) = iX = Xi = R_i(X)$ because $i$ is central, and $iA = Ai$ gives the commutation. For $J$, $h(Ju,v) = h(iu,v) = i\,h(u,v)$ and $h(u,J^\dagger v) = h(u,-iv) = ih(u,v)$, so $J^\dagger = -J$; $J^2 = -\mathrm{id}$ and unitarity follow. The distinction between the scalar $i$ multiplying $E$ and the operator $J$ acting on $V$ is the distinction between the complex structure of the operator algebra and the complex structure of the space it acts on.

**Proposition (the complex-linear operators are those commuting with $J_E$).** A real-linear operator $T$ on $E$ is complex-linear for the complex structure $J_E$ exactly when $T J_E = J_E T$; the one-sided multiplications $L_A, R_B$ and every two-sided multiplication are complex-linear, and the complex-linear operators on $E$ form the algebra $\operatorname{End}_{\mathbb C}(E)$.

**Proof.** The equivalence of complex-linearity and commuting with the complex structure is the definition of a complex-linear map on a complex vector space; the one-sided multiplications commute with $J_E$ because $L_AJ_E(X) = A(iX) = i\,AX = J_EL_A(X)$ and $R_BJ_E(X) = (iX)B = i\,XB = J_ER_B(X)$, using the centrality of $i$. The two-sided multiplications are sums of composites and hence complex-linear too.

**Remark (holomorphic and antiholomorphic operators on $E$).** The complex structure $J$ of $V$ extends to $E$ in two ways: the conjugation $E \to E$, $A \mapsto JA$ or $A \mapsto AJ$ (which is the left or right multiplication by the element $J \in E$), and the $\mathbb C$-linear structure $J_E = L_i$. The two are different: $L_J(A) = JA$ is a complex-linear operator on $E$ for the structure $J_E$, whereas the conjugation by $J$, $\mathrm{Ad}_J(A) = JAJ^{-1} = -JAJ$, is its own inverse and is the involution associated with $J$; the one-sided multiplications by the elements of $E$ and the inner automorphisms by the unitary elements are the two families of operators of the operator layer, the latter developed in *The Signed Sandwich on a Complex Vector Space*.

## Summary

On the endomorphism algebra $E = \operatorname{End}_{\mathbb C}(V)$ of a complex vector space the left and right multiplications $L_A(X) = AX$ and $R_B(X) = XB$ satisfy $L_AL_B = L_{AB}$, $R_AR_B = R_{AB}$ and $L_AR_B = R_BL_A$, so $L$ is a representation of $E$ and $R$ of the opposite algebra $E^{\mathrm{op}}$ with commuting images, and the double centraliser theorem gives $\operatorname{End}(E) = L(E)R(E)\cong E\otimes E^{\mathrm{op}}$ with the commutant of $L(E)$ equal to $R(E)$ and conversely. The complex structure of $E$ is the central one-sided multiplication $J_E = L_i = R_i$, which commutes with every one-sided multiplication, whereas the complex structure of $V$ is the skew-adjoint unitary element $J \in E$; a real-linear operator on $E$ is complex-linear exactly when it commutes with $J_E$. When $h$ is a chosen Hermitian form on $V$, the operator algebra carries the Hermitian trace form $\langle X,Y\rangle = \operatorname{tr}(X^\dagger Y)$, positive definite, and the one-sided multiplications $L_U, R_U$ by a unitary $U$ are commuting isometries of it, so the unitary group acts on $E$ through two commuting unitary representations. The adjoints of the one-sided multiplications for the trace form, the signed variants and the module-level graded action are the companion articles of this group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V$, $h$, $n$ | the complex vector space, its Hermitian form, its dimension |
| $E = \operatorname{End}_{\mathbb C}(V)$ | the endomorphism algebra, of complex dimension $n^2$ |
| $A^\dagger$ | the adjoint of $A$ for $h$ |
| $L_A(X) = AX$, $R_B(X) = XB$ | the one-sided multiplications |
| $J_E = L_i = R_i$ | the complex structure of the operator algebra |
| $J$ | the complex structure of $V$, an element of $E$ |
| $\langle X,Y\rangle = \operatorname{tr}(X^\dagger Y)$ | the Hermitian trace form of $E$ |
| $\operatorname{End}(E) = L(E)R(E)$ | the double centraliser |

## Further Reading

- Frank W. Anderson and Kent R. Fuller, *Rings and Categories of Modules* (Springer, second edition, 1992), for the left and right multiplications, the double centraliser theorem and the commutant.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, second edition, 2001), for the one-sided multiplicative structure of an endomorphism algebra.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (Springer, 1974), for the complex structure, the adjoint and the unitary operators.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involution of an algebra of endomorphisms and its trace form.
