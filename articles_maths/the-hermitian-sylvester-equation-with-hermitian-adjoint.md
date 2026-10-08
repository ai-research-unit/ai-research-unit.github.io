
# __The Hermitian Sylvester Equation with Hermitian Adjoint__

## Introduction

The **Hermitian Sylvester equation** is the linear equation

$$
X\,a + a^{\dagger}X = C
$$

for an unknown $X$ in the algebra, with $a$ and a right-hand side $C$ given. It is the equation whose solution operator is the two-sided operator $L_a(X) = a^{\dagger}X + Xa$, the sum of a left and a right multiplication, and it is the derivative of the Hermitian sandwich at the identity: the infinitesimal version of $x\mapsto \Phi(x)$ is a Sylvester operator with coefficient the element at which the derivative is taken. The equation is the Hermitian companion of the classical Sylvester equation $Xa - bX = C$ of linear algebra, and it inherits from the dagger a complete adjoint theory: the solution operator of the daggered coefficient is the adjoint, an equation with a self-adjoint coefficient has a self-adjoint solution operator, and a Hermitian right-hand side has a Hermitian solution.

The two structural facts are the adjunction $L_a^{*} = L_{a^{\dagger}}$, which is the abstract reason the Hermitian theory is consistent, and the preservation of the Hermitian part, $C^{*} = C\Rightarrow X^{*} = X$ when $L_a$ is invertible, which is the reason the equation is the one that occurs in the Cartan decomposition and in the theory of the Hermitian cone. The equation is treated here as an equation **on the Clifford algebra with the dagger**, so that its solution operator, its kernel, its positivity and its Hermitian solutions all carry the involution.

The two-sided operators and their adjoints are *Two-Sided Operators on a Clifford Algebra*; the Hermitian sandwich is *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint*; the self-adjoint and skew operators are *Self-Adjoint and Skew Operators with Hermitian Adjoint*; the spectra and the spectral theorem are *The Spectra of Self-Adjoint Operators with Hermitian Adjoint*; the trace and blade forms are *The Blade Form and the Hermitian Structure with Hermitian Adjoint*; the positivity and the cone are *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint*; the congruence classification of the classical Sylvester law is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, and the classical Sylvester equation of linear algebra is the ordinary-matrix case of the construction here.

## The Solution Operator

**Definition.** For $a\in\mathrm{Cl}(V,q)$ the **Hermitian Sylvester operator** with coefficient $a$ is

$$
L_a : \mathrm{Cl}(V,q)\longrightarrow \mathrm{Cl}(V,q), \qquad L_a(X) = a^{\dagger}X + Xa ,
$$

and the equation $L_a(X) = C$ is the **Hermitian Sylvester equation**.

**Proposition.** The operator is the sum of a left and a right multiplication, $L_a = L_{a^{\dagger}} + R_a$ in the notation of *Two-Sided Operators on a Clifford Algebra*, and it is $A$-linear.

**Theorem (adjunction).** The adjoint of the Sylvester operator is the Sylvester operator of the daggered coefficient:

$$
L_a^{*} = L_{a^{\dagger}} , \qquad \text{that is} \qquad \bigl(a^{\dagger}X + Xa\bigr)^{*} = aX + Xa^{\dagger}.
$$

**Proof.** For the Hermitian–Schmidt form $\langle X,Y\rangle = \mathrm{Sc}(X^{\dagger}Y)$ of *The Blade Form and the Hermitian Structure with Hermitian Adjoint*, use $L_b^{*} = L_{b^{\dagger}}$ and $R_b^{*} = R_{b^{\dagger}}$ of *Two-Sided Operators on a Clifford Algebra*: $L_a^{*} = (L_{a^{\dagger}} + R_a)^{*} = L_{(a^{\dagger})^{\dagger}} + R_{a^{\dagger}} = L_a + R_{a^{\dagger}} = L_{a^{\dagger}}$. This was checked on the regular module of $\mathrm{Cl}_{0,3}(\mathbb{R})$ against the Frobenius form: $L_a^{*} = L_{a^{\dagger}}$ for every tested $a$.

**Corollary (self-adjoint and skew-adjoint coefficients).** The Sylvester operator $L_a$ is self-adjoint iff $a$ is self-adjoint, $a^{\dagger} = a$, and skew-adjoint iff $a$ is skew-adjoint, $a^{\dagger} = -a$; in the skew case $L_a(X) = a^{\dagger}X + Xa = -aX + Xa = [X,a]$, the inner derivation by $a$, and its kernel is the centraliser of $a$ in the algebra. The two cases were checked: $L_a$ self-adjoint for a self-adjoint $a$ and skew-adjoint for a skew $a$, so the adjoint theory of the equation is exactly the adjoint theory of the coefficient.

## Solvability and the Hermitian Solution

### Uniqueness and the Hermitian Part

**Theorem (the Hermitian part is preserved).** Let $L_a$ be invertible. Then the equation has a unique solution $X$ for every $C$, and

$$
C^{\dagger} = C \ \Longrightarrow \ X^{\dagger} = X .
$$

So a Hermitian right-hand side has a Hermitian solution, and the solution operator restricts to an isomorphism of the Hermitian part of the algebra onto itself.

**Proof.** Adjoint the equation $a^{\dagger}X + Xa = C$: the left side becomes $X^{\dagger}a + a^{\dagger}X^{\dagger} = L_a(X^{\dagger})$, and the right side becomes $C^{\dagger} = C$; so $L_a(X^{\dagger}) = C = L_a(X)$ and $X^{\dagger} = X$ by injectivity of $L_a$.

**Corollary (the Hermitian Sylvester map).** The map $C\mapsto X = L_a^{-1}(C)$ is $A$-linear and satisfies $L_a^{-1}(C^{\dagger}) = L_a^{-1}(C)^{\dagger}$; it is thus a morphism of $\sigma$-modules, and it is self-adjoint for the Hermitian–Schmidt form exactly when $a$ is self-adjoint. For the real case ($\sigma = \mathrm{id}$) it preserves the symmetric part, and for a complex algebra it preserves the Hermitian part.

### The Kernel and the Eigenvalues

**Proposition (the kernel).** The kernel of $L_a$ consists of the $X$ with $a^{\dagger}X = -Xa$. If $a$ is skew-adjoint with $a^{2} = -1$ then $a$ generates a copy of $\mathbb{C}$ inside the algebra and the kernel contains its span $\mathrm{span}\{1,a\}$, since $L_a(1) = a^{\dagger} + a = 0$ and $L_a(a) = a^{\dagger}a + a^{2} = -a^{2} + a^{2} = 0$; if instead $a$ is self-adjoint with $a^{2} = -1$ then $L_a(a) = a^{2} + a^{2} = -2 \neq 0$, so $a$ is not in the kernel. In general the kernel is the set of $X$ on which the left multiplication by $a^{\dagger}$ agrees with the right multiplication by $-a$, and $L_a$ is injective exactly when there is no such $X$.

**Proof.** The equation $a^{\dagger}X = -Xa$ is the defining condition of the kernel; the two evaluations are immediate, and the last sentence is the statement that $L_a(X) = 0$ means the left and the right multiplications coincide on $X$ with the indicated signs.

**Remark.** The operator $L_a$ is finite-dimensional, so its invertibility is equivalent to the non-vanishing of its determinant; the eigenvalues of $L_a$ are the sums $\lambda_i + \mu_j$ of the eigenvalues of the left multiplication by $a^{\dagger}$ and of the right multiplication by $a$, so the equation is uniquely solvable exactly when no such sum vanishes. This is the Clifford form of the classical solvability condition of the Sylvester equation, and the same condition appears in the Lyapunov theory of stability.

### Positivity

**Theorem (the positive case).** Let $a$ be self-adjoint and suppose the algebra has a positive dagger, as in the definite case of *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint*. Then

$$
\langle L_a(X), X\rangle = \mathrm{Sc}\bigl((aX + Xa)^{\dagger}X\bigr) = 2\,\mathrm{Sc}(X^{\dagger}aX)
$$

for $X$ self-adjoint, and $L_a$ is positive definite iff $a$ lies in the interior of the Hermitian cone. The Sylvester equation with a positive coefficient is the linearised form of the exponential of the cone, and its solvability for every Hermitian $C$ is the statement that the cone is open in its linear span.

**Proof.** $(aX+Xa)^{\dagger}X = X^{\dagger}aX + aX^{\dagger}X$, and for $X$ self-adjoint the two terms are equal, giving $2X^{\dagger}aX$; its scalar part is positive for all $X\neq0$ exactly when $a$ is in the interior of the cone, by the definition of the cone in *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint*.

## The Differential Interpretation

**Proposition (the differential of the sandwich).** Let $\Phi(x) = x\,T\,x^{\dagger}$ be the Hermitian sandwich of *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint* with a fixed $T$, and let $x = x_0 + t\,h$ be a first-order variation. Then

$$
\Phi(x_0 + th) = \Phi(x_0) + t\,\bigl(h\,T\,x_0^{\dagger} + x_0\,T\,h^{\dagger}\bigr) + O(t^{2}) ,
$$

so the derivative is the sum of the two one-sided terms $h\mapsto h\,T\,x_0^{\dagger}$ and $h\mapsto x_0\,T\,h^{\dagger}$. It is a **Sylvester-type operator**: a left multiplication by the coefficient $x_0T$ applied to one factor and a right multiplication by $Tx_0^{\dagger}$ applied to the daggered factor, and its adjoint is obtained by the dagger, which exchanges the two terms and is the operator-level reason for the adjunction $L_a^{*} = L_{a^{\dagger}}$. The linearisation of the sandwich is therefore a Sylvester operator, and it occurs whenever the sandwich is differentiated, in the Cartan decomposition and in the exponential map of the operator group.

**Remark (Sylvester's law of inertia is a different statement).** The name of Sylvester attaches to two different theorems: this equation, and **Sylvester's law of inertia**, the statement that the inertia of a Hermitian form is a congruence invariant, proved in *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*. The equation above is a linear equation on the algebra; the law is the classification statement for the forms, and the two should not be conflated. The congruence version is the statement that the canonical form of a Hermitian form is unique, and the equation version is the statement that the linearised congruence can be solved.

## Worked Cases

### A Self-Adjoint Coefficient on a Definite Algebra

Let $A = \mathrm{Cl}_{0,3}(\mathbb{R})$, and let $a$ be the self-adjoint element $a = 1 + \tfrac12 e_1e_2$ (the scalar plus a bivector). Then $a$ is in the Hermitian part, and $L_a$ is self-adjoint for the Hermitian–Schmidt form; its kernel is trivial because the sums of the left and right eigenvalues do not vanish, so the equation $L_a(X) = C$ has a unique solution for every $C$, and a Hermitian $C$ has a Hermitian solution $X$. The example is the concrete instance in which every hypothesis of the theorems is satisfied: self-adjoint coefficient, positive definite dagger, invertible Sylvester operator, Hermitian solution.

### A Skew-Adjoint Coefficient and the Kernel

Let $a = e_1e_2$ in $\mathrm{Cl}_{0,3}(\mathbb{R})$, skew-adjoint with $a^{2} = -1$. Then $L_a(X) = [X,a]$, the inner derivation, and it is skew-adjoint; the kernel contains the centraliser of $a$, which is $\mathrm{span}\{1,a\}$ because $a$ generates a copy of $\mathbb{C}$ inside the algebra. The equation $[X,a] = C$ is solvable exactly for $C$ in the image of the derivation, and the solution is unique modulo the kernel: the example shows the kernel and the failure of invertibility in the skew case.

## Summary

The **Hermitian Sylvester equation** is $Xa + a^{\dagger}X = C$, whose solution operator is $L_a(X) = a^{\dagger}X + Xa = L_{a^{\dagger}} + R_a$. Its adjoint is $L_a^{*} = L_{a^{\dagger}}$, verified on the regular module against the Frobenius form, so $L_a$ is self-adjoint for a self-adjoint coefficient and skew-adjoint for a skew coefficient; in the skew case $L_a$ is the inner derivation $[X,a]$ and its kernel is the centraliser. When $L_a$ is invertible the equation has a unique solution for every $C$, and the **Hermitian part is preserved**: a Hermitian right-hand side gives a Hermitian solution, because $L_a(X^{\dagger}) = L_a(X)^{\dagger}$. The kernel is the eigenspace where $a^{\dagger}X = -Xa$, and the solvability condition is that no sum $\lambda_i+\mu_j$ of the left and right eigenvalues vanishes, the Clifford form of the classical Sylvester condition.

The equation with a **positive coefficient** is the linearised form of the Hermitian cone: on the self-adjoint part, $\langle L_a(X),X\rangle = 2\mathrm{Sc}(X^{\dagger}aX)$, which is positive definite exactly when $a$ is in the interior of the cone. The operator is the **derivative of the Hermitian sandwich** at the identity and consequently appears in the Cartan decomposition and in the linearisation of the congruence; the congruence-classification statement known as **Sylvester's law of inertia** is a different theorem, proved in the article on the unitary Witt group, and the two uses of the name are distinguished.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a(X) = a^{\dagger}X + Xa$ | Hermitian Sylvester operator |
| $L_a = L_{a^{\dagger}} + R_a$ | Left and right multiplication form |
| $L_a^{*} = L_{a^{\dagger}}$ | Adjunction of the solution operator |
| $a^{\dagger}=\pm a \Rightarrow L_a$ self/skew-adjoint | Adjointness follows the coefficient |
| $L_a(X)=C$ | The Hermitian Sylvester equation |
| $C^{\dagger}=C \Rightarrow X^{\dagger}=X$ | Preservation of the Hermitian part |
| $\ker L_a$: $a^{\dagger}X = -Xa$ | Kernel |
| $\langle L_a(X),X\rangle = 2\mathrm{Sc}(X^{\dagger}aX)$ | Positivity for a self-adjoint coefficient |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the Sylvester equation, the solvability condition on the spectra and the Lyapunov theory.
- Rajendra Bhatia, *Matrix Analysis*, Graduate Texts in Mathematics 169 (Springer, 1997), for the Lyapunov equation, the positivity of the solution operator and the stability interpretation.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces*, Graduate Studies in Mathematics 34 (American Mathematical Society, 2001), for the Cartan decomposition, the derivative of the conjugation and the role of the Sylvester operator in the exponential map.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the left and right multiplications, the derivation $[X,a]$ and the centraliser.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for the Hermitian part under an involution, the cone of positive elements and the adjoint theory of the solution operator.
