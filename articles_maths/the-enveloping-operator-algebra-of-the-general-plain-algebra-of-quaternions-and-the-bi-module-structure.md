# __The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure__

## Introduction

The left and right multiplications of $\mathbb{H}$ generate together an algebra of operators, and that algebra is the **enveloping algebra** $\mathbb{H}^{\mathrm{e}}=\mathbb{H}\otimes_\mathbb{R}\mathbb{H}^{\mathrm{op}}$. It is isomorphic to the full algebra of real-linear endomorphisms of the four-dimensional space, and the isomorphism is explicit: the elementary tensor $\tilde a\otimes\tilde b^{\mathrm{op}}$ acts as the sandwich $L_{\tilde a}R_{\tilde b}$, $\tilde q\mapsto\tilde a\tilde q\tilde b$. This article defines the enveloping algebra, identifies it with $\operatorname{End}_\mathbb{R}(\mathbb{H})$, writes the Conway operator basis and its composition rule, reads the one-sided operators as the edge rows and the two-sided operators as the elementary tensors, and describes the regular bimodule as a module over the enveloping algebra. The product and the operators are *Two-Sided Operators on the General Plain Algebra of Quaternions*, below this article in this category, and *One-Sided Operators on the General Plain Algebra of Quaternions*, below this article in this category; the transpose of a sandwich and the matrix formula $D\,G^{\mathsf T}D$ are *Association and the Transpose on the General Plain Algebra*, above this article in this category; the module category is *Modules over the General Plain Algebra of Quaternions*, above this article in this category.

## The Enveloping Algebra

**Definition.** The **enveloping algebra** of $\mathbb{H}$ is $\mathbb{H}^{\mathrm{e}}=\mathbb{H}\otimes_\mathbb{R}\mathbb{H}^{\mathrm{op}}$, the tensor product of the algebra with its opposite, of real dimension $16$.

**Theorem (the sandwich action).** The assignment $\tilde a\otimes\tilde b^{\mathrm{op}}\mapsto T_{\tilde a,\tilde b}$, where $T_{\tilde a,\tilde b}(\tilde q)=\tilde a\tilde q\tilde b$, extends uniquely to a representation of $\mathbb{H}^{\mathrm{e}}$ on the real vector space $\mathbb{H}$, and makes ${}_\mathbb{H}\mathbb{H}_\mathbb{H}$ a module over $\mathbb{H}^{\mathrm{e}}$.

*Proof.* The sandwich $T_{\tilde a,\tilde b}$ is bilinear in $(\tilde a,\tilde b)$, so it defines a linear map on the tensor product $\mathbb{H}\otimes_\mathbb{R}\mathbb{H}^{\mathrm{op}}$. It is multiplicative: $T_{\tilde a,\tilde b}T_{\tilde c,\tilde d}(\tilde q)=\tilde a\tilde c\,\tilde q\,\tilde d\tilde b=T_{\tilde a\tilde c,\tilde d\tilde b}(\tilde q)$, and $\tilde a\tilde c$ is the product in $\mathbb{H}$ while $\tilde d\tilde b$ is the product in $\mathbb{H}^{\mathrm{op}}$ of $\tilde b^{\mathrm{op}}$ and $\tilde d^{\mathrm{op}}$; so the map is an algebra homomorphism, and the associative law of the algebra is exactly the compatibility of the two actions.

## The Identification with the Endomorphisms

**Theorem.** The sandwich representation is an isomorphism $\mathbb{H}^{\mathrm{e}}\overset{\sim}{\to}\operatorname{End}_\mathbb{R}(\mathbb{H})$; both sides have real dimension $16$.

*Proof.* The map is a non-zero algebra homomorphism, since $e_0\otimes e_0^{\mathrm{op}}$ acts as the identity operator, and both algebras have real dimension $16$. The algebra $\mathbb{H}$ is central simple, and the tensor product of central simple algebras is central simple, so $\mathbb{H}^{\mathrm{e}}$ is simple; a non-zero homomorphism from a simple algebra into a ring is injective. Hence the map is injective, and by the equality of dimensions it is bijective.

**Corollary.** $\mathbb{H}^{\mathrm{e}}\cong\operatorname{End}_\mathbb{R}(\mathbb{H})\cong M_4(\mathbb{R})$, and $\mathbb{H}$ is a simple module over $\mathbb{H}^{\mathrm{e}}$.

*Proof.* The identification; the simplicity is the simplicity of ${}_\mathbb{H}\mathbb{H}$, a module over a quotient of $\mathbb{H}^{\mathrm{e}}$.

## The Conway Operator Basis

**Definition.** Following Conway, write $\tilde a[\,]\tilde b$ for the operator $\tilde q\mapsto\tilde a\tilde q\tilde b$. The sixteen operators $e_n[\,]e_m$, $n,m\in\{0,1,2,3\}$, are the **Conway operator basis** of $\mathbb{H}^{\mathrm{e}}$.

**Equivalent forms.** $e_n[\,]e_m=L_{e_n}R_{e_m}$, and $e_0[\,]e_m=R_{e_m}$ while $e_n[\,]e_0=L_{e_n}$.

## The Composition Rule

**Theorem.** $(e_a[\,]e_b)(e_c[\,]e_d)=(e_ae_c)[\,](e_de_b)$.

*Proof.* Apply the left side to $\tilde q$: $e_a\bigl(e_c\tilde qe_d\bigr)e_b=e_ae_c\,\tilde q\,e_de_b$, which is the right side.

**Corollary (structure constants).** Since $e_ae_c=\varepsilon(a,c)e_{a\oplus c}$ with $\varepsilon(a,c)=\pm1$ and $\oplus$ the quaternion group law on the indices, and $e_de_b=\varepsilon(d,b)e_{d\oplus b}$,

$$
(e_a[\,]e_b)(e_c[\,]e_d)=\varepsilon(a,c)\varepsilon(d,b)\,e_{a\oplus c}[\,]e_{d\oplus b}.
$$

*Proof.* Substitute the two basis products in the composition rule.

**Corollary (the transpose of the basis element).** $(e_n[\,]e_m)^{\sim}=e_m[\,]e_n$.

*Proof.* The transpose of a sandwich swaps its parameters, by *Association and the Transpose on the General Plain Algebra*, above this article in this category.

## The One-Sided Operators as Edge Rows

**Theorem.** The one-sided operators are the edge rows of the Conway basis:

$$
L_{e_n}=e_n[\,]e_0,\qquad R_{e_m}=e_0[\,]e_m .
$$

*Proof.* The definitions: $e_n[\,]e_0(\tilde q)=e_n\tilde q\,e_0=e_n\tilde q$ and $e_0[\,]e_m(\tilde q)=e_0\tilde qe_m=\tilde qe_m$.

**Corollary.** The left multiplications span the $4$-dimensional subspace $\mathbb{H}\otimes\mathbb{R}e_0^{\mathrm{op}}$ and the right multiplications the subspace $\mathbb{R}e_0\otimes\mathbb{H}^{\mathrm{op}}$; the two subspaces intersect in the scalars $\mathbb{R}(e_0[\,]e_0)$, the identity operator.

*Proof.* $L$ is injective, so the $L_{e_n}$ span a $4$-dimensional space, the first tensor factor; similarly the second. An operator that is both a left and a right multiplication is multiplication by a central element, that is a scalar, by the centre theorem.

## Two Commuting Copies

**Theorem.** The left and the right multiplications commute: $L_{\tilde a}R_{\tilde b}=R_{\tilde b}L_{\tilde a}$, and they generate $\mathbb{H}^{\mathrm{e}}$.

*Proof.* $L_{\tilde a}R_{\tilde b}(\tilde q)=\tilde a\tilde q\tilde b=R_{\tilde b}L_{\tilde a}(\tilde q)$ by associativity. The products $L_{\tilde a}R_{\tilde b}$ are the images of the elementary tensors, which span $\mathbb{H}^{\mathrm{e}}$.

Thus $\mathbb{H}^{\mathrm{e}}$ contains the two commuting copies $L(\mathbb{H})$ and $R(\mathbb{H})$ of $\mathbb{H}$ and of $\mathbb{H}^{\mathrm{op}}$, and it is their tensor product; the commutant of $L(\mathbb{H})$ inside $\operatorname{End}_\mathbb{R}(\mathbb{H})$ is $R(\mathbb{H})$, and conversely, the double centraliser of the two-sided action of $\mathbb{H}$ is the pair $(\mathbb{H},\mathbb{H}^{\mathrm{op}})$.

## The Two-Sided Operators as the Elementary Tensors

**Theorem.** The map $\tilde a\otimes\tilde b^{\mathrm{op}}\mapsto \tilde a[\,]\tilde b=L_{\tilde a}R_{\tilde b}$ is an $\mathbb{R}$-linear bijection from the $16$-dimensional tensor product onto the two-sided operators, with tensor rank the minimal number of sandwiches.

*Proof.* The map is the representation of the enveloping algebra, an isomorphism; the tensor rank statement is the definition of the rank of a tensor in $\mathbb{H}\otimes\mathbb{H}^{\mathrm{op}}$, transported by the isomorphism.

**Corollary.** The two-sided operators form the whole of $\operatorname{End}_\mathbb{R}(\mathbb{H})$: every real-linear operator of the four-dimensional space is a sandwich, and the Conway basis is a basis of the operator algebra.

*Proof.* The theorem and the identification above.

## The Regular Bimodule

**Theorem.** ${}_\mathbb{H}\mathbb{H}_\mathbb{H}$ is a module over $\mathbb{H}^{\mathrm{e}}$ by the sandwich action; it is the **standard module**, simple, of real dimension four, and the whole of $\mathbb{H}^{\mathrm{e}}$ acts faithfully on it.

*Proof.* The compatibility of the two actions is associativity, as in the sandwich theorem; faithfulness is injectivity of the representation, that is the identification. Simplicity and the module theory are *Modules over the General Plain Algebra of Quaternions*, above this article in this category.

**Corollary.** The enveloping algebra is the endomorphism algebra of its own standard module: $\mathbb{H}^{\mathrm{e}}=\operatorname{End}_\mathbb{R}({}_\mathbb{H}\mathbb{H}_\mathbb{H})$, and the centre of $\mathbb{H}^{\mathrm{e}}$ is the scalars acting by $T_{\lambda e_0,\lambda e_0}$, a one-dimensional space.

*Proof.* The identification with the endomorphisms; an operator commuting with all sandwiches is a scalar, since it must equal both a left and a right multiplication, and only the scalars are central.

## Comparison with the Complex Case

Over the biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ the same construction gives $\mathbb{B}^{\mathrm{e}}=\mathbb{B}\otimes_\mathbb{C}\mathbb{B}^{\mathrm{op}}\cong M_4(\mathbb{C})$, and the standard module is $\mathbb{B}$ itself, of complex dimension four and simple over $\mathbb{B}^{\mathrm{e}}$, exactly as $\mathbb{H}$ is of real dimension four and simple over $\mathbb{H}^{\mathrm{e}}$; the module that splits is the one-sided one, the left regular module of $M_2(\mathbb{C})$, which is two copies of its column module $S$.

| Feature | $\mathbb{H}$ | $\mathbb{B}$ |
|---|---|---|
| enveloping algebra | $\mathbb{H}\otimes_\mathbb{R}\mathbb{H}^{\mathrm{op}}\cong M_4(\mathbb{R})$ | $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}^{\mathrm{op}}\cong M_4(\mathbb{C})$ |
| scalar field of the tensor product | $\mathbb{R}$ | $\mathbb{C}$ |
| standard module | $\mathbb{H}$, simple | $\mathbb{B}\cong\mathbb{C}^4$, simple |
| left regular module over the algebra | $\mathbb{H}$, simple | $S\oplus S$, two copies of the column module $S$ |
| centre of the enveloping algebra | one-dimensional | one-dimensional |
| operator basis | $e_n[\,]e_m$ | $\tilde\Pi_n[\,]\tilde\Pi_m$ |

The two constructions differ only in the coefficient field: over $\mathbb{R}$ the operator algebra is a real matrix algebra and over $\mathbb{C}$ a complex one, and the standard module over the enveloping algebra is simple in both cases; the splitting into the two columns appears in the one-sided regular module of the matrix model, not in the standard module. The complex case is owned by the biquaternion chapter and is cited for the contrast alone.

## Summary

The enveloping algebra $\mathbb{H}^{\mathrm{e}}=\mathbb{H}\otimes_\mathbb{R}\mathbb{H}^{\mathrm{op}}$ has dimension $16$ and is isomorphic to the real-linear endomorphisms of $\mathbb{H}$ by the sandwich action $\tilde a\otimes\tilde b^{\mathrm{op}}\mapsto(\tilde q\mapsto\tilde a\tilde q\tilde b)$. Its Conway basis $e_n[\,]e_m$ obeys $(e_a[\,]e_b)(e_c[\,]e_d)=(e_ae_c)[\,](e_de_b)$, with structure constants read from the basis products; the one-sided operators are the edge rows $L_{e_n}=e_n[\,]e_0$ and $R_{e_m}=e_0[\,]e_m$; the left and right multiplications are two commuting copies whose product spans the algebra; and the two-sided operators are the elementary tensors, so that every real-linear operator is a sandwich. The regular bimodule is the standard simple module over $\mathbb{H}^{\mathrm{e}}$, faithful and of dimension four; over the complex case the same construction gives $M_4(\mathbb{C})$ and a standard module that is the algebra itself, of complex dimension four.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}^{\mathrm{e}}=\mathbb{H}\otimes_\mathbb{R}\mathbb{H}^{\mathrm{op}}$ | Enveloping algebra |
| $\tilde a[\,]\tilde b$ | The sandwich $\tilde q\mapsto\tilde a\tilde q\tilde b$ |
| $L_{\tilde a},R_{\tilde b}$ | Left and right multiplications |
| $e_n[\,]e_m$ | Conway operator basis, $16$ elements |
| $\varepsilon(a,c)$, $\oplus$ | Structure constants and index law of the basis products |

## Further Reading

- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the $[\,]$ operator notation and the composition of the sandwiches.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the enveloping algebra and its identification with the endomorphisms.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the double centraliser theorem and the standard module.
- Israel Nathan Herstein, *Noncommutative Rings* (Mathematical Association of America, 1968), for the centraliser and the tensor product of an algebra with its opposite.
