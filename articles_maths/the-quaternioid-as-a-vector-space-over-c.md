# __The Quaternioid as a Vector Space over $\mathbb{C}$__

## Introduction

The quaternion algebra $\mathbb{H}$ is a four-dimensional real vector space. It can be read over $\mathbb{C}$ by a chosen complex structure: a unit imaginary quaternion $\nu$ whose left multiplication makes $\mathbb{H}$ a two-dimensional complex vector space, a module over $\mathbb{C}_\nu=\mathbb{R}\oplus\mathbb{R}\nu$.

The single caution of the article: the field $\mathbb{C}_\nu$ is *not* the centre of $\mathbb{H}$. The centre of $\mathbb{H}$ is the scalar line $\mathbb{R}_{\mathbb{H}}$; the field $\mathbb{C}_\nu$ is a two-dimensional subalgebra, and different choices of $\nu$ give different subalgebras.

## The Reading by a Chosen Complex Structure

Let $\nu$ be a unit imaginary quaternion, $\nu^2=-1$, and let
$$
J=L_\nu:\mathbb{H}\longrightarrow\mathbb{H},\qquad J(\tilde q)=\nu\tilde q,
$$
be the left multiplication by $\nu$. Then $J^2=-\operatorname{id}$, since $\nu^2=-1$ and the product is associative, and $J$ is a **complex structure** on the real vector space $\mathbb{H}$: a real-linear map with square $-\operatorname{id}$.

**Proposition (dimension two).** With the scalar action
$$
(a+b\nu)\cdot \tilde q=a\tilde q+b\nu\tilde q=a \tilde q+b\,J(\tilde q) , \qquad a,b\in\mathbb{R},
$$
the real vector space $\mathbb{H}$ becomes a complex vector space of dimension two, a module over the field $\mathbb{C}_\nu=\mathbb{R}\oplus\mathbb{R}\nu=\mathbb{R}e_0\oplus\mathbb{R}\nu$. A complex basis is $(e_0,\mu)$ for any unit imaginary $\mu$ with $\mu\perp\nu$; the third unit is $\nu\mu$.

**Proof.** The action is the $\mathbb{R}$-bilinear extension of the real scalar action together with $J$, and $J^2=-\operatorname{id}$ makes it a complex scalar action. For the basis, write $\tilde q=q_0e_0+q_1\nu+q_2\mu+q_3\nu\mu$; the two halves are
$$
q_0e_0+q_1\nu=(q_0+q_1\nu)e_0 , \qquad q_2\mu+q_3\nu\mu=(q_2+q_3\nu)\mu ,
$$
using $\nu\cdot e_0=\nu e_0$ and $\nu\cdot \mu=\nu\mu$, so $\tilde q=(q_0+q_1\nu)e_0+(q_2+q_3\nu)\mu$ is a $\mathbb{C}_\nu$-combination of $e_0$ and $\mu$. The two generators are $\mathbb{C}_\nu$-independent: $z e_0+w \mu=0$ with $z=a+b\nu$, $w=c+d\nu$ reads $a e_0+c \mu+b \nu+d\,\nu\mu=0$ in the real basis $(e_0,\mu,\nu,\nu\mu)$, so $a=b=c=d=0$.

**Proposition (not a complex algebra).** For this scalar action the product of $\mathbb{H}$ is $\mathbb{R}$-bilinear but not $\mathbb{C}_\nu$-bilinear, so $\mathbb{H}$ is a module over $\mathbb{C}_\nu$ and not a $\mathbb{C}_\nu$-algebra. Explicitly, with $\lambda=\nu$, $\tilde p=\mu$ and $\tilde q=e_0$,
$$
\lambda(\tilde p\tilde q)=\nu(\mu e_0)=\nu\mu , \qquad \tilde p(\lambda \tilde q)=\mu(\nu e_0)=\mu\nu=-\nu\mu ,
$$
so the second slot fails; the first slot does not fail, since $\lambda(\tilde p\tilde q)=(\lambda \tilde p)\tilde q$ by associativity.

**Proof.** Left multiplication by $\lambda$ is associative and always passes to the first slot; the second slot requires commuting $\lambda$ past $\tilde p$, which holds for every $\tilde p$ only if $\lambda$ is central, and the only central elements are real. The witness shows the failure.

**Proposition (all choices are conjugate).** For two unit imaginary quaternions $\nu,\nu'$ there is a unit quaternion $a$ with $\nu'=a\nu a^{-1}$, and the inner automorphism $\iota_a(\tilde q)=a\tilde q a^{-1}$ carries the $\mathbb{C}_\nu$-structure to the $\mathbb{C}_{\nu'}$-structure, $\iota_a\circ J_\nu=J_{\nu'}\circ\iota_a$. Hence the complex structures on $\mathbb{H}$ are all conjugate under the inner automorphisms. The conjugating element is not unique: the units $a$ and $-a$ give the same automorphism, and the same holds for every unit quaternion of the plane $a\mathbb{C}_\nu$, since the elements commuting with $\nu$ are exactly the elements of $\mathbb{C}_\nu$.

**Proof.** Every unit imaginary quaternion is conjugate to $e_1$ by an inner automorphism, the inner automorphisms acting transitively on the sphere of unit imaginary quaternions, so the assignment $\nu\mapsto\mathbb{C}_\nu$ has one orbit. The commutation is the associativity rewrite $\iota_a(\nu\tilde q)=a \nu \tilde q a^{-1}=a \nu a^{-1}\,a \tilde q a^{-1}=\nu'\iota_a(\tilde q)$.

**Warning (the chosen field is not the centre).** The field $\mathbb{C}_\nu$ contains $\nu$, which does not commute with the unit imaginary $\mu$ orthogonal to it, $\nu\mu=-\mu\nu$. The centre of $\mathbb{H}$ is therefore not $\mathbb{C}_\nu$ but the scalar line $\mathbb{R}_{\mathbb{H}}=\mathbb{R}e_0$, of real dimension one. The quaternion algebra has a one-dimensional centre and infinitely many two-dimensional commutative subalgebras $\mathbb{C}_\nu$, one for each axis line of the vector subspace; the two are not to be confused. The axis lines and the subalgebras they carry are *The Group of Involutions of the Quaternioid*, below this article in this category, and the subalgebra description is *Introduction to the Remarkable Subspaces of the Quaternions*, below this article in this category.

## The Complex-Linear Maps

For the reading of the previous section, the $\mathbb{C}_\nu$-linear endomorphisms of $\mathbb{H}$ are the real-linear endomorphisms commuting with $J$,
$$
\operatorname{End}_{\mathbb{C}_\nu}(\mathbb{H})=\{T\in\operatorname{End}_{\mathbb{R}}(\mathbb{H}):TJ=JT\}.
$$
In a complex basis $(e_0,\mu)$ this is the matrix ring $M_2(\mathbb{C}_\nu)$, of complex dimension four and real dimension eight. Inside it the left multiplications $L_{\tilde p}$ of *The Quaternioid as a Vector Space over $\mathbb{R}$* occupy a distinguished part: $L_{\tilde p}$ is $\mathbb{C}_\nu$-linear exactly when $\tilde p$ commutes with $\nu$, that is, exactly when $\tilde p\in\mathbb{C}_\nu$, and then $L_{\tilde p}$ is the scalar multiplication by $\tilde p$. For $\tilde p$ outside $\mathbb{C}_\nu$ the left multiplication $L_{\tilde p}$ is real-linear alone. The right multiplications all commute with $J$ as well, since $R_{\tilde q}J(\tilde p)=R_{\tilde q}(\nu \tilde p)=(\nu \tilde p)\tilde q=\nu(\tilde p\tilde q)=JR_{\tilde q}(\tilde p)$ by associativity, so $R_{\tilde q}J=JR_{\tilde q}$ for every $\tilde q$; the two families sit in $\operatorname{End}_{\mathbb{C}_\nu}(\mathbb{H})$ on different footings, which is the asymmetry visible in the two slots of the product.

Worked witness: with $\nu=e_1$, $\mu=e_2$, the matrix of $J=L_{e_1}$ in the real basis $(e_0,e_1,e_2,e_3)$ is block diagonal with two copies of $\left(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\right)$; the centralizer of that matrix is $M_2(\mathbb{C})$ in the two complex coordinates, of real dimension eight.

## Summary

The quaternion algebra read over $\mathbb{C}$ through a chosen complex structure is a two-dimensional complex module. A chosen unit imaginary quaternion $\nu$ gives a complex structure $J=L_\nu$ and makes $\mathbb{H}$ a two-dimensional complex module over $\mathbb{C}_\nu$, with basis $(e_0,\mu)$; the product is not $\mathbb{C}_\nu$-bilinear, so $\mathbb{H}$ is a module and not a complex algebra, and $\mathbb{C}_\nu$ is a commutative subalgebra, not the centre. The choices $\nu$ are all conjugate by the inner automorphisms. The $\mathbb{C}_\nu$-linear maps are the centralizer of $J$, isomorphic to $M_2(\mathbb{C}_\nu)$; among the left multiplications only the scalars by $\mathbb{C}_\nu$ are complex-linear, while every right multiplication is.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{C}_\nu=\mathbb{R}\oplus\mathbb{R}\nu$ | the commutative subalgebra generated by a unit imaginary $\nu$ |
| $J=L_\nu$ | the complex structure $\tilde q\mapsto \nu\tilde q$, with $J^2=-\operatorname{id}$ |
| $(e_0,\mu)$ | a complex basis over $\mathbb{C}_\nu$, for $\mu\perp\nu$ unit imaginary |
| $\operatorname{End}_{\mathbb{C}_\nu}(\mathbb{H})$ | the centralizer of $J$, isomorphic to $M_2(\mathbb{C}_\nu)$ |

## Further Reading

- *The Quaternioid as a Vector Space over $\mathbb{R}$* (`articles_maths/the-quaternioid-as-a-vector-space-over-r.md`), for the real reading this article extends.
- *The Two General Products and the Reason There Are Only Two* (`articles_maths/the-two-general-products-and-the-reason-there-are-only-two.md`), below this article in this category, for the count of the products that the base changes produce.
- *The Group of Involutions of the Quaternioid* (`articles_maths/the-group-of-involutions-of-the-quaternioid.md`), below this article in this category, for the subalgebras $\mathbb{C}_\nu$ and the axis lines that carry them.
