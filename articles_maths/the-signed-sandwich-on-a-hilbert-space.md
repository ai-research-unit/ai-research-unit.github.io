# __The Signed Sandwich on a Hilbert Space__

## Introduction

A two-sided operator on a Hilbert space multiplies its argument on the left and on the right; the **signed sandwich** inserts, between the two multiplications, the grade involution of a $\mathbb{Z}/2$-grading. Concretely, the Hilbert space is split as $H=H^0\oplus H^1$, the parity operator $\Gamma$ is $+\mathrm{id}$ on $H^0$ and $-\mathrm{id}$ on $H^1$, the grade involution of $B(H)$ is $\alpha(T)=\Gamma T\Gamma$, and the signed sandwich by $A$ and $B$ is

$$
S_{A,B}(T)=A\,\alpha(T)\,B .
$$

Because $\Gamma$ is a self-adjoint unitary, $\alpha$ is an isometric $*$-automorphism of $B(H)$, and the signed sandwich has the same norm as its unsigned counterpart, $S_{A,B}$ is invertible exactly when both $A$ and $B$ are, and the composite of two signed sandwiches is unsigned. This article fixes these facts, the composition table, the exact sequence relating the signed and unsigned families, the singular elements, and the reflections that the signed sandwiches with $B=A^{-1}$ realise.

The algebra $B(H)$ and its involution are *Bounded Operators on a Hilbert Space*; the unsigned sandwich and the multiplication operators are *The Left and Right Multiplication Operators on a Hilbert Space*; the algebraic signed sandwich and its coset structure are *The Signed Sandwich on a Banach Algebra* (Part II), of which this article is the Hilbert-space reading, and the signed left and right multiplications are *The Signed Left Multiplication on a Hilbert Space* below. The graded modules over the graded algebra $B(H)$ are *The Graded Action on a Module over a Hilbert Space*; the adjoints of the operators defined here are *The Signed Adjoint Sandwich on a Hilbert Space*.

Throughout, $H=H^0\oplus H^1$ is a $\mathbb{Z}/2$-graded Hilbert space over $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$, the summands are orthogonal, $\Gamma=P^0-P^1$ is the parity operator, and $\alpha(T)=\Gamma T\Gamma$ is the grade involution of $B(H)=\mathrm{End}(H)$; an element $T$ is **even** when $\alpha(T)=T$ and **odd** when $\alpha(T)=-T$, and every element is the sum of its even and odd parts. The unsigned sandwich is $T_{A,B}(T)=ATB$, the signed sandwich is $S_{A,B}(T)=A\,\alpha(T)\,B$, and composition is read from right to left.

## The Signed Sandwich and Its Norm

**Definition.** The **signed sandwich** by $A,B\in B(H)$ is

$$
S_{A,B}:B(H)\longrightarrow B(H),\qquad S_{A,B}(T)=A\,\alpha(T)\,B,
$$

and the **unsigned sandwich** is $T_{A,B}(T)=ATB$.

**Proposition (the grade involution).** The map $\alpha(T)=\Gamma T\Gamma$ is an involutive $*$-automorphism of $B(H)$: it is linear, multiplicative, $\alpha^2=\mathrm{id}$, and $\alpha(T^*)=\alpha(T)^*$. It is an isometry, $\|\alpha(T)\|=\|T\|$, and it preserves the Hilbert–Schmidt norm and the identity, $\alpha(I)=I$.

*Proof.* Conjugation by an invertible element is an automorphism, and $\Gamma^2=I$ makes it involutive; $\Gamma=\Gamma^*$ gives $\alpha(T^*)=\Gamma T^*\Gamma=(\Gamma T\Gamma)^*=(\alpha(T))^*$; the isometry and the Hilbert–Schmidt statement are the invariance of the norms under the unitary $\Gamma$, and $\alpha(I)=\Gamma\Gamma=I$.

**Proposition (boundedness and norm).** $S_{A,B}$ is a bounded operator on $B(H)$ with

$$
\|S_{A,B}\|=\|A\|\,\|B\| ,
$$

the norm being computed with respect to the operator norm; the same formula holds for the Hilbert–Schmidt norm on $S_2(H)$, where $\|S_{A,B}\|_{HS}=\|A\|\,\|B\|$.

*Proof.* $\|A\alpha(T)B\|\le\|A\|\|B\|\|\alpha(T)\|=\|A\|\|B\|\|T\|$, giving the upper bound; the value is attained at a rank-one $T=\xi\otimes\bar\eta$ for which $\alpha(T)=\varepsilon\,T$ and $\|ATB\|=\|A\|\|B\|$, so the bound is sharp. The Hilbert–Schmidt statement is the same computation with $\|\cdot\|_{\mathrm{HS}}$ in place of $\|\cdot\|$.

**Proposition (relation to the unsigned sandwich and the coset).** Every signed sandwich is the unsigned sandwich composed with the involution,

$$
S_{A,B}=T_{A,B}\circ\alpha ,
$$

so the signed sandwiches form the coset $T(B(H),B(H))\,\alpha$ of the unsigned ones inside $B(B(H))$, and the signed sandwich is the unsigned sandwich with the argument twisted. In particular $S_{A,B}=T_{A,B}$ for all $A,B$ exactly when $\alpha=\mathrm{id}$, that is when $H^1=0$.

*Proof.* $T_{A,B}(\alpha(T))=A\alpha(T)B=S_{A,B}(T)$ is the definition; the identity of the two families on all arguments forces $\alpha=\mathrm{id}$, and $\alpha=\mathrm{id}$ means $\Gamma=I$ and $H^1=0$.

## The Composition Table

**Theorem (products of two-sided operators).** For $A,B,C,D\in B(H)$,

$$
T_{A,B}\,T_{C,D}=T_{AC,\,DB},\qquad
T_{A,B}\,S_{C,D}=S_{AC,\,DB},\qquad
S_{A,B}\,T_{C,D}=S_{A\alpha(C),\,\alpha(D)B},\qquad
S_{A,B}\,S_{C,D}=T_{A\alpha(C),\,\alpha(D)B}.
$$

So the product of an even number of signed sandwiches is unsigned, the product of an odd number is signed, and the sign rule is the involution acting on the inner factors.

*Proof.* Each identity is associativity and $\alpha^2=\mathrm{id}$: for the last, $S_{A,B}(S_{C,D}(X))=A\alpha(C\alpha(X)D)B=A\alpha(C)\alpha^2(X)\alpha(D)B=A\alpha(C)X\alpha(D)B$, and the three others are the same computation with the involution applied to any subset of the inner factors.

**Corollary (the algebra generated by the two-sided operators).** The set of all two-sided operators $\{T_{A,B}\}\cup\{S_{A,B}\}$ is the algebra generated by the unsigned and signed sandwiches; it contains the unsigned sandwiches as the subalgebra of index two formed by the elements of even signed length, and the quotient is $\mathbb{Z}/2$.

*Proof.* The product rules express every product as a two-sided operator, so the set is closed under multiplication and is an algebra; the parity of the number of signed factors is additive, by the same rules, and gives the stated quotient.

**Proposition (the multiplication algebra comparison).** When $\alpha=\mathrm{id}$ the table reduces to the multiplication algebra of *The Left and Right Multiplication Operators on a Hilbert Space*, and when $\alpha$ is nontrivial the signed sandwiches are the extra operators obtained by first twisting the argument.

*Proof.* At $\alpha=\mathrm{id}$ one has $S_{A,B}=T_{A,B}$ and the first line is the composition of the multiplication algebra; the second statement is the definition of $S_{A,B}$.

## Invertibility and the Singular Elements

**Theorem (invertibility).** For $A,B\in B(H)$ the following are equivalent:

(i) $S_{A,B}$ is invertible in $B(B(H))$;

(ii) $T_{A,B}$ is invertible;

(iii) $A$ and $B$ are invertible in $B(H)$.

When these hold, $(S_{A,B})^{-1}=S_{A^{-1},B^{-1}}$ and $S_{A,B}S_{A^{-1},B^{-1}}=S_{A^{-1},B^{-1}}S_{A,B}=\mathrm{id}$.

*Proof.* Composition with the invertible $\alpha$ does not change invertibility, giving (i) $\iff$ (ii); for the sandwich of a Banach algebra, $T_{A,B}=L_AR_B$ is invertible exactly when $A$ and $B$ are, because $L_A$ is invertible exactly when $A$ is and $R_B$ exactly when $B$ is, and the two commute; the inverse formula is $S_{A,B}S_{A^{-1},B^{-1}}(T)=A\alpha(A^{-1})\alpha^2(T)\alpha(B^{-1})B=T$, using $\alpha^2=\mathrm{id}$.

**Definition.** The **singular set** of the signed sandwich is the set of pairs $(A,B)$ with $A$ or $B$ non-invertible; the **critical elements** are the $T$ for which $S_{A,B}$ or its adjoint annihilates $T$.

**Proposition (the singular set is a union of two hypersurfaces).** $S_{A,B}$ is non-invertible exactly when $A$ or $B$ lies in the complement of the invertible group, that is, exactly when $0\in\sigma(A)\cup\sigma(B)$; the non-invertible signed sandwiches are the union of the left-singular and right-singular families, and their intersection consists of the sandwiches with both factors singular.

*Proof.* The spectrum is the complement of the invertible set, and the theorem identifies the singular pairs with the complements of the two groups; the rest is set algebra.

## The Reflections

**Definition.** A **signed sandwich with inverse right factor** is $S_{U,U^{-1}}(T)=U\alpha(T)U^{-1}$; it is an automorphism of $B(H)$ whose square is the inner automorphism by $U\alpha(U)$, and it is a **reflection** exactly when $U\alpha(U)$ is central.

**Proposition (the reflection criterion).** $S_{U,U^{-1}}$ is an involutive automorphism of $B(H)$ if and only if $U\alpha(U)=\lambda I$ for a scalar $\lambda$; since $U\alpha(U)$ is unitary, $|\lambda|=1$, and the involutivity requires $\lambda=1$ unless $U\alpha(U)=-I$, in which case the square is the identity as well. Hence $S_{U,U^{-1}}$ is a reflection exactly when $U\alpha(U)=\pm I$.

*Proof.* The square is the conjugation $T\mapsto U\alpha(U)\,T\,(U\alpha(U))^{-1}$, which is the identity exactly when $U\alpha(U)$ is central; the centre of $B(H)$ is the scalars, and $\|U\alpha(U)\|=1$ so the scalar is unimodular; the square of the conjugation by $\lambda I$ is the identity for every scalar $\lambda$, and the signed sandwich has order two up to the sign carried by the involution, which is the statement $S_{U,U^{-1}}^2=\iota_{U\alpha(U)}$.

**Remark.** The reflections of the Hilbert space are studied in *Reflections as Signed Two-Sided Operators on a Hilbert Space* below, where the unitary slice and the failure of the reflection property in the degenerate case $\alpha=\mathrm{id}$ are treated; the adjoint theory of the reflection is *The Signed Adjoint of the Reflection on a Hilbert Space*.

## Worked Cases

### The Matrix Algebra

For $H=\mathbb{K}^{p+q}$ with $H^0=\mathbb{K}^p$, $H^1=\mathbb{K}^q$ and $\Gamma=\operatorname{diag}(I_p,-I_q)$, the algebra $B(H)$ is $M_{p+q}(\mathbb{K})$ and the grade involution acts on a block matrix by

$$
\alpha\begin{pmatrix}A&B\\C&D\end{pmatrix}=\begin{pmatrix}A&-B\\-C&D\end{pmatrix},
$$

so the signed sandwich by $U$ and $V$ keeps the diagonal blocks and reverses the sign of the off-diagonal blocks. This is the block action of the graded matrix algebra, and it is the finite-dimensional model of the general signed sandwich.

### The Parity Operator

The parity operator $\Gamma$ is even, $\alpha(\Gamma)=\Gamma$, and the signed sandwich $S_{I,I}$ is the grade involution $\alpha$ itself. The even part $S_{I,I}=\alpha$ has eigenvalue $+1$ on the even operators and $-1$ on the odd operators, so the eigenvalues of the signed sandwich by the identity are the two signs of the grading, with eigenspaces the even and odd subspaces of $B(H)$.

### A Non-Invertible Signed Sandwich

For $A$ the projection onto $H^0$ and $B=I$, the sandwich $S_{A,I}(T)=A\alpha(T)$ has nontrivial kernel: it annihilates every operator whose image lies in $H^1$. So the singular set of the previous section is not merely a set of measure zero among the sandwiches; it is realisable by an explicit projection.

## Summary

On a graded Hilbert space $H=H^0\oplus H^1$ with parity operator $\Gamma$ and grade involution $\alpha(T)=\Gamma T\Gamma$, the signed sandwich $S_{A,B}(T)=A\alpha(T)B$ is a bounded operator on $B(H)$ of norm $\|A\|\|B\|$, equal to the unsigned sandwich composed with the involution, $S_{A,B}=T_{A,B}\circ\alpha$. The products of two signs obey $T_{A,B}S_{C,D}=S_{AC,DB}$ and $S_{A,B}S_{C,D}=T_{A\alpha(C),\alpha(D)B}$, so the parity of the signed length is additive and the two-sided operators form an algebra with a $\mathbb{Z}/2$-quotient; the signed sandwich is invertible exactly when both factors are, with $S_{A,B}^{-1}=S_{A^{-1},B^{-1}}$, and the non-invertible sandwiches form the union of the left-singular and right-singular families. The signed sandwich $S_{U,U^{-1}}$ is a reflection exactly when $U\alpha(U)=\pm I$, and its adjoint theory, the module structure and the reflections are the subjects of the companion articles of the group; in finite dimension the block-matrix model exhibits the sign reversal of the off-diagonal blocks directly.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H=H^0\oplus H^1$ | the graded Hilbert space, orthogonal summands |
| $\Gamma=P^0-P^1$ | the parity operator, self-adjoint unitary |
| $\alpha(T)=\Gamma T\Gamma$ | the grade involution of $B(H)$ |
| $T_{A,B}(T)=ATB$ | the unsigned sandwich |
| $S_{A,B}(T)=A\alpha(T)B$ | the signed sandwich |
| $\|S_{A,B}\|=\|A\|\|B\|$ | the norm of a signed sandwich |
| $S_{A,B}=T_{A,B}\circ\alpha$ | signed as unsigned composed with the involution |
| $S_{A,B}S_{C,D}=T_{A\alpha(C),\alpha(D)B}$ | product of two signed sandwiches |
| $S_{U,U^{-1}}$ | reflection candidate, involutive iff $U\alpha(U)$ central |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vols. 1–2 (Academic Press, 1983–1986), for the two-sided multiplications and the graded structure of $B(H)$.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the elementary operators of Hilbert space and their products.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the sandwich operators $T\mapsto ATB$ and their spectra.
- Pierre Deligne and John W. Morgan, "Notes on Supersymmetry", in *Quantum Fields and Strings: A Course for Mathematicians*, vol. 1 (American Mathematical Society, 1999), for the sign rule of the graded category.
