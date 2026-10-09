# __The Signed Left Multiplication on a Hilbert Space__

## Introduction

The signed left multiplication of a graded Hilbert space is the one-sided operator $\ell_U(T)=U\alpha(T)$, the left multiplication with its argument twisted by the grade involution $\alpha(T)=\Gamma T\Gamma$. It is the left factor out of which the signed sandwich is built, in the same way that the ordinary left multiplication is the left factor of the unsigned sandwich, and it shares with the ordinary one the cleanest properties of a one-sided operator: it is bounded with the same norm as its element, its products are unsigned left multiplications, it is invertible exactly when its element is, and it is an isometry exactly when its element is. What changes is the grading: the signed left multiplication is a coset of the unsigned one, obtained by composing with the involution on the outside, and its action on the graded pieces of $B(H)$ is what the sign rule of the graded category expresses.

The algebra $B(H)$ and its involution are *Bounded Operators on a Hilbert Space*; the unsigned left multiplication and its Hilbert–Schmidt structure are *The Left and Right Multiplication Operators on a Hilbert Space*; the signed sandwich that is assembled from the two signed one-sided multiplications is *The Signed Sandwich on a Hilbert Space*; the corresponding signed right multiplication and the adjoint of $\ell_U$ are *The Signed Adjoint Sandwich on a Hilbert Space* and *The Adjoint of the Left Multiplication on a Hilbert Space* below. The algebraic signed left multiplication is *The Signed Left Multiplication on a Graded Algebra* (Part II), of which the present article is the Hilbert-space reading.

Throughout, $H=H^0\oplus H^1$ is a graded Hilbert space over $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$, $\Gamma$ is the parity operator, $\alpha(T)=\Gamma T\Gamma$ is the grade involution of $B(H)$, and $\|T\|$ and $\|T\|_{\mathrm{HS}}$ are the operator and Hilbert–Schmidt norms. The **signed left multiplication** is $\ell_U(T)=U\alpha(T)=L_U\circ\alpha$ and the **signed right multiplication** is $\varrho_V(T)=\alpha(T)V=R_V\circ\alpha$; the unsigned left multiplication is $L_U(T)=UT$.

## The Signed Left Multiplication

**Definition.** For $U\in B(H)$ the **signed left multiplication** is

$$
\ell_U:B(H)\longrightarrow B(H),\qquad \ell_U(T)=U\,\alpha(T)=L_U\circ\alpha .
$$

**Proposition (boundedness and norm).** $\ell_U$ is a bounded linear operator on $B(H)$ with

$$
\|\ell_U\|=\|U\|,
$$

and the map $U\mapsto\ell_U$ is linear, injective and order-reversing under composition; the same identity holds for the Hilbert–Schmidt norm, $\|\ell_U(T)\|_{\mathrm{HS}}\le\|U\|\|T\|_{\mathrm{HS}}$ with equality for suitable $T$.

*Proof.* $\|U\alpha(T)\|\le\|U\|\|\alpha(T)\|=\|U\|\|T\|$ by the isometry of the grade involution, and the value $\|U\|$ is attained at a rank-one $T=\xi\otimes\bar\eta$ transforming in the even part of the grading with $\|U\xi\|=\|U\|\|\xi\|$; injectivity is the invertibility of $\alpha$ and the faithfulness of the left representation, and linearity is immediate.

**Proposition (action on the graded pieces).** If $T$ is even then $\ell_U(T)=UT$, if $T$ is odd then $\ell_U(T)=-UT$; hence

$$
\ell_U(T)=U\,T \quad\text{on the even part},\qquad \ell_U(T)=-U\,T \quad\text{on the odd part},
$$

and the signed left multiplication is the ordinary left multiplication with the sign $-1$ on the odd part.

*Proof.* $\alpha(T)=\varepsilon_T T$ with $\varepsilon_T=\pm1$ on the homogeneous parts, by the definition of $\alpha$.

**Proposition (the signed right multiplication).** The signed right multiplication is $\varrho_V(T)=\alpha(T)V$, and the two signed one-sided operators are related by

$$
\varrho_V=\alpha\circ R_V= R_V\circ\alpha ,
$$

so the signed right multiplication is the right multiplication with the same twist on the argument.

*Proof.* $\alpha(TV)=\alpha(T)\alpha(V)$, and $\alpha(V)=V$ only if $V$ is even; the correct statement is $\alpha(T)V=\varrho_V(T)$ by definition, and $\alpha(T)V=R_V(\alpha(T))$, which is $\varrho_V=R_V\alpha$; for the other order one has $\alpha(TV)=R_{\alpha(V)}\alpha(T)$, so the ordering of the twist matters and is fixed once and for all.

## Composition and the Coset

**Theorem (products).** For all $U,V,W\in B(H)$,

$$
\ell_U\,\ell_V=L_{U\alpha(V)},\qquad L_U\,\ell_V=\ell_{UV},\qquad \ell_U\,L_V=L_{U\alpha(V)},\qquad \ell_U\varrho_V=L_{U\alpha(V)} .
$$

So the product of two signed left multiplications is an unsigned left multiplication, the product of a signed and an unsigned one is signed, and the signed left multiplications form the coset

$$
\ell(B(H))=L(B(H))\,\alpha
$$

of the unsigned left multiplications inside $B(B(H))$.

*Proof.* $\ell_U(\ell_V(T))=U\alpha(V\alpha(T))=U\alpha(V)\alpha^2(T)=L_{U\alpha(V)}(T)$, using $\alpha^2=\mathrm{id}$; the remaining identities are the same computation with the involution applied to the inner factors, and they exhibit the coset structure.

**Corollary (the parity of the signed length).** The set $\{\ell_U\}\cup\{L_U\}$ is the algebra of left multiplications shifted by $\alpha$; the product is unsigned when the number of signed factors is even and signed when it is odd, and the quotient of the generated algebra by the unsigned subalgebra is $\mathbb{Z}/2$.

*Proof.* The composition rules add the numbers of signed factors modulo two, exactly as in the signed sandwich; the unsigned left multiplications form the index-two subalgebra.

**Proposition (faithfulness and the image).** The map $U\mapsto\ell_U$ is injective, so the signed left multiplications are parametrised by $B(H)$; the image is the set $L(B(H))\alpha$, and the map is not multiplicative, its failure being the twist $U V\mapsto U\alpha(V)$.

*Proof.* If $\ell_U=0$ then $U\alpha(T)=0$ for all $T$, and testing $T=I$ gives $U=0$; the parametrisation and the failure of multiplicativity are the composition rule $\ell_U\ell_V=L_{U\alpha(V)}$.

## Isometry, Invertibility and the Kernel

**Theorem (invertibility).** $\ell_U$ is invertible in $B(B(H))$ exactly when $U\in B(H)$ is invertible, and then

$$
(\ell_U)^{-1}=\ell_{\alpha(U)^{-1}}=\ell_{\alpha(U^{-1})}.
$$

*Proof.* $\ell_U\ell_W=L_{U\alpha(W)}=L_I$ exactly when $\alpha(W)=U^{-1}$, that is $W=\alpha(U^{-1})=\alpha(U)^{-1}$; the other order is analogous, and the inverse is a signed left multiplication. Invertibility of the product forces $U$ invertible since $\ell_U$ is a composite of the invertible $\alpha$ and the left multiplication by $U$.

**Proposition (isometry).** $\ell_U$ is isometric for the operator norm exactly when $U$ is isometric, and isometric for the Hilbert–Schmidt norm exactly when $U$ is isometric; it is a partial isometry exactly when $U$ is a partial isometry, and unitary exactly when $U$ is unitary.

*Proof.* $\|\ell_U(T)\|=\|U\alpha(T)\|$, and as $T$ ranges over the unit ball of $B(H)$ the operators $T$ and $\alpha(T)$ range over the same ball, so the norm of $\ell_U$ on the ball is that of $U$; the Hilbert–Schmidt statement is the same with the rank-one operators, and the partial-isometry and unitary statements are the special cases.

**Proposition (kernel and image).** For $U\in B(H)$,

$$
\ker\ell_U=\alpha^{-1}(\ker L_U)=\alpha(\ker U), \qquad \operatorname{im}\ell_U=U\,B(H),
$$

and the restriction of $\ell_U$ to the even and odd parts is $L_U$ and $-L_U$ respectively, so the kernel is the intersection of the kernel of the left multiplication with each graded piece taken with its sign.

*Proof.* $\ell_U(T)=0$ iff $U\alpha(T)=0$ iff $\alpha(T)\in\ker U$ iff $T\in\alpha(\ker U)$; the image is the range of the left multiplication by $U$; the graded description is the action on the homogeneous pieces.

## The Sandwich as a Composite

**Proposition.** The signed sandwich factors through the one-sided multiplications in two ways:

$$
S_{U,V}=L_U\,\varrho_V=\ell_U\,R_{\alpha(V)},
$$

and the unsigned sandwich is $T_{U,V}=L_UR_V$. So the signed sandwich is the signed right multiplication followed by the left multiplication by $U$, or equivalently the signed left multiplication followed by the right multiplication by $\alpha(V)$.

*Proof.* $(L_U\varrho_V)(T)=L_U(\alpha(T)V)=U\alpha(T)V=S_{U,V}(T)$, and $(\ell_UR_{\alpha(V)})(T)=\ell_U(T\alpha(V))=U\alpha(T)\alpha^2(V)=U\alpha(T)V$; the two expressions agree, and the unsigned case is associativity.

**Corollary (the composition table recovered).** The products of the signed sandwich computed in *The Signed Sandwich on a Hilbert Space* are the products of the factors displayed here, and the parity of the signed length is the parity of the numbers of signed one-sided factors.

*Proof.* Substituting the factorisations into the four general products and using $\alpha^2=\mathrm{id}$ gives the table.

**Example (finite dimension).** For $H=\mathbb{K}^{p+q}$ with $\Gamma=\operatorname{diag}(I_p,-I_q)$ the signed left multiplication by a block matrix $U=\begin{pmatrix}A&B\\C&D\end{pmatrix}$ acts on a block matrix $T=\begin{pmatrix}P&Q\\R&S\end{pmatrix}$ by

$$
\ell_U(T)=\begin{pmatrix}A&B\\C&D\end{pmatrix}\begin{pmatrix}P&-Q\\-R&S\end{pmatrix},
$$

so the signed left multiplication is the ordinary one with the off-diagonal blocks of the argument negated. The unsigned left multiplication is the same product without the sign, and the kernel is the kernel of $U$ transported by the sign reversal of the off-diagonal blocks.

**Example (the normal basis of a graded Hilbert space).** When $H$ has a homogeneous orthonormal basis, the signed left multiplication by a diagonal $U$ acts on the matrix units by $\ell_U(e_m\otimes\bar e_n)=\varepsilon_n u_m\,e_m\otimes\bar e_n$, where $\varepsilon_n$ is the sign of the grading of $e_n$; the eigenvalues of $\ell_U$ in this basis are the products of the diagonal entries with the graded signs, and $\ell_U$ is isometric exactly when these products all have modulus one.

## Summary

The signed left multiplication of a graded Hilbert space is $\ell_U(T)=U\alpha(T)=L_U\circ\alpha$, bounded with $\|\ell_U\|=\|U\|$, injective in $U$, and equal to the ordinary left multiplication with the sign $-1$ on the odd part. Its products obey $\ell_U\ell_V=L_{U\alpha(V)}$ and $L_U\ell_V=\ell_{UV}$, so the signed left multiplications form the coset $L(B(H))\alpha$ of the unsigned ones inside $B(B(H))$, with the parity of the signed length adding modulo two; it is invertible exactly when $U$ is, with $(\ell_U)^{-1}=\ell_{\alpha(U^{-1})}$, is isometric exactly when $U$ is, and is unitary exactly when $U$ is. Its kernel is $\alpha(\ker U)$ and its image is $U\,B(H)$. The signed sandwich factors through the two one-sided multiplications, $S_{U,V}=L_U\varrho_V=\ell_UR_{\alpha(V)}$, which recovers the composition table of the sandwich and exhibits the signed left multiplication as the elementary building block of the two-sided theory.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha(T)=\Gamma T\Gamma$ | the grade involution |
| $\ell_U(T)=U\alpha(T)=L_U\circ\alpha$ | the signed left multiplication |
| $\varrho_V(T)=\alpha(T)V=R_V\circ\alpha$ | the signed right multiplication |
| $\|\ell_U\|=\|U\|$ | the norm identity |
| $\ell_U\ell_V=L_{U\alpha(V)}$ | product of two signed left multiplications |
| $\ell(B(H))=L(B(H))\alpha$ | the coset of signed left multiplications |
| $(\ell_U)^{-1}=\ell_{\alpha(U^{-1})}$ | the inverse |
| $\ker\ell_U=\alpha(\ker U)$ | the kernel |
| $S_{U,V}=L_U\varrho_V=\ell_UR_{\alpha(V)}$ | the sandwich as a composite |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the one-sided multiplications of $B(H)$ and their compositions.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the elementary operators and their kernels.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the operators $T\mapsto AT$ on operator spaces.
- Pierre Deligne and John W. Morgan, "Notes on Supersymmetry", in *Quantum Fields and Strings: A Course for Mathematicians*, vol. 1 (American Mathematical Society, 1999), for the sign rule of graded multiplication.
